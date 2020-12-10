<template>
  <a-card class="card" title="Related Itineraries" :bordered="false">
    <a-table
      ref="table"
      size="default"
      :rowKey="record => record.id"
      :columns="columns"
      :data-source="data"
      :pagination="false"
      :scroll="{ x: 1500 }"
      bordered
    >
      <template slot="is_lock" slot-scope="data">
        <a-checkbox :checked="data" disabled />
      </template>
    </a-table>

    <a-button
      type="primary"
      class="text-center w-full h-12 mt-4"
      @click="
        () => {
          modal = true
        }
      "
      >Related Itinerary</a-button
    >
    <a-modal v-model="modal" title="Related Itinerary" width="90%">
      <template slot="footer">
        <a-button key="submit" type="primary" :disabled="selectedRowKeys.length == 0" @click="handleOk">
          Select
        </a-button>
      </template>
      <itinerary-table-list
        :rowSelection="{
          selectedRowKeys: selectedRowKeys,
          onChange: onSelectChange,
          getCheckboxProps: record => ({
            props: {
              disabled: false,
              checked: true
            }
          })
        }"
        :tableData="loadData"
      />
    </a-modal>
  </a-card>
</template>

<script>
import ItineraryTableList from '@/views/itinerary/TableList'
import { getItineraries } from '@/api/itinerary'

export default {
  components: {
    ItineraryTableList
  },
  props: {
    data: {
      type: Array,
      default: undefined
    }
  },
  watch: {
    data(val) {
      this.selectedRowKeys = val != null ? val.map(f => f.id) : []
    }
  },
  methods: {
    handleOk() {
      var data = this.selectedRowKeys.map(f => {
        return this.modalData.find(f1 => f1.id === f)
      })

      this.modal = false
      this.$emit('select', data)
    },
    onSelectChange(selectedRowKeys) {
      this.selectedRowKeys = selectedRowKeys
    }
  },
  data() {
    return {
      tableData: [],
      modalData: [],
      selectedRowKeys: [],
      modal: false,
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
          this.modalData = Object.assign([], data.data)
          return data
        })
      }
    }
  }
}
</script>
