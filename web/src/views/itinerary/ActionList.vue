<template>
  <a-card class="card" title="Itineraries" :bordered="false" v-action:view_itinerary>
    <a-table
      ref="table"
      size="default"
      :rowKey="record => record.id"
      :columns="columns"
      :data-source="data"
      :loading="loading"
      :pagination="false"
      :scroll="{ x: 1500 }"
      bordered
    >
      <template slot="serial_no" slot-scope="text, record, index">
        <a-input v-if="record.editable" v-model="data[index].serial_no" :disabled="record.loading" />
        <template v-else>{{ text }}</template>
      </template>

      <template slot="email" slot-scope="text, record, index">
        <a-input
          allowClear
          v-if="record.editable"
          v-model="data[index].email"
          :disabled="record.loading"
          @click="openModal(data[index])"
        />
        <template v-else>{{ text }}</template>
      </template>

      <template slot="name" slot-scope="text, record, index">
        <a-input allowClear v-if="record.editable" v-model="data[index].name" :disabled="record.loading" />
        <template v-else>{{ text }}</template>
      </template>

      <template slot="passport_no" slot-scope="text, record, index">
        <a-input allowClear v-if="record.editable" v-model="data[index].passport_no" :disabled="record.loading" />
        <template v-else>{{ text }}</template>
      </template>

      <template slot="entry" slot-scope="text, record, index">
        <a-textarea v-if="record.editable" v-model="data[index].entry" :rows="5" :disabled="record.loading" />
        <template v-else>{{ text }}</template>
      </template>

      <template slot="exit" slot-scope="text, record, index">
        <a-textarea v-if="record.editable" v-model="data[index].exit" :rows="5" :disabled="record.loading" />
        <template v-else>{{ text }}</template>
      </template>

      <template slot="ticket1" slot-scope="text, record, index">
        <a-textarea v-if="record.editable" v-model="data[index].ticket1" :rows="5" :disabled="record.loading" />
        <template v-else>{{ text }}</template>
      </template>

      <template slot="ticket2" slot-scope="text, record, index">
        <a-textarea v-if="record.editable" v-model="data[index].ticket2" :rows="5" :disabled="record.loading" />
        <template v-else>{{ text }}</template>
      </template>

      <template slot="hotel" slot-scope="text, record, index">
        <a-textarea
          v-if="record.editable"
          v-model="data[index].hotel"
          :rows="5"
          :disabled="record.loading"
        ></a-textarea>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="remark" slot-scope="text, record, index">
        <a-textarea
          v-if="record.editable"
          v-model="data[index].remark"
          :rows="5"
          :disabled="record.loading"
        ></a-textarea>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="is_lock" slot-scope="text, record, index">
        <a-checkbox
          v-if="record.editable"
          v-model="data[index].is_lock"
          :disabled="record.loading || !$auth('lock_itinerary')"
        />
        <template v-else>
          <a-checkbox v-model="data[index].is_lock" disabled />
        </template>
      </template>

      <template slot="action" slot-scope="data">
        <template v-if="data.loading">
          <a-spin :spinning="data.loading"></a-spin>
        </template>
        <template v-else>
          <template v-if="data.editable">
            <a @click="cancel(data)">Cancel</a>
            <a-divider type="vertical" />
            <a @click="save(data)">Save</a>
          </template>
          <template v-else>
            <a-popconfirm
              title="Are you sure cancel?"
              @confirm="remove(data)"
              okText="Yes"
              cancelText="No"
              v-action:delete_itinerary
            >
              <a>Delete</a>
            </a-popconfirm>

            <a-divider type="vertical" v-action:change_itinerary />

            <a @click="toggle(data)" v-action:change_itinerary>Edit</a>
          </template>
        </template>
      </template>
    </a-table>
    <a-button class="w-full mt-4 mb-4 h-12" type="dashed" icon="plus" @click="newMember" v-action:add_itinerary
      >Add Itinerary</a-button
    >

    <a-modal v-model="modal" title="Select User" width="80%">
      <user-list-table :modal="true" @select="onSelect" />
    </a-modal>
  </a-card>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getItineraries, updateItinerary, createItinerary, deleteItinerary } from '@/api/itinerary'
import { FormValidate, FormItemValidate } from '@/components'
import UserListTable from '@/views/user/ListTable'

export default {
  components: {
    Ellipsis,
    FormValidate,
    FormItemValidate,
    UserListTable
  },
  mounted() {
    this.loadData()
  },
  methods: {
    loadData() {
      this.loading = true
      getItineraries({ booking_id: parseInt(this.$route.params.id) })
        .then(res => {
          const { data } = res.result
          this.data = Object.assign(
            [],
            data.map(f => {
              f.isNew = false
              f.editable = false
              f.loading = false
              return f
            })
          )
        })
        .finally(() => {
          this.loading = false
        })
    },
    newMember() {
      const length = this.data.length
      this.data.push({
        id: length === 0 ? 1 : this.data[length - 1].id + 1,
        serial_no: '',
        email: '',
        name: '',
        passport_no: '',
        entry: '',
        exit: '',
        ticket1: '',
        ticket2: '',
        hotel: '',
        remark: '',
        is_lock: false,

        editable: true,
        isNew: true,
        loading: false
      })
    },
    toggle(data) {
      const target = this.data.find(item => item.id === data.id)
      target._originalData = { ...target }
      target.editable = !target.editable
    },
    setData(id, data) {
      if (id == null) return
      let target = this.data.find(item => item.id === id)
      if (target == null) return
      Object.assign(target, data)
    },
    save(data) {
      const { id } = data

      var form = Object.assign({
        serial_no: data.serial_no,
        email: data.email,
        name: data.name,
        passport_no: data.passport_no,
        entry: data.entry,
        exit: data.exit,
        ticket1: data.ticket1,
        ticket2: data.ticket2,
        hotel: data.hotel,
        remark: data.remark,
        is_lock: data.is_lock,
        booking_id: parseInt(this.$route.params.id)
      })

      if (data.isNew) {
        this.setData(id, { loading: true })
        createItinerary(form)
          .then(res => {
            const { data } = res.result
            this.setData(
              id,
              Object.assign(data, {
                editable: false,
                isNew: false,
                loading: false
              })
            )
          })
          .catch(error => {
            this.$notification.error({
              message: this.getMessage(error),
              description: this.getDescription(error)
            })
          })
          .finally(() => {
            this.setData(id, { loading: false })
          })
      } else {
        this.setData(data.id, { loading: true })
        updateItinerary(data.id, form)
          .then(res => {
            const { data } = res.result
            this.setData(
              data.id,
              Object.assign(data, {
                editable: false,
                isNew: false,
                loading: false
              })
            )
          })
          .catch(error => {
            this.$notification.error({
              message: this.getMessage(error),
              description: this.getDescription(error)
            })
          })
          .finally(() => {
            this.setData(data.id, { loading: false })
          })
      }
    },
    getMessage(error) {
      if (
        error != null &&
        error.response != null &&
        error.response.data != null &&
        error.response.data.result != null
      ) {
        if (error.response.data.result['serial_no'] != null) return 'Serial No'
        if (error.response.data.result['email'] != null) return 'Email'
        if (error.response.data.result['name'] != null) return 'name'
        if (error.response.data.result['passport_no'] != null) return 'Passport No'
        if (error.response.data.result['entry'] != null) return 'Entry'
        if (error.response.data.result['exit'] != null) return 'Eixt'
        if (error.response.data.result['ticket1'] != null) return 'Ticket1'
        if (error.response.data.result['ticket2'] != null) return 'Ticket2'
        if (error.response.data.result['hotel'] != null) return 'Hotel'
        if (error.response.data.result['remark'] != null) return 'Remark'
        if (error.response.data.result['is_lock'] != null) return 'Lock'
      }
      return 'Error'
    },
    getDescription(error) {
      console.log(error.response)
      if (
        error != null &&
        error.response != null &&
        error.response.data != null &&
        error.response.data.result != null
      ) {
        return (
          error.response.data.result['serial_no'] ||
          error.response.data.result['email'] ||
          error.response.data.result['name'] ||
          error.response.data.result['passport_no'] ||
          error.response.data.result['entry'] ||
          error.response.data.result['exit'] ||
          error.response.data.result['ticket1'] ||
          error.response.data.result['ticket2'] ||
          error.response.data.result['hotel'] ||
          error.response.data.result['remark'] ||
          error.response.data.result['is_lock'] ||
          error.response.data.result['detail'] ||
          error.response.data.result['non_field_errors']
        )
      }

      return ''
    },
    remove(data) {
      if (data.isNew) {
        const newData = this.data.filter(item => item.id !== data.id)
        this.data = newData
      } else {
        this.setData(data.id, { loading: true })
        deleteItinerary(data.id)
          .then(res => {
            this.loadData()
          })
          .catch(error => {
            this.$notification.error({
              message: this.getMessage(error),
              description: this.getDescription(error)
            })
          })
          .finally(() => {
            this.setData(data.id, { loading: false })
          })
      }
    },
    cancel(data) {
      const target = this.data.find(item => item.id === data.id)
      if (target.isNew) {
        this.remove(data)
      } else {
        Object.keys(target).forEach(key => {
          target[key] = target._originalData[key]
        })
        target._originalData = undefined
      }
    },
    openModal(data) {
      this.modal = true
      this.modalData = data
    },
    onSelect(data) {
      this.modal = false
      Object.assign(this.modalData, {
        email: data.email,
        name: data.name,
        passport_no: data.passport_no
      })
      this.setData(this.modalData.id, this.modalData)
    }
  },
  data() {
    return {
      data: [],
      loading: false,
      form: {},
      modal: false,
      modalData: {},
      columns: [
        {
          title: 'Serial No',
          dataIndex: 'serial_no',
          align: 'center',
          width: '160px',
          scopedSlots: { customRender: 'serial_no' }
        },
        {
          title: 'Email',
          dataIndex: 'email',
          align: 'center',
          width: '180px',
          ellipsis: true,
          scopedSlots: { customRender: 'email' }
        },
        {
          title: 'Name',
          dataIndex: 'name',
          align: 'center',
          width: '160px',
          ellipsis: true,
          scopedSlots: { customRender: 'name' }
        },
        {
          title: 'Passport No',
          dataIndex: 'passport_no',
          align: 'center',
          width: '160px',
          ellipsis: true,
          scopedSlots: { customRender: 'passport_no' }
        },
        {
          title: 'Travel Plan',
          align: 'center',
          children: [
            {
              title: 'Entry',
              dataIndex: 'entry',
              align: 'center',
              ellipsis: true,
              scopedSlots: { customRender: 'entry' }
            },
            {
              title: 'Exit',
              dataIndex: 'exit',
              align: 'center',
              ellipsis: true,
              scopedSlots: { customRender: 'exit' }
            }
          ]
        },
        {
          title: 'Quotation',
          align: 'center',
          children: [
            {
              title: 'Ticket1',
              dataIndex: 'ticket1',
              align: 'center',
              ellipsis: true,
              scopedSlots: { customRender: 'ticket1' }
            },
            {
              title: 'Ticket2',
              dataIndex: 'ticket2',
              align: 'center',
              ellipsis: true,
              scopedSlots: { customRender: 'ticket2' }
            }
          ]
        },
        {
          title: 'Hotel',
          dataIndex: 'hotel',
          align: 'center',
          ellipsis: true,
          scopedSlots: { customRender: 'hotel' }
        },
        {
          title: 'Remark',
          dataIndex: 'remark',
          align: 'center',
          ellipsis: true,
          scopedSlots: { customRender: 'remark' }
        },
        {
          title: 'Lock',
          dataIndex: 'is_lock',
          align: 'center',
          width: '80px',
          ellipsis: true,
          scopedSlots: { customRender: 'is_lock' }
        },
        {
          title: 'Action',
          width: '120px',
          scopedSlots: { customRender: 'action' },
          align: 'center'
        }
      ]
    }
  }
}
</script>
<style>
.ant-table-thead > tr > th {
  padding: 8px 2px;
  font-size: 12px;
}
</style>
