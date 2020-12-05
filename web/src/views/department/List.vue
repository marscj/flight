<template>
  <page-header-wrapper>
    <template slot="extra">
      <a-button v-action:add_department type="primary" icon="plus" @click="openModal">Add</a-button>
    </template>
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
            <router-link v-action:view_department :to="{ name: 'DepartmentDetail', params: { id: data.id } }">
              <span>Detail</span>
            </router-link>
          </template>
        </template>
      </s-table>
    </a-card>

    <a-modal v-model="modal" title="Add Department" @ok="submit">
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
import { getDepartments, createDepartment } from '@/api/department'
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
        return getDepartments(Object.assign(parameter, Object.assign({}, this.queryParam, {}))).then(res => {
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
      createDepartment(this.form)
        .then(res => {
          this.modal = false
          this.$router.push({
            name: 'DepartmentDetail',
            params: { id: res.result.id }
          })
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
