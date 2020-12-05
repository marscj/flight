<template>
  <page-header-wrapper>
    <form-validate ref="observer">
      <template v-if="post_type == 'edit'">
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
                  <a-icon
                    v-action:reset_password
                    slot="addonAfter"
                    type="lock"
                    @click="
                      () => {
                        $refs.modal.setVisible(true)
                      }
                    "
                  />
                </a-input>
              </form-item-validate>
            </a-col>

            <a-col :lg="12" :md="12" :sm="24">
              <form-item-validate label="First Name" vid="first_name">
                <a-input v-model="form.first_name" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="12" :md="12" :sm="24">
              <form-item-validate label="Last Name" vid="last_name">
                <a-input v-model="form.last_name" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="12" :md="12" :sm="24">
              <form-item-validate label="Department" vid="department_id">
                <a-select
                  v-model="form.department_id"
                  :allowClear="true"
                  @change="onDepartmentChange"
                  :disabled="!$auth('change_user')"
                >
                  <a-select-option v-for="index in extra.department" :key="index.id" :value="index.id">{{
                    index.name
                  }}</a-select-option>
                </a-select>
              </form-item-validate>
            </a-col>

            <a-col :lg="12" :md="12" :sm="24">
              <form-item-validate label="Role" vid="role_id">
                <a-select
                  v-model="form.groups_id"
                  :allowClear="true"
                  @change="onRoleChange"
                  mode="multiple"
                  :disabled="!$auth('assign_role')"
                >
                  <a-select-option v-for="index in extra.role" :key="index.id" :value="index.id">{{
                    index.name
                  }}</a-select-option>
                </a-select>
              </form-item-validate>
            </a-col>

            <a-col :lg="12" :md="12" :sm="24">
              <form-item-validate label="Active" vid="is_active" help="Whether the account is available">
                <a-checkbox v-model="form.is_active" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="12" :md="12" :sm="24">
              <form-item-validate label="Staff" vid="is_staff" help="Used to log in to the back-end website">
                <a-checkbox v-model="form.is_staff" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>
          </a-row>
        </a-card>

        <a-card class="card" title="Passport" :bordered="false">
          <a-row class="form-row" :gutter="16">
            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="Type" vid="possport_type">
                <a-input v-model="form.possport_type" :maxLength="4" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="Code" vid="passport_code">
                <a-input v-model="form.passport_code" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="No." vid="passport_no">
                <a-input v-model="form.passport_no" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="Sex" vid="passport_sex">
                <a-input v-model="form.passport_sex" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="Nationality" vid="passport_nationality">
                <a-input v-model="form.passport_nationality" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="Date of birth" vid="passport_date_birth">
                <a-date-picker v-model="form.passport_date_birth" class="w-full" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="Date of issue" vid="passport_date_issue">
                <a-date-picker v-model="form.passport_date_issue" class="w-full" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="Date of expiry" vid="passport_date_expiry">
                <a-date-picker v-model="form.passport_date_expiry" class="w-full" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="Place of birth" vid="passport_place_birth">
                <a-input v-model="form.passport_place_birth" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>

            <a-col :lg="6" :md="12" :sm="24">
              <form-item-validate label="Issuing authority" vid="passport_issuing_authority">
                <a-input v-model="form.passport_issuing_authority" :disabled="!$auth('change_user')" />
              </form-item-validate>
            </a-col>
          </a-row>
        </a-card>
        <a-row>
          <a-col :span="12">
            <a-popconfirm
              title="Are you sure cancel?"
              @confirm="onDelete"
              okText="Yes"
              cancelText="No"
              v-if="$auth('delete_user')"
            >
              <a-button href="javascript:;" type="danger">Delete</a-button>
            </a-popconfirm>
          </a-col>

          <a-col :span="12" class="text-right">
            <a-button v-action:change_user type="primary" @click="submit" :loading="updateing" html-type="submit">
              Submit
            </a-button>
          </a-col>
        </a-row>
      </template>
      <template v-if="post_type == 'add'">
        <a-card class="card" title="Authorization" :bordered="false">
          <form-item-validate label="Email" vid="email">
            <a-input v-model="form.email" />
          </form-item-validate>

          <form-item-validate label="Password" vid="password1">
            <a-input-password v-model="form.password1" placeholder="Password"> </a-input-password>
          </form-item-validate>

          <form-item-validate label="Password" vid="password2">
            <a-input-password v-model="form.password2" placeholder="Repeat password"> </a-input-password>
          </form-item-validate>
        </a-card>
        <a-row>
          <a-col :span="24" class="text-right">
            <a-button v-action:add_user type="primary" @click="submit" :loading="updateing" html-type="submit">
              Submit
            </a-button>
          </a-col>
        </a-row>
      </template>
    </form-validate>
    <reset-password ref="modal" title="Rest Password" />
  </page-header-wrapper>
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import { getUser, updateUser, deleteUser, createUser } from '@/api/user'
import ResetPassword from './ResetPassword'
import moment from 'moment'

export default {
  components: { FormValidate, FormItemValidate, ResetPassword },
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
      form: {
        passport_date_birth: null,
        passport_date_issue: null,
        passport_date_expiry: null
      },
      extra: {}
    }
  },
  mounted() {
    if (this.post_type == 'edit') {
      this.getUserData()
    }
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
      if (this.post_type == 'edit') {
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
              this.$refs.observer.setErrors(error)
            }
          })
          .finally(() => {
            this.updateing = false
          })
      } else if (this.post_type == 'add') {
        createUser({
          email: this.form.email,
          password1: this.form.password1,
          password2: this.form.password2
        })
          .then(res => {
            this.$router.replace({
              name: 'UserDetail',
              params: { id: res.result.user.id }
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
    onDelete() {
      this.updateing = true
      deleteUser(this.$route.params.id)
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
</style>
