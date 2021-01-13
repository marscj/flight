<template>
  <form-validate ref="observer" :form="form">
    <page-header-wrapper :content="'ID:' + $route.params.id">
      <a-card v-if="post_type == 'edit'" class="card" title="Progress" :bordered="false">
        <a-steps v-if="!form.is_cancel" direction="horizontal" :current="current" progressDot>
          <a-step>
            <template v-slot:title>
              <span>Create Ticket</span>
            </template>
            <template v-slot:description>
              <div class="antd-pro-pages-profile-advanced-style-stepDescription">
                {{ form.author }}
                <div>{{ form.date }}</div>
              </div>
            </template>
          </a-step>
          <a-step title="Booked" />
          <a-step title="Confirmed" />
          <a-step title="Completed" />
        </a-steps>
        <a-steps v-else :direction="(isMobile && 'vertical') || 'horizontal'" :current="1" progressDot>
          <a-step>
            <template v-slot:title>
              <span>Create Ticket</span>
            </template>
            <template v-slot:description>
              <div class="antd-pro-pages-profile-advanced-style-stepDescription">
                {{ form.author }}
                <div>{{ form.date }}</div>
              </div>
            </template>
          </a-step>
          <a-step title="Cancelled" />
        </a-steps>
      </a-card>
      <a-card class="card" title="Ticket Info" :bordered="false">
        <a-row class="form-row" :gutter="16">
          <a-col :sm="24" :md="8">
            <form-item-validate label="Serial No." vid="serial_no">
              <a-input v-model="form.serial_no" :disabled="disabled()"></a-input>
            </form-item-validate>
          </a-col>
          <a-col :sm="24" :md="8">
            <form-item-validate label="Line" vid="air_line">
              <a-input v-model="form.air_line" :disabled="disabled()"></a-input>
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="8">
            <form-item-validate label="Class" vid="air_class">
              <a-input v-model="form.air_class" :disabled="disabled()"></a-input>
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="8">
            <form-item-validate label="Fare" vid="fare">
              <a-input-number
                v-model="form.fare"
                :disabled="disabled()"
                :min="0"
                :precision="2"
                decimalSeparator="."
                class="w-full"
              />
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="8">
            <form-item-validate label="Tax" vid="tax">
              <a-input-number
                v-model="form.tax"
                :disabled="disabled()"
                :min="0"
                :precision="2"
                decimalSeparator="."
                class="w-full"
              />
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="8">
            <form-item-validate label="Total" vid="total">
              <a-input-number
                v-model="form.total"
                :disabled="disabled()"
                :min="0"
                :precision="2"
                decimalSeparator="."
                class="w-full"
              />
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="12">
            <form-item-validate label="Info" vid="air_info">
              <a-textarea v-model="form.air_info" :disabled="disabled()" :rows="5"></a-textarea>
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="12">
            <form-item-validate label="remark" vid="remark">
              <a-textarea v-model="form.remark" :disabled="disabled()" :rows="5"></a-textarea>
            </form-item-validate>
          </a-col>
        </a-row>

        <a-upload-dragger
          v-if="post_type == 'edit' && form.uploads"
          :multiple="true"
          :before-upload="beforeUpload"
          :remove="handleRemove"
          action="http://ubangservice.com/api/uploads/"
          :withCredentials="true"
          :default-file-list="form.uploads"
          :data="{
            content_type: 'ticket',
            object_id: $route.params.id
          }"
          :disabled="disabled() || form.is_confirm"
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

      <form-item-validate vid="user_id">
        <itinerary-related-list @select="onSelectItinerary" :disabled="disabled()" />
      </form-item-validate>
    </page-header-wrapper>

    <a-row v-if="post_type == 'edit'">
      <a-col :span="12">
        <a-popconfirm
          title="Are you sure delete?"
          @confirm="onDelete"
          okText="Yes"
          cancelText="No"
          v-if="$auth('delete_ticket')"
        >
          <a-button href="javascript:;" type="danger">Delete</a-button>
        </a-popconfirm>
      </a-col>

      <a-col :span="12" class="text-right">
        <a-button
          v-if="post_type == 'edit'"
          v-action:change_ticket
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
          v-action:add_ticket
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
import { getTicket, updateTicket, createTicket, deleteTicket } from '@/api/ticket'
import { uploadFile, deleteFile } from '@/api/upload'
import ItineraryRelatedList from '@/views/itinerary/RelatedList'

import moment from 'moment'

export default {
  components: { FormValidate, FormItemValidate, ItineraryRelatedList },
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
        if (this.post_type == 'add' && this.$auth('add_ticket')) {
          return false
        }

        if (this.post_type == 'edit' && this.$auth('change_ticket')) {
          return false
        }

        return true
      },
      form: {}
    }
  },
  mounted() {
    if (this.$route.params.id) {
      this.getTicketData()
    }
  },
  computed: {
    current() {
      var _step = 0
      if (this.form.is_booking) {
        _step = 1
      }

      if (this.form.is_confirm) {
        _step = 2
      }

      if (this.form.is_complete) {
        _step = 3
      }

      return _step
    }
  },
  methods: {
    getTicketData() {
      this.loading = true
      getTicket(this.$route.params.id)
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
      var form = Object.assign({
        serial_no: this.form.serial_no,
        air_line: this.form.air_line,
        air_class: this.form.air_class,
        fare: this.form.fare,
        tax: this.form.tax,
        total: this.form.total,
        air_info: this.form.air_info,
        remark: this.form.remark,
        itinerary_id: this.form.itinerary_id
      })

      if (this.post_type == 'edit') {
        updateTicket(this.$route.params.id, form)
          .then(res => {
            const { data, extra } = res.result
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
        createTicket(form)
          .then(res => {
            this.$router.replace({
              name: 'TicketDetail',
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
      deleteTicket(this.$route.params.id)
        .then(() => {
          this.$router.go(-1)
        })
        .finally(() => {
          this.updateing = false
        })
    },
    onSelectItinerary(val) {
      if (val != null) {
        this.form.itinerary_id = val[0]
      }
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
