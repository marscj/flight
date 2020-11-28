<template>
  <page-header-wrapper>
    <template slot="extra">
      <a-button v-action:add_group type="primary" icon="plus" @click="openModal">New</a-button>
    </template>
    <a-card>
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
        <template slot="action" slot-scope="data">
          <template>
            <router-link :to="{ name: 'RoleDetail', params: { id: data.id } }">
              <span>Detail</span>
            </router-link>
          </template>
        </template>
      </s-table>
    </a-card>

    <a-modal v-model="modal" title="Add Role" @ok="submit">
      <form-validate :form="form" :submit="submit" :label-col="{ span: 6 }" :wrapper-col="{ span: 12 }" ref="observer">
        <form-item-validate label="Name" vid="name">
          <a-input v-model="form.name" :maxLength="150"></a-input>
        </form-item-validate>
      </form-validate>
    </a-modal>
  </page-header-wrapper>
</template>

<script>
import { STable, Ellipsis } from '@/components'
import { getRoles, createRole } from '@/api/role'
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
  },
  methods: {
    openModal() {
      this.modal = true
      this.form = {}
    },
    submit() {
      createRole(this.form)
        .then(res => {
          this.modal = false
          this.$refs.table.refresh()
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.checkError(error)
          }
        })
    }
  }
}
</script>

<style></style>
