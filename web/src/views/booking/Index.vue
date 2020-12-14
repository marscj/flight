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

        <a-upload-dragger
          v-if="post_type == 'edit' && form.uploads"
          :multiple="true"
          :before-upload="beforeUpload"
          :remove="handleRemove"
          action="http://ubangservice.com/api/uploads/"
          :withCredentials="true"
          :default-file-list="form.uploads"
          :data="{
            content_type: 'booking',
            object_id: $route.params.id
          }"
          :disabled="disabled()"
        >
          <p class="ant-upload-drag-icon">
            <a-icon type="inbox" />
          </p>
          <p class="ant-upload-text">
            Click or drag file to this area to upload
          </p>
          <p class="ant-upload-hint">
            Support for a single or bulk upload
          </p>
        </a-upload-dragger>
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
      }
      return isLt2M
    },
    handleRemove(file) {
      if (file != null && file.id != null) {
        deleteFile(file.id)
      }
    }
  }
}
</script>

<style lang="less" scoped>
.card {
  margin-bottom: 24px;
}
</style>
