<template>
  <page-header-wrapper>
    <a-card>
      <div class="table-page-search-wrapper">
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
          <span v-for="index in data.join(',')" :key="index">{{ index }}</span>
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

      <a-modal v-model="modal" title="Create User" @ok="submit">
        <validation-observer ref="observer">
          <validation-provider name="non_field_errors" v-slot="{ errors }">
            <span class="errorText">{{ errors[0] }}</span>
          </validation-provider>

          <a-form :form="form" :submit="submit" :label-col="{ span: 6 }" :wrapper-col="{ span: 12 }">
            <a-form-item label="Phone Number">
              <validation-provider vid="phone_number" name="phone number" v-slot="{ errors }">
                <a-input v-model="form.phone_number">
                  <a-icon slot="prefix" type="mobile" :style="{ color: 'rgba(0,0,0,.25)' }" />
                  <a-select slot="addonBefore" defaultValue="+971" style="width:80px">
                    <a-select-option value="+971">+971</a-select-option>
                  </a-select>
                </a-input>
                <span class="errorText">{{ errors[0] }}</span>
              </validation-provider>
            </a-form-item>
          </a-form>
        </validation-observer>
      </a-modal>
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
          align: 'center'
        },
        {
          title: 'NAME',
          dataIndex: 'name',
          align: 'center'
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
          width: '80px',
          scopedSlots: { customRender: 'active' },
          align: 'center'
        },
        {
          title: 'ACTION',
          width: '80px',
          scopedSlots: { customRender: 'action' },

          align: 'center'
        }
      ],
      loadData: parameter => {
        return getUsers(Object.assign(parameter, this.queryParam)).then(res => {
          console.log(res)
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
