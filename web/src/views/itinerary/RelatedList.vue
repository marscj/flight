<template>
  <a-card class="card" title="Related Itineraries">
    <a-table
      ref="table"
      size="default"
      :rowKey="record => record.id"
      :columns="columns"
      :data-source="data"
      :pagination="false"
      :loading="loading"
      :scroll="{ x: 1200 }"
      bordered
    >
      <template slot="is_lock" slot-scope="data">
        <a-checkbox :checked="data" disabled />
      </template>
    </a-table>

    <a-button
      type="primary"
      class="text-center w-full h-12 mt-4"
      :disabled="loading || disabled"
      @click="
        () => {
          modal = true
        }
      "
      >Related Itinerary</a-button
    >
    <a-modal v-model="modal" title="Change Itinerary" width="90%">
      <template slot="footer">
        <a-button key="submit" type="primary" @click="handleOk">
          Select
        </a-button>
      </template>
      <itinerary-table-list
        @onData="onData"
        :rowSelection="{
          hideDefaultSelections: true,
          type: 'radio',
          selectedRowKeys: selectedRowKeys,
          onChange: onSelectChange,
          getCheckboxProps: record => ({
            props: {
              disabled: record.ticket != null && !data.find(f => f.id == record.id)
            }
          })
        }"
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
    disabled: {
      type: Boolean,
      default: false
    }
  },
  watch: {
    data(val) {
      this.$emit('select', val)
      this.selectedRowKeys = val.map(f => f.id)
    }
  },
  mounted() {
    if (this.$route.params.id) {
      this.getData()
    } else {
      this.data = Object.assign([], this.$route.params.itinerary)
    }
  },
  methods: {
    getData() {
      this.loading = true
      getItineraries({
        ticket_id: this.$route.params.id
      })
        .then(res => {
          const { data } = res.result
          this.data = Object.assign([], data)
        })
        .finally(() => {
          this.loading = false
        })
    },
    handleOk() {
      var data = this.selectedRowKeys.map(f => {
        return this.modalData.find(f1 => f1.id === f)
      })

      this.modal = false
      this.data = Object.assign([], data)
    },
    onData(data) {
      this.modalData = Object.assign([], data)
    },
    onSelectChange(selectedRowKeys) {
      this.selectedRowKeys = selectedRowKeys
    }
  },
  data() {
    return {
      loading: false,
      data: [],
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
          width: '80px'
        },
        {
          title: 'Serial No',
          dataIndex: 'serial_no',
          align: 'center',
          width: '160px',
          scopedSlots: { customRender: 'serial_no' }
        },
        {
          title: 'Email',
          dataIndex: 'email',
          align: 'center',
          width: '180px',
          ellipsis: true,
          scopedSlots: { customRender: 'email' }
        },
        {
          title: 'Name',
          dataIndex: 'name',
          align: 'center',
          width: '160px',
          ellipsis: true,
          scopedSlots: { customRender: 'name' }
        },
        {
          title: 'Passport No',
          dataIndex: 'passport_no',
          align: 'center',
          width: '160px',
          ellipsis: true,
          scopedSlots: { customRender: 'passport_no' }
        },
        {
          title: 'Travel Plan',
          align: 'center',
          children: [
            {
              title: 'Exit',
              dataIndex: 'exit',
              align: 'center',
              width: '160px',
              ellipsis: true,
              scopedSlots: { customRender: 'exit' }
            },
            {
              title: 'Entry',
              dataIndex: 'entry',
              align: 'center',
              width: '160px',
              ellipsis: true,
              scopedSlots: { customRender: 'entry' }
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
              width: '160px',
              ellipsis: true,
              scopedSlots: { customRender: 'ticket1' }
            },
            {
              title: 'Ticket2',
              dataIndex: 'ticket2',
              align: 'center',
              width: '160px',
              ellipsis: true,
              scopedSlots: { customRender: 'ticket2' }
            }
          ]
        },
        {
          title: 'Hotel',
          dataIndex: 'hotel',
          align: 'center',
          ellipsis: true,
          width: '160px',
          scopedSlots: { customRender: 'hotel' }
        },
        {
          title: 'Remark',
          dataIndex: 'remark',
          align: 'center',
          ellipsis: true,
          width: '160px',
          scopedSlots: { customRender: 'remark' }
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
          title: 'Action',
          width: '120px',
          scopedSlots: { customRender: 'action' },
          align: 'center'
        }
      ]
    }
  }
}
</script>
