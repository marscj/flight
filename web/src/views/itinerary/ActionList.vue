<template>
  <div>
    <a-table
      ref="table"
      size="default"
      :rowKey="record => record.id"
      :columns="columns"
      :data-source="data"
      :loading="loading"
      :scroll="{ x: 1380 }"
      :pagination="false"
      bordered
    >
      <template slot="serial_no" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="email" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="name" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="passport_no" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="entry" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="exit" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="ticket1" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="ticket2" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="hotel" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="remark" slot-scope="text, data">
        <a-input v-if="data.editable" :value="text"></a-input>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="is_lock" slot-scope="text, data">
        <a-checkbox v-if="data.editable" :value="text"></a-checkbox>
        <template v-else>{{ text }}</template>
      </template>

      <template slot="action" slot-scope="data">
        <template v-if="data.editable">
          <a @click="toggle(data.id)">Cancel</a>
          <a-divider type="vertical" />
          <a @click="toggle(data.id)">Save</a>
        </template>
        <template v-else>
          <router-link v-action:view_booking :to="{ name: 'BookingHistory', params: { id: data.id } }">
            <span>History</span>
          </router-link>

          <a-divider type="vertical" />

          <a @click="toggle(data.id)">Edit</a>
        </template>
      </template>
    </a-table>
    <a-button class="w-full mt-4 mb-4 h-12" type="dashed" icon="plus" @click="newMember">Add Itinerary</a-button>
  </div>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getItineraries, updateItinerary, createItinerary, deleteItinerary } from '@/api/itinerary'
import { FormValidate, FormItemValidate } from '@/components'

export default {
  components: {
    STable,
    Ellipsis,
    FormValidate,
    FormItemValidate
  },
  props: {
    bookingId: {
      type: Number,
      default: undefined
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    loadData() {
      this.loading = true
      getItineraries({ booking_id: this.bookingId })
        .then(res => {
          const { result } = res
          this.data = Object.assign(
            [],
            result.map(f => {
              f.editable = false
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
        id: length === 0 ? '1' : (parseInt(this.data[length - 1].id) + 1).toString(),
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
        editable: true
      })
    },
    toggle(id) {
      const target = this.data.find(item => item.id === id)
      target._originalData = { ...target }
      target.editable = !target.editable
    }
  },
  data() {
    return {
      data: [],
      loading: false,
      form: {},
      columns: [
        {
          title: 'Serial No',
          dataIndex: 'serial_no',
          align: 'center',
          width: '180px',
          scopedSlots: { customRender: 'serial_no' }
        },
        {
          title: 'Email',
          dataIndex: 'email',
          align: 'center',
          width: '180px',
          scopedSlots: { customRender: 'email' }
        },
        {
          title: 'Name',
          dataIndex: 'name',
          align: 'center',
          width: '140px',
          scopedSlots: { customRender: 'name' }
        },
        {
          title: 'Passport No',
          dataIndex: 'passport_no',
          align: 'center',
          width: '140px',
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
              width: '180px',
              scopedSlots: { customRender: 'entry' }
            },
            {
              title: 'Exit',
              dataIndex: 'exit',
              align: 'center',
              width: '180px',
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
              width: '180px',
              scopedSlots: { customRender: 'ticket1' }
            },
            {
              title: 'Ticket2',
              dataIndex: 'ticket2',
              align: 'center',
              width: '180px',
              scopedSlots: { customRender: 'ticket2' }
            }
          ]
        },
        {
          title: 'Hotel',
          dataIndex: 'hotel',
          align: 'center',
          width: '180px',
          scopedSlots: { customRender: 'hotel' }
        },
        {
          title: 'Remark',
          dataIndex: 'remark',
          align: 'center',
          width: '180px',
          scopedSlots: { customRender: 'remark' }
        },
        {
          title: 'Lock',
          dataIndex: 'is_lock',
          align: 'center',
          width: '100px',
          scopedSlots: { customRender: 'is_lock' }
        },
        {
          title: 'Action',
          width: '180px',
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
