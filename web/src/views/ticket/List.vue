<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_ticket :to="{ name: 'TicketHistory' }">
        <a-button type="primary">History</a-button>
      </router-link>
    </template>
    <a-card>
      <div class="table-page-search-wrapper">
        <form-validate layout="inline" :form="queryParam">
          <a-row :gutter="24">
            <a-col :md="6" :sm="24">
              <form-item-validate label="ID">
                <a-input v-model="queryParam.id" @pressEnter="() => $refs.table.refresh()"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :md="12" :sm="24">
              <form-item-validate label="Create">
                <a-range-picker v-model="date" @change="() => $refs.table.refresh()" />
              </form-item-validate>
            </a-col>

            <a-col :md="24" :sm="24">
              <form-item-validate>
                <a-input-search
                  v-model="queryParam.search"
                  placeholder="E.g Serial No. or Author"
                  enter-button="Search"
                  @search="() => $refs.table.refresh()"
                />
              </form-item-validate>
            </a-col>
          </a-row>
        </form-validate>
      </div>
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
import moment from 'moment'

export default {
  components: {
    STable,
    FormValidate,
    FormItemValidate
  },
  data() {
    return {
      date: [],
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
          title: 'Author',
          dataIndex: 'author',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Create',
          dataIndex: 'date',
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
        return getTickets(
          Object.assign(
            parameter,
            Object.assign(
              {
                date_before:
                  this.date != null && this.date.length > 0 ? moment(this.date[1]).format('YYYY-MM-DD') : undefined,
                date_after:
                  this.date != null && this.date.length > 0 ? moment(this.date[0]).format('YYYY-MM-DD') : undefined
              },
              this.queryParam
            )
          )
        ).then(res => {
          const { data, extra } = res.result
          return data
        })
      }
    }
  }
}
</script>
