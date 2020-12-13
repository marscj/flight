<template>
  <page-header-wrapper>
    <form-validate ref="observer" :form="form">
      <a-card class="card" :loading="loading" :bordered="false">
        <form-item-validate label="Photo">
          <a-upload
            name="avatar"
            list-type="picture"
            class="avatar-uploader"
            :show-upload-list="false"
            :before-upload="beforeUpload"
            :custom-request="customRequest"
          >
            <a-avatar
              v-if="form && form.avatar && form.avatar.medium"
              :src="form.avatar.medium"
              :size="128"
              alt="avatar"
            />
            <div v-else>
              <a-icon :type="loading ? 'loading' : 'plus'" />
              <div class="ant-upload-text">
                Upload
              </div>
            </div>
          </a-upload>
        </form-item-validate>

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
              <a-select v-model="form.department_id" disabled>
                <a-select-option v-for="index in extra.department" :key="index.id" :value="index.id">{{
                  index.name
                }}</a-select-option>
              </a-select>
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Role" vid="role_id">
              <a-select v-model="form.groups_id" mode="multiple" disabled>
                <a-select-option v-for="index in extra.role" :key="index.id" :value="index.id">{{
                  index.name
                }}</a-select-option>
              </a-select>
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Active" vid="is_active" help="Whether the account is available">
              <a-checkbox v-model="form.is_active" disabled />
            </form-item-validate>
          </a-col>

          <a-col :lg="12" :md="12" :sm="24">
            <form-item-validate label="Staff" vid="is_staff" help="Used to log in to the back-end website">
              <a-checkbox v-model="form.is_staff" disabled />
            </form-item-validate>
          </a-col>
        </a-row>
      </a-card>
      <a-row>
        <a-col :span="24" class="text-right">
          <a-button type="primary" @click="submit" :loading="loading" html-type="submit">
            Submit
          </a-button>
        </a-col>
      </a-row>
    </form-validate>
    <change-password ref="modal" title="Rest Password" />
  </page-header-wrapper>
</template>

<script>
import { getUser, updateUser } from '@/api/user'
import FormValidate from '@/components/FormValidate'
import FormItemValidate from '@/components/FormItemValidate'
import ChangePassword from './ChangePassword'

function getBase64(img, callback) {
  const reader = new FileReader()
  reader.addEventListener('load', () => callback(reader.result))
  reader.readAsDataURL(img)
}

export default {
  components: {
    FormValidate,
    FormItemValidate,
    ChangePassword
  },
  data() {
    return {
      loading: false,
      updateing: false,
      uploading: false,
      form: {},
      extra: {},
      fileList: []
    }
  },
  mounted() {
    this.getUserData()
  },
  methods: {
    getUserData() {
      this.loading = true
      getUser(this.$store.getters.user.info.id)
        .then(res => {
          const { data, extra } = res.result
          this.form = Object.assign({}, data)
          this.extra = Object.assign({}, extra)
          this.fileList = []
        })
        .finally(() => {
          this.loading = false
        })
    },
    beforeUpload(file) {
      const isJpgOrPng = file.type === 'image/jpeg' || file.type === 'image/png'
      if (!isJpgOrPng) {
        this.$message.error('You can only upload JPG file!')
      }
      const isLt2M = file.size / 1024 / 1024 < 2
      if (!isLt2M) {
        this.$message.error('Image must smaller than 2MB!')
      }
      return isJpgOrPng && isLt2M
    },
    customRequest(request) {
      this.loading = true
      const formData = new FormData()
      formData.append('avatar', request.file)

      updateUser(this.$store.getters.user.info.id, formData)
        .then(res => {
          const { data, extra } = res.result
          this.form = Object.assign({}, data)
          this.extra = Object.assign({}, extra)
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result)
          }
        })
        .finally(() => {
          this.loading = false
        })
    },
    submit() {
      this.updateing = true
      var form = {
        first_name: this.form.first_name,
        last_name: this.form.last_name
      }
      updateUser(this.$store.getters.user.info.id, form)
        .then(res => {
          const { data, extra } = res.result
          this.form = Object.assign({}, data)
          this.extra = Object.assign({}, extra)
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result)
          }
        })
        .finally(() => {
          this.updateing = false
        })
    }
  }
}
</script>

<style>
.card {
  margin-bottom: 24px;
}

.avatar-uploader > .ant-upload {
  width: 128px;
  height: 128px;
}
.ant-upload-select-picture-card i {
  font-size: 32px;
  color: #999;
}

.ant-upload-select-picture-card .ant-upload-text {
  margin-top: 8px;
  color: #666;
}
</style>
