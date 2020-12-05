<template>
  <div>
    <a-table
      ref="table"
      size="default"
      :rowKey="record => record.id"
      :columns="columns"
      :data-source="data"
      :loading="loading"
      bordered
    >
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
    <!-- <a-button style="width: 100%; margin-top: 16px; margin-bottom: 8px" type="dashed" icon="plus" @click="newMember"
      >Add Itinerary</a-button
    > -->
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
      columns: [
        {
          title: 'ID',
          dataIndex: 'id',
          align: 'center',
          width: '80px'
        },
        {
          title: 'Name',
          dataIndex: 'name',
          align: 'center'
        },
        {
          title: 'Action',
          width: '100px',
          scopedSlots: { customRender: 'action' },
          align: 'center'
        }
      ]
    }
  }
}
</script>
