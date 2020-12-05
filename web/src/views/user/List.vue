<template>
  <page-header-wrapper>
    <template slot="extra">
      <a-button v-action:add_user type="primary" icon="plus" @click="openModal">Add</a-button>
    </template>
    <a-card>
      <div class="table-page-search-wrapper">
        <form-validate layout="inline" :form="queryParam">
          <a-row :gutter="24">
            <a-col :md="6" :sm="24">
              <form-item-validate label="Role">
                <a-select v-model="queryParam.role" @change="() => $refs.table.refresh()">
                  <a-select-option key="0" :value="0">All</a-select-option>
                  <a-select-option v-for="index in extra.role" :key="index.id" :value="index.id">
                    {{ index.name }}</a-select-option
                  >
                </a-select>
              </form-item-validate>
            </a-col>

            <a-col :md="6" :sm="24">
              <form-item-validate label="Department">
                <a-select v-model="queryParam.department" @change="() => $refs.table.refresh()">
                  <a-select-option key="0" :value="0">All</a-select-option>
                  <a-select-option v-for="index in extra.department" :key="index.id" :value="index.id">
                    {{ index.name }}</a-select-option
                  >
                </a-select>
              </form-item-validate>
            </a-col>

            <a-col :md="6" :sm="24">
              <form-item-validate label="Staff">
                <a-select v-model="queryParam.is_staff" @change="() => $refs.table.refresh()">
                  <a-select-option key="0" :value="0">All</a-select-option>
                  <a-select-option key="1" :value="1">Yes</a-select-option>
                  <a-select-option key="2" :value="2">No</a-select-option>
                </a-select>
              </form-item-validate>
            </a-col>

            <a-col :md="6" :sm="24">
              <form-item-validate label="Active">
                <a-select v-model="queryParam.is_active" @change="() => $refs.table.refresh()">
                  <a-select-option key="0" :value="0">All</a-select-option>
                  <a-select-option key="1" :value="1">Yes</a-select-option>
                  <a-select-option key="2" :value="2">No</a-select-option>
                </a-select>
              </form-item-validate>
            </a-col>

            <a-col :md="24" :sm="24">
              <form-item-validate>
                <a-input-search
                  v-model="queryParam.search"
                  placeholder="E.g Name, Email, Passport No."
                  enter-button="Search"
                  @search="() => $refs.table.refresh()"
                />
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
      modal: false,
      form: {},
      queryParam: {
        role: 0,
        department: 0,
        is_staff: 0,
        is_active: 0
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
          title: 'Email',
          dataIndex: 'email',
          align: 'center',
          sorter: true
        },
        {
          title: 'Name',
          dataIndex: 'name',
          align: 'center'
        },
        {
          title: 'Role',
          dataIndex: 'roles',
          scopedSlots: { customRender: 'roles' },
          align: 'center'
        },
        {
          title: 'Department',
          dataIndex: 'department',
          scopedSlots: { customRender: 'department' },
          align: 'center'
        },
        {
          title: 'Staff',
          dataIndex: 'is_staff',
          width: '100px',
          scopedSlots: { customRender: 'staff' },
          align: 'center',
          sorter: true
        },
        {
          title: 'Active',
          dataIndex: 'is_active',
          width: '100px',
          scopedSlots: { customRender: 'active' },
          align: 'center',
          sorter: true
        },
        {
          title: 'Action',
          width: '100px',
          scopedSlots: { customRender: 'action' },
          align: 'center'
        }
      ],
      loadData: parameter => {
        return getUsers(
          Object.assign(
            parameter,
            Object.assign({}, this.queryParam, {
              role: this.queryParam.role != 0 ? this.queryParam.role : null,
              department: this.queryParam.department != 0 ? this.queryParam.department : null,
              is_staff: this.queryParam.is_staff != 0 ? (this.queryParam.is_staff == 1 ? true : false) : null,
              is_active: this.queryParam.is_active != 0 ? (this.queryParam.is_active == 1 ? true : false) : null
            })
          )
        ).then(res => {
          this.extra = res.result.extra
          return res.result
        })
      }
    }
  },
  methods: {
    openModal() {
      this.modal = true
      this.form = {}
    },
    submit() {
      createUser(this.form)
        .then(res => {
          this.modal = false
          this.$refs.table.refresh()
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error)
          }
        })
    }
  }
}
</script>

<style></style>
