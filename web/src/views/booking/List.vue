<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_booking :to="{ name: 'BookingHistory' }">
        <a-button type="primary">History</a-button>
      </router-link>
    </template>
    <a-card>
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
            <router-link v-action:view_booking :to="{ name: 'BookingDetail', params: { id: data.id } }">
              <span>Detail</span>
            </router-link>
          </template>
        </template>
      </s-table>
    </a-card>
  </page-header-wrapper>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getBookings } from '@/api/booking'
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
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Remark',
          dataIndex: 'remark',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Author',
          dataIndex: 'author',
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
          const { data, extra } = res.result
          return data
        })
      }
    }
  }
}
</script>

<style></style>
