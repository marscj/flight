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
      <template slot="action" slot-scope="data">
        <template>
          <router-link v-action:view_booking :to="{ name: 'BookingHistory', params: { id: data.id } }">
            <span>History</span>
          </router-link>

          <a-divider type="vertical" />

          <a
            @click="
              () => {
                modal = true
                form = data
              }
            "
            >Edit</a
          >
        </template>
      </template>
    </a-table>
    <a-button
      class="w-full mt-4 mb-4 h-12"
      type="dashed"
      icon="plus"
      @click="
        () => {
          modal = true
          form = {}
        }
      "
      >Add Itinerary</a-button
    >
    <a-modal v-model="modal" :title="form.id != null ? 'Edit Itinerary' : 'Add Itinerary'" width="80%">
      <div class="table-page-search-wrapper">
        <form-validate ref="observer" :form="form" layout="inline" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
          <a-row :gutter="24">
            <a-col :xl="12" :md="12" :sm="24">
              <form-item-validate label="Serial No" vid="serial_no">
                <a-input v-model="form.serial_no"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :xl="12" :md="12" :sm="24"
              ><form-item-validate label="Email" vid="email">
                <a-input v-model="form.email"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :xl="12" :md="12" :sm="24"
              ><form-item-validate label="Name" vid="name">
                <a-input v-model="form.name"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :xl="12" :md="12" :sm="24">
              <form-item-validate label="Passport No" vid="passport_no">
                <a-input v-model="form.passport_no"></a-input> </form-item-validate
            ></a-col>

            <a-col :xl="12" :md="12" :sm="24"
              ><form-item-validate label="Entry" vid="entry">
                <a-input v-model="form.entry"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :xl="12" :md="12" :sm="24"
              ><form-item-validate label="Exit" vid="exit">
                <a-input v-model="form.exit"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :xl="12" :md="12" :sm="24">
              <form-item-validate label="Ticket1" vid="ticket1">
                <a-input v-model="form.ticket1"></a-input> </form-item-validate
            ></a-col>

            <a-col :xl="12" :md="12" :sm="24">
              <form-item-validate label="Ticket2" vid="ticket2">
                <a-input v-model="form.ticket2"></a-input> </form-item-validate
            ></a-col>

            <a-col :xl="12" :md="12" :sm="24">
              <form-item-validate label="Hotel" vid="ticket2">
                <a-textarea v-model="form.hotel"></a-textarea>
              </form-item-validate>
            </a-col>

            <a-col :xl="12" :md="12" :sm="24"
              ><form-item-validate label="Remark" vid="ticket2">
                <a-textarea v-model="form.remark"></a-textarea>
              </form-item-validate>
            </a-col>

            <a-col :xl="12" :md="12" :sm="24">
              <form-item-validate label="Lock" vid="ticket2">
                <a-checkbox v-model="form.is_lock"></a-checkbox> </form-item-validate
            ></a-col>

            <a-col :xl="12" :md="12" :sm="24"> </a-col>
          </a-row>
        </form-validate>
      </div>
    </a-modal>
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
          this.data = Object.assign([], result)
        })
        .finally(() => {
          this.loading = false
        })
    }
  },
  data() {
    return {
      data: [],
      loading: false,
      form: {},
      modal: false,
      columns: [
        {
          title: 'Serial No',
          dataIndex: 'serial_no',
          align: 'center',
          width: '80px',
          scopedSlots: { customRender: 'serial_no' }
        },
        {
          title: 'Email',
          dataIndex: 'email',
          align: 'center',
          scopedSlots: { customRender: 'email' }
        },
        {
          title: 'Name',
          dataIndex: 'name',
          align: 'center',
          scopedSlots: { customRender: 'name' }
        },
        {
          title: 'Passport No',
          dataIndex: 'passport_no',
          align: 'center',
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
              scopedSlots: { customRender: 'entry' }
            },
            {
              title: 'Exit',
              dataIndex: 'exit',
              align: 'center',
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
              scopedSlots: { customRender: 'ticket1' }
            },
            {
              title: 'Ticket2',
              dataIndex: 'ticket2',
              align: 'center',
              scopedSlots: { customRender: 'ticket2' }
            }
          ]
        },
        {
          title: 'Hotel',
          dataIndex: 'hotel',
          align: 'center',
          scopedSlots: { customRender: 'hotel' }
        },
        {
          title: 'Remark',
          dataIndex: 'remark',
          align: 'center',
          scopedSlots: { customRender: 'remark' }
        },
        {
          title: 'Lock',
          dataIndex: 'is_lock',
          align: 'center',
          scopedSlots: { customRender: 'is_lock' }
        },
        {
          title: 'Action',
          width: '100px',
          scopedSlots: { customRender: 'action' },
          align: 'center',
          fixed: 'right'
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
