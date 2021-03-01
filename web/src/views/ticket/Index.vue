<template>
  <form-validate ref="observer" :form="form">
    <page-header-wrapper>
      <template v-if="post_type == 'add'" slot="extra">
        <a-button type="primary" v-action:add_ticket :loading="updateing" html-type="submit" @click="book()"
          >Book</a-button
        >
      </template>
      <template v-else slot="extra">
        <a-button v-action:change_ticket type="primary" :loading="updateing" html-type="submit" @click="book()"
          >Update</a-button
        >
        <a-button v-if="status == 4" type="primary" @click="rebook()">Rebook</a-button>
        <a-button type="primary" @click="change()">Change</a-button>
        <a-button type="primary" @click="cancel()">Cancel</a-button>
      </template>

      <a-card
        :bordered="false"
        :tabList="[
          {
            key: 'tickets',
            scopedSlots: { tab: 'tab_ticket' }
          },
          {
            key: 'messages',
            scopedSlots: { tab: 'tab_message' }
          }
        ]"
        :activeTabKey="$route.query.tab"
        @tabChange="tabChange"
      >
        <template slot="tab_ticket">
          <span class="text-lg">Tickets</span>
        </template>

        <template slot="tab_message">
          <a-badge :count="form.comments == null ? 0 : form.comments.length" :offset="[12]">
            <span class="text-lg">Messages</span>
          </a-badge>
        </template>

        <div v-if="tab === 'tickets'">
          <a-card v-if="post_type == 'edit'" class="card" title="Progress">
            <a-steps direction="horizontal" :current="status" progressDot>
              <a-step :title="text_status[0]" />
              <a-step :title="text_status[1]" />
              <a-step :title="text_status[2]" />
              <a-step v-if="status == 4" :title="text_status[4]" status="error" />
              <a-step v-else :title="text_status[3]" />
              <a-step v-if="status != 4" :title="text_status[5]" />
            </a-steps>
          </a-card>
          <a-card class="card" title="Ticket Info">
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
              action="http://thesaadiyat.com/api/uploads/"
              :withCredentials="true"
              :default-file-list="form.uploads"
              :data="{
                content_type: 'ticket',
                object_id: $route.params.id
              }"
              :disabled="disabled() || check_status || check_lock"
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

          <form-item-validate vid="itinerary_id">
            <itinerary-related-list @select="onSelectItinerary" :disabled="disabled() || post_type != 'add'" />
          </form-item-validate>

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
          </a-row>
        </div>
        <message v-else-if="tab === 'messages'"></message>
      </a-card>
    </page-header-wrapper>
  </form-validate>
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import { getTicket, updateTicket, createTicket, deleteTicket } from '@/api/ticket'
import { uploadFile, deleteFile } from '@/api/upload'
import ItineraryRelatedList from '@/views/itinerary/RelatedList'
import Message from './Message'

import moment from 'moment'

const StatusTexts = [
  ['New', 'Booked', 'Watting Confirm', 'Confirmed', 'Refused', 'Completed'],
  ['New', 'Changed', 'Watting Confirm', 'Confirmed', 'Refused', 'Completed'],
  ['New', 'Canceled', 'Watting Confirm', 'Confirmed', 'Refused', 'Completed']
]

export default {
  components: { FormValidate, FormItemValidate, ItineraryRelatedList, Message },
  props: {
    post_type: {
      type: String,
      default: 'edit'
    }
  },
  data() {
    return {
      StatusTexts,
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
      form: {
        serial_no: ''
      },
      itinerary: {}
    }
  },
  mounted() {
    if (this.$route.params.id) {
      this.getTicketData()
    }
  },
  computed: {
    tab() {
      return this.$route.query.tab ? this.$route.query.tab : 'tickets'
    },
    check_status() {
      if (this.status == 3 || this.status == 5) {
        return false
      }

      return true
    },
    check_lock() {
      return this.itinerary.is_lock ?? true
    },
    type_status() {
      if (this.$route.params.type_status != null) {
        return this.$route.params.type_status
      }

      if (this.form != null && this.form.type_status != null) {
        return this.form.type_status
      }

      return 0
    },
    status() {
      if (this.form.normal_status != null && this.form.change_status != null && this.form.cancel_status != null) {
        switch (this.type_status) {
          case 0:
            return this.form.normal_status ?? 0
          case 1:
            return this.form.change_status ?? 0
          case 2:
            return this.form.cancel_status ?? 0
        }
      }
      return 0
    },
    text_status() {
      return StatusTexts[this.type_status ?? 0]
    }
  },
  methods: {
    tabChange(val) {
      this.$router.push({
        ...this.$route,
        name: this.$route.name,
        query: Object.assign({}, this.$route.query, {
          tab: val
        })
      })
    },
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
        itinerary_id: this.itinerary.id ?? this.form.itinerary_id,
        type_status: this.type_status,
        normal_status: this.type_status == 0 ? (this.post_type == 'edit' ? this.form.normal_status : 2) : 0,
        change_status: this.type_status == 1 ? (this.post_type == 'edit' ? this.form.change_status : 2) : 0,
        cancel_status: this.type_status == 2 ? (this.post_type == 'edit' ? this.form.cancel_status : 2) : 0,
        parent: this.$route.params.parent_id
      })
      console.log(form)
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
      if (val != null && val.length > 0) {
        this.itinerary = val[0]
        this.form.serial_no = val[0].serial_no
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
    },
    book() {
      this.submit()
    },
    rebook() {
      this.$router.push({
        name: 'AddTicket',
        params: Object.assign({}, this.$route.params, {
          type_status: 0,
          parent_id: this.form.parent_id ?? this.form.id
        })
      })
    },
    change() {
      this.$router.push({
        name: 'AddTicket',
        params: Object.assign({}, this.$route.params, {
          type_status: 1,
          parent_id: this.form.parent_id ?? this.form.id
        })
      })
    },
    cancel() {
      this.$router.push({
        name: 'AddTicket',
        params: Object.assign({}, this.$route.params, {
          type_status: 2,
          parent_id: this.form.parent_id ?? this.form.id
        })
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
