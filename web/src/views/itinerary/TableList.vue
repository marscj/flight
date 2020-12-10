<template>
  <s-table
    ref="table"
    size="default"
    :rowKey="record => record.id"
    :columns="columns"
    :data="loadData"
    showPagination="auto"
    :pageURI="true"
    :rowSelection="{
      selectedRowKeys: selectedRowKeys,
      onChange: onSelectChange,
      getCheckboxProps: record => ({
        props: {
          disabled: false
        }
      })
    }"
    bordered
    :scroll="{ x: 1500 }"
  >
    <template slot="is_lock" slot-scope="data">
      <a-checkbox :checked="data" disabled />
    </template>
  </s-table>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getItineraries } from '@/api/itinerary'
import { FormValidate, FormItemValidate } from '@/components'

export default {
  components: {
    STable,
    FormValidate,
    FormItemValidate
  },
  props: {
    rowSelection: {
      type: Object,
      default: null
    }
  },
  methods: {
    onSelectChange(selectedRowKeys) {
      this.selectedRowKeys = selectedRowKeys
    }
  },
  data() {
    return {
      selectedRowKeys: [],
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
        }
      ],
      loadData: parameter => {
        return getItineraries(Object.assign(parameter, Object.assign({}, this.queryParam, {}))).then(res => {
          const { data } = res.result
          return data
        })
      }
    }
  }
}
</script>

<style></style>
