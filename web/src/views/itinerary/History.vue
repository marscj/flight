<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_itinerary :to="{ name: 'AllItineraries' }">
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
        :scroll="{ x: 1500 }"
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
          width: '80px',
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
          width: '160px'
        },
        {
          title: 'Email',
          dataIndex: 'email',
          align: 'center',
          width: '180px',
          ellipsis: true
        },
        {
          title: 'Name',
          dataIndex: 'name',
          align: 'center',
          width: '160px',
          ellipsis: true
        },
        {
          title: 'Passport No',
          dataIndex: 'passport_no',
          align: 'center',
          width: '160px',
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
          console.log(res.result)
          return res.result
        })
      }
    }
  }
}
</script>

<style></style>
