<template>
  <form-validate ref="observer">
    <page-header-wrapper>
      <template slot="extra">
        <a-button v-action:change_user type="primary" @click="submit" :loading="updateing" html-type="submit">
          Submit
        </a-button>
      </template>
      <a-card class="card" title="Base Information" :bordered="false">
        <a-row class="form-row" :gutter="16">
          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Email" vid="Email">
              <a-input v-model="form.email" disabled />
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Password" vid="password">
              <a-input v-model="form.password" disabled>
                <a-icon slot="addonAfter" type="lock" />
              </a-input>
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="First Name" vid="first_name">
              <a-input v-model="form.first_name" />
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Last Name" vid="last_name">
              <a-input v-model="form.last_name" />
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Department" vid="department_id">
              <a-select v-model="form.department_id" :allowClear="true" @change="onDepartmentChange">
                <a-select-option v-for="index in extra.department" :key="index.id" :value="index.id">{{
                  index.name
                }}</a-select-option>
              </a-select>
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Role" vid="role_id">
              <a-select v-model="form.groups_id" :allowClear="true" @change="onRoleChange" mode="multiple">
                <a-select-option v-for="index in extra.role" :key="index.id" :value="index.id">{{
                  index.name
                }}</a-select-option>
              </a-select>
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Active" vid="is_active" help="Whether the account is available">
              <a-checkbox v-model="form.is_active" />
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Staff" vid="is_staff" help="Used to log in to the back-end website">
              <a-checkbox v-model="form.is_staff" />
            </form-item-validate>
          </a-col>
        </a-row>
      </a-card>

      <a-card class="card" title="Passport" :bordered="false">
        <a-row class="form-row" :gutter="16">
          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="Type" vid="possport_type">
              <a-input v-model="form.possport_type" :maxLength="4" />
            </form-item-validate>
          </a-col>

          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="Code" vid="passport_code">
              <a-input v-model="form.passport_code" />
            </form-item-validate>
          </a-col>

          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="No." vid="passport_no">
              <a-input v-model="form.passport_no" />
            </form-item-validate>
          </a-col>

          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="Sex" vid="passport_sex">
              <a-input v-model="form.passport_sex" />
            </form-item-validate>
          </a-col>

          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="Nationality" vid="passport_nationality">
              <a-input v-model="form.passport_nationality" />
            </form-item-validate>
          </a-col>

          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="Date of birth" vid="passport_date_birth">
              <a-date-picker v-model="form.passport_date_birth" class="w-full" />
            </form-item-validate>
          </a-col>

          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="Date of issue" vid="passport_date_issue">
              <a-date-picker v-model="form.passport_date_issue" class="w-full" />
            </form-item-validate>
          </a-col>

          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="Date of expiry" vid="passport_date_expiry">
              <a-date-picker v-model="form.passport_date_expiry" class="w-full" />
            </form-item-validate>
          </a-col>

          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="Place of birth" vid="passport_place_birth">
              <a-input v-model="form.passport_place_birth" />
            </form-item-validate>
          </a-col>

          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="Issuing authority" vid="passport_issuing_authority">
              <a-input v-model="form.passport_issuing_authority" />
            </form-item-validate>
          </a-col>
        </a-row>
      </a-card>
    </page-header-wrapper>
  </form-validate>
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import { getUser, updateUser } from '@/api/user'
import moment from 'moment'

export default {
  components: { FormValidate, FormItemValidate },

  data() {
    return {
      loading: false,
      updateing: false,
      form: {
        passport_date_birth: null,
        passport_date_issue: null,
        passport_date_expiry: null
      },
      extra: {}
    }
  },
  mounted() {
    this.getUserData()
  },
  methods: {
    onDepartmentChange(val) {
      if (val) {
        this.form.department_id = val
      } else {
        this.form.department_id = null
      }
    },
    onRoleChange(val) {
      if (val) {
        this.form.groups_id = val
      } else {
        this.form.groups_id = null
      }
    },
    getUserData() {
      this.loading = true
      getUser(this.$route.params.id)
        .then(res => {
          const { data, extra } = res.result

          this.form = Object.assign(data, {
            passport_date_birth:
              data.passport_date_birth != null ? moment(data.passport_date_birth, 'YYYY-MM-DD') : null,
            passport_date_issue:
              data.passport_date_issue != null ? moment(data.passport_date_issue, 'YYYY-MM-DD') : null,
            passport_date_expiry:
              data.passport_date_expiry != null ? moment(data.passport_date_expiry, 'YYYY-MM-DD') : null
          })

          this.extra = Object.assign({}, extra)
        })
        .finally(() => {
          this.loading = false
        })
    },
    submit() {
      this.updateing = true
      var form = Object.assign({}, this.form, {
        passport_date_birth:
          this.form.passport_date_birth != null ? moment(this.form.passport_date_birth).format('YYYY-MM-DD') : null,
        passport_date_issue:
          this.form.passport_date_issue != null ? moment(this.form.passport_date_issue).format('YYYY-MM-DD') : null,
        passport_date_expiry:
          this.form.passport_date_expiry != null ? moment(this.form.passport_date_expiry).format('YYYY-MM-DD') : null
      })
      updateUser(this.$route.params.id, form)
        .then(res => {
          const { data, extra } = res.result
          this.form = Object.assign({}, data, {
            passport_date_birth:
              data.passport_date_birth != null ? moment(data.passport_date_birth, 'YYYY-MM-DD') : null,
            passport_date_issue:
              data.passport_date_issue != null ? moment(data.passport_date_issue, 'YYYY-MM-DD') : null,
            passport_date_expiry:
              data.passport_date_expiry != null ? moment(data.passport_date_expiry, 'YYYY-MM-DD') : null
          })
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
</style>
