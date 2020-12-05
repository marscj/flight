<template>
  <page-header-wrapper>
    <form-validate ref="observer">
      <a-card :loading="loading">
        <form-item-validate label="Photo" required>
          <a-upload
            name="Photo"
            :multiple="false"
            :fileList="fileList"
            :beforeUpload="beforeUpload"
            :disabled="fileList.length > 0"
            :remove="handleRemove"
            listType="text"
          >
            <div v-if="fileList.length == 0">
              <img v-if="form && form.photo && form.photo.thumbnail" alt="images" :src="form.photo.thumbnail" />

              <div v-else>
                <a-button v-if="fileList.length == 0"> <a-icon type="upload" /> Select File </a-button>
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
    </form-validate>
  </page-header-wrapper>
</template>

<script>
import { getUser, updateUser } from '@/api/user'
import FormValidate from '@/components/FormValidate'
import FormItemValidate from '@/components/FormItemValidate'

export default {
  components: {
    FormValidate,
    FormItemValidate
  },
  data() {
    return {
      loading: false,
      updateing: false,
      form: {},
      extra: {},
      fileList: []
    }
  },
  mounted() {
    this.getUserData()
  },
  computed: {
    photo() {
      return this.fileList[0]
    }
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
      const isIMG = file.type === 'image/jpeg' || file.type === 'image/png'
      if (!isIMG) {
        this.$message.error('You can only upload JPG or PNG file!')
      }

      const isLt2M = file.size / 1024 / 1024 < 2
      if (!isLt2M) {
        this.$message.error('Image must smaller than 2MB!')
      }

      if (isIMG && isLt2M) {
        this.fileList = [...this.fileList, file]
      }
      return false
    },
    handleRemove(file) {
      const index = this.fileList.indexOf(file)
      const newFileList = this.fileList.slice()
      newFileList.splice(index, 1)
      this.fileList = newFileList
    },
    submit() {
      this.updateing = true
      const formData = new FormData()

      if (this.photo) {
        formData.append('photo', this.photo)
      }

      formData.append('username', this.form.username)
      formData.append('phone_number', this.form.phone_number)
      formData.append('first_name', this.form.first_name)
      formData.append('last_name', this.form.last_name)
      formData.append('role', this.form.role)
      formData.append('is_active', this.form.is_active)
      formData.append('is_superuser', this.form.is_superuser)

      updateUser(this.$route.params.id, formData)
        .then(res => {
          this.getUserData()
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
