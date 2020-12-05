<template>
  <form-validate ref="observer">
    <page-header-wrapper>
      <a-card class="card" title="Base Information" :bordered="false">
        <form-item-validate label="Name" vid="name" required>
          <a-input v-model="form.name" :disabled="disabled()" />
        </form-item-validate>
      </a-card>

      <a-card
        v-if="post_type == 'edit'"
        class="card"
        title="Permissions"
        :bordered="false"
        style="width:auto; overflow:auto;"
      >
        <a-spin :spinning="updateing">
          <table cellpadding="10" bordercolor="gray" bgcolor="white" border="1" width="auto">
            <tbody v-for="(permission, index) in permissionData" :key="index" class="whitespace-no-wrap bg-gray-100">
              <tr>
                <td colspan="10" class="py-4 ">
                  <span class="uppercase font-bold">{{ index }}</span>
                </td>
              </tr>
              <tr>
                <td v-for="data in permission" :key="data.id" class="py-4 ">
                  <a-checkbox v-model="data.check" :disabled="disabled()" @change="onClick(data)"
                    ><span class="">{{ data.name }}</span></a-checkbox
                  >
                </td>
              </tr>
            </tbody>
          </table>
        </a-spin>
      </a-card>
      <a-row v-if="post_type == 'edit'">
        <a-col :span="12">
          <a-popconfirm
            title="Are you sure cancel?"
            @confirm="onDelete"
            okText="Yes"
            cancelText="No"
            v-if="$auth('delete_group')"
          >
            <a-button href="javascript:;" type="danger">Delete</a-button>
          </a-popconfirm>
        </a-col>

        <a-col :span="12" class="text-right">
          <a-button v-action:change_group type="primary" @click="submit" :loading="updateing" html-type="submit">
            Submit
          </a-button>
        </a-col>
      </a-row>
      <a-row v-if="post_type == 'add'">
        <a-col :span="24" class="text-right">
          <a-button v-action:add_group type="primary" @click="submit" :loading="updateing" html-type="submit">
            Submit
          </a-button>
        </a-col>
      </a-row>
    </page-header-wrapper>
  </form-validate>
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import { getRole, updateRole, createRole, deleteRole } from '@/api/role'
import moment from 'moment'
import _ from 'lodash'

export default {
  components: { FormValidate, FormItemValidate },
  props: {
    post_type: {
      type: String,
      default: 'edit'
    }
  },
  data() {
    return {
      loading: false,
      updateing: false,
      disabled: () => {
        if (this.post_type == 'add' && this.$auth('add_group')) {
          return false
        }

        if (this.post_type == 'edit' && this.$auth('change_group')) {
          return false
        }

        return true
      },
      form: {},
      permission: [],
      permissionData: []
    }
  },
  mounted() {
    if (this.post_type == 'edit') this.getRoleData()
  },
  methods: {
    initRole(group, permission) {
      if (group) {
        var _inter = _.intersectionBy(group.permissions, permission, 'id')

        var _per = permission.map(f => {
          if (_inter.find(f1 => f.id === f1.id)) {
            return Object.assign(f, { check: true })
          }
          return Object.assign(f, { check: false })
        })

        this.permissionData = _per.reduce(function(pre, current) {
          current.name = current.name.replace('group', 'role')
          current.content_type.model = current.content_type.model.replace('group', 'role')

          pre[current.content_type.model] = pre[current.content_type.model] || []
          pre[current.content_type.model].push(current)
          return pre
        }, {})
      }
    },
    getRoleData() {
      this.loading = true
      getRole(this.$route.params.id)
        .then(res => {
          const { data, extra } = res.result
          this.form = Object.assign({}, data)
          this.permission = Object.assign([], extra.permission)

          this.initRole(this.form, this.permission)
        })
        .finally(() => {
          this.loading = false
        })
    },
    submit() {
      this.updateing = true
      var form = Object.assign({}, this.form, {})

      if (this.post_type == 'edit') {
        updateRole(this.$route.params.id, form)
          .then(res => {
            const { data, extra } = res.result

            this.extra = extra
          })
          .catch(error => {
            if (error.response) {
              this.$refs.observer.checkError(error)
            }
          })
          .finally(() => {
            this.updateing = false
          })
      } else if (this.post_type == 'add') {
        createRole(this.form)
          .then(res => {
            this.$router.replace({
              name: 'RoleDetail',
              params: { id: res.result.id }
            })
          })
          .catch(error => {
            if (error.response) {
              this.$refs.observer.setErrors(error)
            }
          })
          .finally(() => {
            this.updateing = false
          })
      }
    },
    updatePermission(permission) {
      this.updateing = true
      setTimeout(() => {
        updateRole(this.$route.params.id, {
          permission: permission.id
        })
          .then(res => {
            const { data, extra } = res.result
            this.form = Object.assign({}, data)
            this.permission = Object.assign([], extra.permission)

            this.initRole(this.form, this.permission)
          })
          .finally(() => {
            this.updateing = false
          })
      }, 0)
    },
    onClick(permission) {
      this.updatePermission(permission)
    },
    onDelete() {
      this.updateing = true
      deleteRole(this.$route.params.id)
        .then(() => {
          this.$router.go(-1)
        })
        .finally(() => {
          this.updateing = false
        })
    }
  }
}
</script>

<style lang="less" scoped>
.card {
  margin-bottom: 24px;
}

table {
  border-collapse: collapse; //collapse separate;
}

tr:nth-child(2n + 1) {
  background-color: #edf2f7;
}

tr:nth-child(2n) {
  background-color: white;
}

tr:hover {
  background-color: rgba(255, 254, 200, 0.77);
}
</style>
