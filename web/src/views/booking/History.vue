<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_booking :to="{ name: 'AllBookings' }">
        <a-button type="primary">Back</a-button>
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

            <a-col :md="6" :sm="24">
              <form-item-validate label="BID">
                <a-input v-model="queryParam.history_id" @pressEnter="() => $refs.table.refresh()"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :md="12" :sm="24">
              <form-item-validate label="History Date">
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
import { getBookingHistories } from '@/api/booking'
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
          dataIndex: 'history_id',
          align: 'center',
          width: '80px',
          sorter: true
        },
        {
          title: 'BID',
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
          title: 'Operator',
          dataIndex: 'history_user',
          align: 'center',
          ellipsis: true
        }
      ],
      loadData: parameter => {
        return getBookingHistories(
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
          const { result } = res
          return result
        })
      }
    }
  }
}
</script>

<style></style>
