<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_ticket :to="{ name: 'TicketHistory' }">
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
            <router-link v-action:view_ticket :to="{ name: 'TicketDetail', params: { id: data.id } }">
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
import { getTickets } from '@/api/ticket'
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
          title: 'Serial No',
          dataIndex: 'serial_no',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'User',
          dataIndex: 'user',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Line',
          dataIndex: 'air_line',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Info',
          dataIndex: 'air_info',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Class',
          dataIndex: 'air_class',
          align: 'center'
        },
        {
          title: 'Fare',
          dataIndex: 'fare',
          align: 'center'
        },
        {
          title: 'Tax',
          dataIndex: 'tax',
          align: 'center'
        },
        {
          title: 'Total',
          dataIndex: 'total',
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
        return getTickets(Object.assign(parameter, Object.assign({}, this.queryParam, {}))).then(res => {
          const { data, extra } = res.result
          return data
        })
      }
    }
  }
}
</script>
