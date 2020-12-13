<template>
  <form-validate ref="observer">
    <page-header-wrapper :content="'ID:' + $route.params.id">
      <a-card class="card" title="Base Information" :bordered="false">
        <form-item-validate label="Title" vid="title" required>
          <a-input v-model="form.title" :maxLength="64" :disabled="disabled()" />
        </form-item-validate>
        <form-item-validate label="Remark" vid="remark">
          <a-textarea v-model="form.remark" :maxLength="1024" :rows="5" :disabled="disabled()" />
        </form-item-validate>

        <a-upload
          v-if="post_type == 'edit'"
          :multiple="true"
          :before-upload="beforeUpload"
          action="http://127.0.0.1:8000/api/uploads/"
          :data="{ object_id: 3, content_type: 'booking' }"
          :headers="headers"
        >
          <a-button> <a-icon type="upload" /> Upload </a-button>
        </a-upload>
      </a-card>

      <itinerary-list v-if="post_type == 'edit'" />
    </page-header-wrapper>

    <a-row v-if="post_type == 'edit'">
      <a-col :span="12">
        <a-popconfirm
          title="Are you sure delete?"
          @confirm="onDelete"
          okText="Yes"
          cancelText="No"
          v-if="$auth('delete_booking')"
        >
          <a-button href="javascript:;" type="danger">Delete</a-button>
        </a-popconfirm>
      </a-col>

      <a-col :span="12" class="text-right">
        <a-button
          v-if="post_type == 'edit'"
          v-action:change_booking
          type="primary"
          @click="submit"
          :loading="updateing"
          html-type="submit"
        >
          Submit
        </a-button>
      </a-col>
    </a-row>
    <a-row>
      <a-col :span="24" class="text-right">
        <a-button
          v-if="post_type == 'add'"
          v-action:add_booking
          type="primary"
          @click="submit"
          :loading="updateing"
          html-type="submit"
        >
          Submit
        </a-button>
      </a-col>
    </a-row>
  </form-validate>
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import ItineraryList from '@/views/itinerary/ActionList'
import { getBooking, updateBooking, createBooking, deleteBooking } from '@/api/booking'
import { uploadFile, deleteFile } from '@/api/upload'
import moment from 'moment'

export default {
  components: { FormValidate, FormItemValidate, ItineraryList },
  props: {
    post_type: {
      type: String,
      default: 'edit'
    }
  },
  data() {
    return {
      headers: {
        authorization: 'authorization-text'
      },
      fileList: [],
      loading: false,
      updateing: false,
      disabled: () => {
        if (this.post_type == 'add' && this.$auth('add_booking')) {
          return false
        }

        if (this.post_type == 'edit' && this.$auth('change_booking')) {
          return false
        }

        return true
      },
      form: {},
      content: ''
    }
  },
  mounted() {
    if (this.$route.params.id) {
      this.getBookingData()
    }
  },
  methods: {
    getBookingData() {
      this.loading = true
      getBooking(this.$route.params.id)
        .then(res => {
          const { data } = res.result
          this.form = Object.assign({}, data)
          this.fileList = Object.assign([], data.uploads)
        })
        .finally(() => {
          this.loading = false
        })
    },
    submit() {
      this.updateing = true
      var form = Object.assign({}, this.form, {})

      if (this.post_type == 'edit') {
        updateBooking(this.$route.params.id, form)
          .then(res => {
            const { data, extra } = res.result
            this.form = Object.assign({}, data)
            this.fileList = Object.assign([], data.uploads)
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
        createBooking(form)
          .then(res => {
            this.$router.replace({
              name: 'BookingDetail',
              params: { id: res.result.data.id }
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
      deleteBooking(this.$route.params.id)
        .then(() => {
          this.$router.go(-1)
        })
        .finally(() => {
          this.updateing = false
        })
    },
    beforeUpload(file) {
      const isLt2M = file.size / 1024 / 1024 < 2
      if (!isLt2M) {
        this.$message.error('Image must smaller than 2MB!')
      } else {
        // this.fileList = [...this.fileList, file]
      }
      return isLt2M
    },
    handleRemove(file) {
      const index = this.fileList.indexOf(file)
      const newFileList = this.fileList.slice()
      newFileList.splice(index, 1)
      this.fileList = newFileList
    },
    customRequest(request) {
      const formData = new FormData()
      formData.append('url', request.file)
      formData.append('content_type', 'booking')
      formData.append('object_id', this.$route.params.id)
      uploadFile(formData).then(res => {
        this.fileList = [...this.fileList, request.file]
      })
    },
    handleChange({ fileList }) {}
  }
}
</script>

<style lang="less" scoped>
.card {
  margin-bottom: 24px;
}
</style>
