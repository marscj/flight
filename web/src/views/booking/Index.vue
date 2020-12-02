<template>
  <form-validate ref="observer">
    <page-header-wrapper>
      <template v-if="post_type == 'edit'" slot="extra">
        <router-link :to="{ name: 'BookingHistory', params: { id: $route.params.id } }">
          <span>History</span>
        </router-link>
      </template>
      <template v-else-if="post_type == 'history'" slot="extra">
        <router-link :to="{ name: 'BookingDetail', params: { id: $route.params.id } }">
          <span>Back</span>
        </router-link>
      </template>

      <a-card class="card" title="Base Information" :bordered="false">
        <form-item-validate label="Title" vid="title" required>
          <a-input v-model="form.title" :maxLength="64" :disabled="disabled()" />
        </form-item-validate>
        <form-item-validate label="Remark" vid="remark">
          <a-textarea v-model="form.remark" :maxLength="1024" :rows="5" :disabled="disabled()" />
        </form-item-validate>
      </a-card>
    </page-header-wrapper>

    <a-row>
      <a-col :span="12">
        <a-popconfirm
          title="Are you sure cancel?"
          @confirm="onDelete"
          okText="Yes"
          cancelText="No"
          v-if="$auth('delete_booking') && edit"
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
import { getBooking, updateBooking, createBooking, deleteBooking } from '@/api/booking'

export default {
  components: { FormValidate, FormItemValidate, History },

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
        if (this.post_type == 'add') {
          return false
        }

        if (this.post_type == 'edit' && this.$auth('change_booking')) {
          return false
        }

        return true
      },
      form: {},
      historyData: []
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
      getBooking(this.$route.params.id, { history: true })
        .then(res => {
          const { data, extra } = res.result
          this.form = Object.assign({}, data)
          this.historyData = Object.assign([], extra.history)
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
      } else if (this.post_type == 'add') {
        createBooking(form)
          .then(res => {
            this.$router.push({
              name: 'BookingDetail',
              params: { id: res.result.id }
            })
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
    onHistory() {
      this.$router.push({ name: 'BookingHistory', params: { id: this.$route.params.id } })
    }
  }
}
</script>

<style lang="less" scoped>
.card {
  margin-bottom: 24px;
}
</style>
