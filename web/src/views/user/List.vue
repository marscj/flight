<template>
  <page-header-wrapper>
    <a-card>
      <div class="table-page-search-wrapper">
        <form-validate layout="inline" :form="queryParam">
          <a-row :gutter="24">
            <a-col :md="6" :sm="24">
              <form-item-validate label="Role">
                <a-select v-model="queryParam.role" @change="() => $refs.table.refresh()">
                  <a-select-option :key="0" :value="0">All</a-select-option>
                  <a-select-option v-for="index in extra.role" :key="index.id" :value="index.id">
                    {{ index.name }}</a-select-option
                  >
                </a-select>
              </form-item-validate>
            </a-col>

            <a-col :md="6" :sm="24">
              <form-item-validate label="Department"> </form-item-validate>
            </a-col>

            <a-col :md="6" :sm="24">
              <form-item-validate label="Staff"> </form-item-validate>
            </a-col>

            <a-col :md="6" :sm="24">
              <form-item-validate label="Active"> </form-item-validate>
            </a-col>

            <a-col :md="20" :sm="24">
              <form-item-validate label="Search">
                <a-input v-model="queryParam.search"></a-input>
              </form-item-validate>
            </a-col>
            <a-col :md="4" :sm="24">
              <form-item-validate>
                <a-button type="primary" html-type="submit" icon="search" @click="() => $refs.table.refresh()">
                  Search
                </a-button>
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
        :pageURI="true"
        showPagination="auto"
        bordered
      >
        <div
          slot="filterDropdown"
          slot-scope="{ setSelectedKeys, selectedKeys, confirm, clearFilters, column }"
          style="padding: 8px"
        >
          <a-input
            v-ant-ref="c => (searchInput = c)"
            :placeholder="`Search ${column.dataIndex}`"
            :value="selectedKeys[0]"
            style="width: 188px; margin-bottom: 8px; display: block;"
            @change="e => setSelectedKeys(e.target.value ? [e.target.value] : [])"
            @pressEnter="() => handleSearch(selectedKeys, confirm, column.dataIndex)"
          />
          <a-button
            type="primary"
            icon="search"
            size="small"
            style="width: 90px; margin-right: 8px"
            @click="() => handleSearch(selectedKeys, confirm, column.dataIndex)"
          >
            Search
          </a-button>
          <a-button size="small" style="width: 90px" @click="() => handleReset(clearFilters)">
            Reset
          </a-button>
        </div>
        <a-icon
          slot="filterIcon"
          slot-scope="filtered"
          type="search"
          :style="{ color: filtered ? '#108ee9' : undefined }"
        />

        <template slot="roles" slot-scope="data">
          <div v-for="index in data" :key="index.id">
            <span>{{ index.name }}</span>
          </div>
        </template>

        <template slot="department" slot-scope="data">
          <span v-if="data">{{ data.name }}</span>
        </template>

        <template slot="active" slot-scope="data">
          <a-checkbox :checked="data" disabled />
        </template>

        <template slot="staff" slot-scope="data">
          <a-checkbox :checked="data" disabled />
        </template>

        <template slot="action" slot-scope="data">
          <template>
            <router-link :to="{ name: 'UserDetail', params: { id: data.id } }">
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
import { getUsers, createUser } from '@/api/user'
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
        role: 0
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
          align: 'center',
          sorter: true
        },
        {
          title: 'Email',
          dataIndex: 'email',
          align: 'center'
        },
        {
          title: 'Role',
          dataIndex: 'roles',
          scopedSlots: { filterDropdown: 'filterDropdown', filterIcon: 'filterIcon', customRender: 'roles' },
          align: 'center'
        },
        {
          title: 'Department',
          dataIndex: 'department',
          scopedSlots: { filterDropdown: 'filterDropdown', filterIcon: 'filterIcon', customRender: 'department' },
          align: 'center'
        },
        {
          title: 'Staff',
          dataIndex: 'is_staff',
          width: '80px',
          scopedSlots: { customRender: 'staff' },
          align: 'center'
        },
        {
          title: 'Active',
          dataIndex: 'is_active',
          width: '100px',
          scopedSlots: { customRender: 'active' },
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
        return getUsers(Object.assign(parameter, this.queryParam)).then(res => {
          this.extra = res.result.extra
          return res.result
        })
      }
    }
  },
  methods: {}
}
</script>

<style></style>
