<template>
  <div>
    <a-table
      ref="table"
      size="default"
      :columns="columns"
      :data-source="data"
      :loading="loading"
      :scroll="{ x: 1380 }"
      :pagination="false"
      bordered
    >
      <template
        v-for="(col, i) in [
          'serial_no',
          'email',
          'name',
          'passport_no',
          'entry',
          'exit',
          'ticket1',
          'ticket2',
          'is_lock',
          'hotel',
          'remark'
        ]"
        :slot="col"
        slot-scope="text, record"
      >
        <a-input
          :key="col"
          v-if="record.editable"
          style="margin: -5px 0"
          :value="text"
          :placeholder="columns[i].title"
          @change="e => handleChange(e.target.value, record.key, col)"
        />
        <template v-else>{{ text }}</template>
      </template>

      <template slot="action" slot-scope="data">
        <template>
          <router-link v-action:view_booking :to="{ name: 'BookingHistory', params: { id: data.id } }">
            <span>History</span>
          </router-link>

          <a-divider type="vertical" />

          <router-link v-action:view_booking :to="{ name: 'BookingDetail', params: { id: data.id } }">
            <span>Edit</span>
          </router-link>
        </template>
      </template>
    </a-table>
    <a-button style="width: 100%; margin-top: 16px; margin-bottom: 8px" type="dashed" icon="plus" @click="newMember"
      >Add Itinerary</a-button
    >
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
        key: length === 0 ? '1' : (parseInt(this.data[length - 1].key) + 1).toString(),
        serial_no: '',
        name: '',
        email: '',
        editable: true,
        passport_no: '',
        entry: '',
        exit: '',
        ticket1: '',
        ticket2: '',
        is_lock: false,
        hotel: '',
        remark: ''
      })
    },
    handleChange(value, key, column) {
      const newData = [...this.data]
      const target = newData.find(item => key === item.key)
      if (target) {
        target[column] = value
        this.data = newData
      }
    }
  },
  data() {
    return {
      data: [],
      loading: false,
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
