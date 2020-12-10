<template>
  <form-validate ref="observer" :form="form">
    <page-header-wrapper v-if="post_type == 'add'">
      <a-card class="card" title="Ticket Info" :bordered="false">
        <a-row class="form-row" :gutter="16">
          <a-col :sm="24" :md="8">
            <form-item-validate label="Serial No.">
              <a-input v-model="form.serial_no"></a-input>
            </form-item-validate>
          </a-col>
          <a-col :sm="24" :md="8">
            <form-item-validate label="Line">
              <a-input v-model="form.air_line"></a-input>
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="8">
            <form-item-validate label="Class">
              <a-input v-model="form.air_class"></a-input>
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="8">
            <form-item-validate label="Fare">
              <a-input v-model="form.fare"></a-input>
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="8">
            <form-item-validate label="Tax">
              <a-input v-model="form.tax"></a-input>
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="8">
            <form-item-validate label="Total">
              <a-input v-model="form.total"></a-input>
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="12">
            <form-item-validate label="Info">
              <a-textarea v-model="form.air_info" :rows="5"></a-textarea>
            </form-item-validate>
          </a-col>

          <a-col :sm="24" :md="12">
            <form-item-validate label="remark">
              <a-textarea v-model="form.remark" :rows="5"></a-textarea>
            </form-item-validate>
          </a-col>
        </a-row>
      </a-card>

      <itinerary-related-list :data="itineraries" @select="onSelectItinerary" />
    </page-header-wrapper>
    <page-header-wrapper v-else>
      <a-card class="card" title="Progress" :bordered="false"> </a-card>
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
      form: {},
      itineraries: []
    }
  },
  mounted() {
    if (this.post_type == 'add') {
      this.itineraries = Object.assign([], this.$route.params.itinerary)
    }

    if (this.$route.params.id) {
      this.getTicketData()
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
      var form = Object.assign({}, this.form, {})

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
      this.itineraries = Object.assign([], val)
    }
  }
}
</script>

<style lang="less" scoped>
.card {
  margin-bottom: 24px;
}
</style>
