<template>
  <form-validate ref="observer">
    <page-header-wrapper>
      <template slot="extra">
        <a-button v-action:change_group type="primary" @click="submit" :loading="updateing" html-type="submit">
          Submit
        </a-button>
      </template>
      <a-card class="card" title="Base Information" :bordered="false">
        <form-item-validate label="Name" vid="name">
          <a-input v-model="form.name" :disabled="!$auth('change_group')" />
        </form-item-validate>
      </a-card>

      <a-card class="card" title="Permissions" :bordered="false">
        <a-spin :spinning="updateing">
          <table border="1" cellpadding="15" bordercolor="gray" bgcolor="white" width="100%">
            <tbody v-for="(permission, index) in permissionData" :key="index" class="whitespace-no-wrap bg-gray-100">
              <tr>
                <td colspan="100" class="py-2 text-center">{{ index }}</td>
              </tr>
              <tr>
                <td v-for="data in permission" :key="data.id" class="py-4">
                  <a-checkbox v-model="data.check" @change="onClick(data)">{{ data.name }}</a-checkbox>
                </td>
              </tr>
            </tbody>
          </table>
        </a-spin>
      </a-card>
    </page-header-wrapper>
  </form-validate>
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import { getRole, updateRole } from '@/api/role'
import moment from 'moment'
import _ from 'lodash'

export default {
  components: { FormValidate, FormItemValidate },

  data() {
    return {
      loading: false,
      updateing: false,
      form: {},
      permission: [],
      permissionData: []
    }
  },
  mounted() {
    this.getRoleData()
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
    }
  }
}
</script>

<style lang="less" scoped>
.card {
  margin-bottom: 24px;
}
.popover-wrapper {
  /deep/ .antd-pro-pages-forms-style-errorPopover .ant-popover-inner-content {
    min-width: 256px;
    max-height: 290px;
    padding: 0;
    overflow: auto;
  }
}
.antd-pro-pages-forms-style-errorIcon {
  user-select: none;
  margin-right: 24px;
  color: #f5222d;
  cursor: pointer;
  i {
    margin-right: 4px;
  }
}
.antd-pro-pages-forms-style-errorListItem {
  padding: 8px 16px;
  list-style: none;
  border-bottom: 1px solid #e8e8e8;
  cursor: pointer;
  transition: all 0.3s;

  &:hover {
    background: #e6f7ff;
  }
  .antd-pro-pages-forms-style-errorIcon {
    float: left;
    margin-top: 4px;
    margin-right: 12px;
    padding-bottom: 22px;
    color: #f5222d;
  }
  .antd-pro-pages-forms-style-errorField {
    margin-top: 2px;
    color: rgba(0, 0, 0, 0.45);
    font-size: 12px;
  }
}

// table {
//   border-spacing: 0;
//   border-top: 1px solid #999999;
//   border-left: 1px solid #999999;
//   margin: 16px auto;
//   width: 100%;
// }

// th {
//   border-right: 1px solid #999999;
//   border-bottom: 1px solid #999999;
//   padding: 8px 0;
// }

// td {
//   border-right: 1px solid #999999;
//   border-bottom: 1px solid #999999;
//   padding: 8px 0;
// }

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
