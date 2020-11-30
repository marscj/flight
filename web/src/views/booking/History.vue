<template>
  <page-header-wrapper>
    <template slot="extra">
      <a-button type="primary">
        Back
      </a-button>
    </template>
    <a-card>
      <a-table
        ref="table"
        size="default"
        :rowKey="record => record.history_id"
        :columns="columns"
        :data-source="data"
        showPagination="auto"
        :pageURI="true"
        bordered
      >
      </a-table>
    </a-card>
  </page-header-wrapper>
</template>

<script>
import { STable, Ellipsis } from '@/components'
export default {
  components: {
    STable
  },
  props: {
    data: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      columns: [
        {
          title: 'ID',
          dataIndex: 'history_id',
          align: 'center',
          width: '80px',
          sorter: true
        }
      ]
    }
  }
}
</script>

<style></style>
