<template>
  <page-header-wrapper>
    <a-card>
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
            <router-link v-action:view_group :to="{ name: 'RoleDetail', params: { id: data.id } }">
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
import { getRoles } from '@/api/role'
import { FormValidate, FormItemValidate } from '@/components'

export default {
  components: {
    STable,
    FormValidate,
    FormItemValidate
  },
  data() {
    return {
      extra: {},
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
          title: 'Name',
          dataIndex: 'name',
          align: 'center'
        },

        {
          title: 'Action',
          width: '100px',
          scopedSlots: { customRender: 'action' },
          align: 'center'
        }
      ],
      loadData: parameter => {
        return getRoles(Object.assign(parameter, Object.assign({}, this.queryParam, {}))).then(res => {
          return res.result
        })
      }
    }
  }
}
</script>
