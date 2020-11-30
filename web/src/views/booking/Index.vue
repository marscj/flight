<template>
  <form-validate ref="observer" v-if="!history">
    <page-header-wrapper>
      <template slot="extra">
        <a @click="onHistory">
          History
        </a>
        <a-button v-action:change_booking type="primary" @click="submit" :loading="updateing" html-type="submit">
          Submit
        </a-button>
      </template>
      <a-card class="card" title="Base Information" :bordered="false">
        <form-item-validate label="Title" vid="title" required>
          <a-input v-model="form.title" :maxLength="64" :disabled="!$auth('change_booking') && isEdit" />
        </form-item-validate>
        <form-item-validate label="Remark" vid="remark">
          <a-textarea
            v-model="form.remark"
            :maxLength="1024"
            :rows="5"
            :disabled="!$auth('change_booking') && isEdit"
          />
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
          v-if="$auth('delete_booking') && isEdit"
        >
          <a-button href="javascript:;" type="danger">Delete</a-button>
        </a-popconfirm>
      </a-col>

      <a-col :span="12" class="text-right">
        <a-button v-action:change_booking type="primary" @click="submit" :loading="updateing" html-type="submit">
          Submit
        </a-button>
      </a-col>
    </a-row>
  </form-validate>
  <history v-else :data="historyData"> </history>
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import { getBooking, updateBooking, createBooking, deleteBooking } from '@/api/booking'
import History from './History'

export default {
  components: { FormValidate, FormItemValidate, History },
  props: {
    isEdit: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      loading: false,
      updateing: false,
      form: {},
      history: false,
      historyData: []
    }
  },
  mounted() {
    if (this.isEdit) {
      this.getBookingData()
    }
  },
  methods: {
    getBookingData() {
      this.loading = true
      getBooking(this.$route.params.id)
        .then(res => {
          const { data, extra } = res.result
          this.form = Object.assign({}, data)
          this.historyData = Object.assign([], extra.history)

          console.log(res.result)
        })
        .finally(() => {
          this.loading = false
        })
    },
    submit() {
      this.updateing = true
      var form = Object.assign({}, this.form, {})
      if (this.isEdit) {
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
      } else {
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
      this.history = true
    }
  }
}
</script>

<style lang="less" scoped>
.card {
  margin-bottom: 24px;
}
</style>
