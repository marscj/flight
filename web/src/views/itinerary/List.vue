<template>
  <div>
    <s-table
      ref="table"
      size="default"
      :rowKey="record => record.id"
      :columns="columns"
      :data="loadData"
      showPagination="auto"
      :pageURI="true"
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
    </s-table>
    <!-- <a-button style="width: 100%; margin-top: 16px; margin-bottom: 8px" type="dashed" icon="plus" @click="newMember"
      >Add Itinerary</a-button
    > -->
  </div>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getBookings, createBooking } from '@/api/booking'
import { FormValidate, FormItemValidate } from '@/components'

export default {
  components: {
    STable,
    FormValidate,
    FormItemValidate
  },
  data() {
    return {
      queryParam: {
        name: undefined
      },
      columns: [
        {
          title: 'ID',
          dataIndex: 'id',
          align: 'center',
          width: '80px',
          sorter: true
        },
        {
          title: 'Title',
          dataIndex: 'title',
          align: 'center'
        },
        {
          title: 'Remark',
          dataIndex: 'remark',
          align: 'center',
          ellipsis: true
        },

        {
          title: 'Action',
          width: '100px',
          scopedSlots: { customRender: 'action' },
          align: 'center'
        }
      ],
      loadData: parameter => {
        return getBookings(Object.assign(parameter, Object.assign({}, this.queryParam, {}))).then(res => {
          return res.result
        })
      }
    }
  }
}
</script>

<style></style>
