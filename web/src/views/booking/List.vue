<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_booking :to="{ name: 'BookingHistory' }">
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

            <a-col :md="18" :sm="24">
              <form-item-validate label="Create At">
                <a-range-picker v-model="date" @change="() => $refs.table.refresh()" />
              </form-item-validate>
            </a-col>

            <a-col :md="24" :sm="24">
              <form-item-validate>
                <a-input-search
                  v-model="queryParam.search"
                  placeholder="E.g Title or Author"
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
        return getBookings(
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

<style></style>
