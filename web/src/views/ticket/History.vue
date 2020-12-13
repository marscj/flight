<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_ticket :to="{ name: 'AllTickets' }">
        <a-button type="primary">Back</a-button>
      </router-link>
    </template>
    <a-card>
      <div class="table-page-search-wrapper">
        <form-validate layout="inline" :form="queryParam">
          <a-row :gutter="24">
            <a-col :md="6" :sm="24">
              <form-item-validate label="TID">
                <a-input v-model="queryParam.id" @pressEnter="() => $refs.table.refresh()"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :md="12" :sm="24">
              <form-item-validate label="History">
                <a-range-picker v-model="date" @change="() => $refs.table.refresh()" />
              </form-item-validate>
            </a-col>

            <a-col :md="24" :sm="24">
              <form-item-validate>
                <a-input-search
                  v-model="queryParam.search"
                  placeholder="E.g Title or Operator"
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
import { getTicketHistories } from '@/api/ticket'
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
          title: 'TID',
          dataIndex: 'id',
          align: 'center',
          width: '80px',
          sorter: true
        },
        {
          title: 'Type',
          dataIndex: 'history_type',
          align: 'center',
          width: '80px'
        },
        {
          title: 'Date',
          dataIndex: 'history_date',
          scopedSlots: { customRender: 'history_date' },
          align: 'center',
          ellipsis: true
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
          title: 'Author',
          dataIndex: 'author',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Operator',
          dataIndex: 'history_user',
          align: 'center',
          ellipsis: true
        }
      ],
      loadData: parameter => {
        return getTicketHistories(Object.assign(parameter, Object.assign({}, this.queryParam, {}))).then(res => {
          const { result } = res
          return result
        })
      }
    }
  }
}
</script>

<style></style>
