<template>
  <div class="table-page-search-wrapper">
    <form-validate layout="inline" :form="queryParam">
      <a-row :gutter="24">
        <a-col :md="8" :sm="24">
          <form-item-validate label="ID">
            <a-input v-model="queryParam.id" @pressEnter="() => $refs.tableList.refresh()"></a-input>
          </form-item-validate>
        </a-col>

        <a-col :md="8" :sm="24">
          <form-item-validate label="Booking ID">
            <a-input v-model="queryParam.booking_id" @pressEnter="() => $refs.tableList.refresh()"></a-input>
          </form-item-validate>
        </a-col>

        <a-col :md="8" :sm="24">
          <form-item-validate label="Create">
            <a-range-picker v-model="date" @change="() => $refs.tableList.refresh()" />
          </form-item-validate>
        </a-col>

        <a-col :md="24" :sm="24">
          <form-item-validate>
            <a-input-search
              v-model="queryParam.search"
              placeholder="E.g Serial No. or Email or Name or Passport"
              enter-button="Search"
              @search="() => $refs.tableList.refresh()"
            />
          </form-item-validate>
        </a-col>
      </a-row>
    </form-validate>

    <s-table
      ref="tableList"
      size="default"
      :rowKey="record => record.id"
      :columns="columns"
      :data="loadData"
      showPagination="auto"
      :pageURI="true"
      :rowSelection="rowSelection"
      bordered
      :scroll="{ x: 1200 }"
    >
      <template slot="is_lock" slot-scope="data">
        <a-checkbox :checked="data" disabled />
      </template>

      <template slot="action" slot-scope="data" v-if="rowSelection == null">
        <router-link
          v-action:view_ticket
          v-if="data.booking_id"
          :to="{ name: 'BookingDetail', params: { id: data.booking_id } }"
        >
          <span>Booking</span>
        </router-link>
        <span v-else>Booking</span>
        <a-divider />
        <router-link
          v-action:view_ticket
          v-if="data.ticket"
          :to="{ name: 'TicketDetail', params: { id: data.ticket.id } }"
        >
          <span>Ticket</span>
        </router-link>
        <span v-else>Ticket</span>
      </template>
    </s-table>
  </div>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getItineraries } from '@/api/itinerary'
import { FormValidate, FormItemValidate } from '@/components'
import moment from 'moment'

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
  methods: {},
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
      ],
      loadData: parameter => {
        return getItineraries(
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
          const { data } = res.result
          this.$emit('onData', data.data)
          return data
        })
      }
    }
  }
}
</script>
