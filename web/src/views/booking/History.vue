<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_booking :to="{ name: 'AllBookings' }">
        <a-button type="primary">Back</a-button>
      </router-link>
    </template>
    <a-card>
      <s-table
        ref="table"
        size="default"
        :rowKey="record => record.history_id"
        :columns="columns"
        :data="loadData"
        showPagination="auto"
        :pageURI="true"
        bordered
      >
        <template slot="history_date" slot-scope="data">
          <span>{{ data }}</span>
        </template>
      </s-table>
    </a-card>
  </page-header-wrapper>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getBookingHistories } from '@/api/booking'
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
          dataIndex: 'history_id',
          align: 'center',
          width: '80px',
          sorter: true
        },
        {
          title: 'BookingID',
          dataIndex: 'id',
          align: 'center',
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
          title: 'Type',
          dataIndex: 'history_type',
          align: 'center'
        },
        {
          title: 'Date',
          dataIndex: 'history_date',
          scopedSlots: { customRender: 'history_date' },
          align: 'center'
        }
      ],
      loadData: parameter => {
        return getBookingHistories(Object.assign(parameter, Object.assign({}, this.queryParam, {}))).then(res => {
          const { result } = res
          console.log(result)
          return result
        })
      }
    }
  }
}
</script>

<style></style>
