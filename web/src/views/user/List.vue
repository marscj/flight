<template>
  <page-header-wrapper>
    <a-card>
      <!-- <div class="table-page-search-wrapper">
        <a-form layout="inline">
          <a-row :gutter="48">
            <a-col :md="8" :sm="24">
              <a-form-item label="Search">
                <a-input v-model="queryParam.search"></a-input>
              </a-form-item>
            </a-col>
            <a-col :md="8" :sm="24">
              <a-form-item>
                <a-button type="primary" html-type="submit" icon="search" @click="() => $refs.table.refresh()">
                  Search
                </a-button>
              </a-form-item>
            </a-col>
          </a-row>
        </a-form>
      </div> -->

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
          <span>{{ data.join(',') }}</span>
        </template>

        <template slot="active" slot-scope="data">
          <a-checkbox :checked="data" disabled />
        </template>

        <template slot="admin" slot-scope="data">
          <a-checkbox :checked="data" disabled />
        </template>

        <template slot="action" slot-scope="data">
          <template>
            <router-link :to="{ name: 'User', params: { id: data.id } }">
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

export default {
  components: {
    STable
  },
  data() {
    return {
      queryParam: {
        role: null
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
          title: 'NAME',
          dataIndex: 'name',
          align: 'center',
          sorter: true
        },
        {
          title: 'EMAIL',
          dataIndex: 'email',
          align: 'center'
        },
        {
          title: 'ROLE',
          dataIndex: 'roles',
          scopedSlots: { filterDropdown: 'filterDropdown', filterIcon: 'filterIcon', customRender: 'roles' },
          align: 'center'
        },
        {
          title: 'ADMIN',
          dataIndex: 'is_superuser',
          width: '80px',
          scopedSlots: { customRender: 'admin' },
          align: 'center'
        },
        {
          title: 'ACTIVE',
          dataIndex: 'is_active',
          width: '100px',
          scopedSlots: { customRender: 'active' },
          align: 'center'
        },
        {
          title: 'ACTION',
          width: '100px',
          scopedSlots: { customRender: 'action' },
          align: 'center'
        }
      ],
      loadData: parameter => {
        return getUsers(Object.assign(parameter, this.queryParam)).then(res => {
          return res.result
        })
      },
      modal: false,
      form: {}
    }
  },
  methods: {
    openModal() {
      this.modal = true
      this.form = {}
    },
    submit() {
      createUser({
        username: '+971' + this.form.phone_number,
        phone_number: '+971' + this.form.phone_number
      })
        .then(res => {
          this.modal = false
          this.$refs.table.refresh()
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result)
          }
        })
    }
  }
}
</script>
