<template>
  <form-validate ref="observer">
    <page-header-wrapper>
      <a-card class="card" title="Progress" :bordered="false"> </a-card>
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
    }
  }
}
</script>

<style lang="less" scoped>
.card {
  margin-bottom: 24px;
}
</style>
