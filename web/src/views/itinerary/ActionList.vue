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
    <a-modal v-model="modal" :title="form.id != null ? 'Edit Itinerary' : 'Add Itinerary'">
      <form-validate ref="observer" :form="form"> </form-validate>
    </a-modal>
  </div>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getItineraries, createBooking } from '@/api/itinerary'
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
          title: 'Name',
          dataIndex: 'name',
          align: 'center',
          scopedSlots: { customRender: 'name' }
        },
        {
          title: 'Email',
          dataIndex: 'email',
          align: 'center',
          scopedSlots: { customRender: 'email' }
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
          title: 'Lock',
          dataIndex: 'is_lock',
          align: 'center',
          scopedSlots: { customRender: 'is_lock' }
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
