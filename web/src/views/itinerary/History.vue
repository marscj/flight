<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_itinerary :to="{ name: 'AllItineraries' }">
        <a-button type="primary">Back</a-button>
      </router-link>
    </template>

    <a-card>
      <div class="table-page-search-wrapper">
        <form-validate layout="inline" :form="queryParam">
          <a-row :gutter="24">
            <a-col :md="6" :sm="24">
              <form-item-validate label="IID">
                <a-input v-model="queryParam.id" @pressEnter="() => $refs.tableList.refresh()"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :md="6" :sm="24">
              <form-item-validate label="Booking ID">
                <a-input v-model="queryParam.booking_id" @pressEnter="() => $refs.tableList.refresh()"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :md="6" :sm="24">
              <form-item-validate label="Ticket ID">
                <a-input v-model="queryParam.ticket_id" @pressEnter="() => $refs.tableList.refresh()"></a-input>
              </form-item-validate>
            </a-col>

            <a-col :md="6" :sm="24">
              <form-item-validate label="History">
                <a-range-picker v-model="date" @change="() => $refs.tableList.refresh()" />
              </form-item-validate>
            </a-col>

            <a-col :md="24" :sm="24">
              <form-item-validate>
                <a-input-search
                  v-model="queryParam.search"
                  placeholder="E.g Serial No. or Email or Name or Passport"
                  enter-button="Search"
                  @search="search"
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
        :scroll="{ x: 1200 }"
      >
        <template slot="is_lock" slot-scope="data">
          <a-checkbox :checked="data" disabled />
        </template>
      </s-table>
    </a-card>
  </page-header-wrapper>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getItineraryHistories } from '@/api/itinerary'
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
          sorter: true
        },
        {
          title: 'IID',
          dataIndex: 'id',
          align: 'center',
          sorter: true
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
        },
        {
          title: 'Serial No',
          dataIndex: 'serial_no',
          align: 'center'
        },
        {
          title: 'Email',
          dataIndex: 'email',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Name',
          dataIndex: 'name',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Passport No',
          dataIndex: 'passport_no',
          align: 'center',
          ellipsis: true
        },
        {
          title: 'Travel Plan',
          align: 'center',
          children: [
            {
              title: 'Entry',
              dataIndex: 'entry',
              align: 'center',
              ellipsis: true
            },
            {
              title: 'Exit',
              dataIndex: 'exit',
              align: 'center',
              ellipsis: true
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
              ellipsis: true
            },
            {
              title: 'Ticket2',
              dataIndex: 'ticket2',
              align: 'center',
              ellipsis: true
            }
          ]
        },
        {
          title: 'Hotel',
          dataIndex: 'hotel',
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
          title: 'Lock',
          dataIndex: 'is_lock',
          align: 'center',
          width: '80px',
          ellipsis: true,
          scopedSlots: { customRender: 'is_lock' }
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
        return getItineraryHistories(Object.assign(parameter, Object.assign({}, this.queryParam, {}))).then(res => {
          return res.result
        })
      }
    }
  }
}
</script>

<style></style>
