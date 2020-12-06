<template>
  <form-validate ref="observer">
    <page-header-wrapper :content="content">
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

      <div v-if="post_type == 'history'" class="pb-4">
        <a-row>
          <a-col :span="12">
            <a-button type="link" v-if="history_index > 0" @click="onPreviou">Previou</a-button>
          </a-col>
          <a-col :span="12" class="text-right">
            <a-button type="link" v-if="history_index < history_length - 1" @click="onNext">Next</a-button>
          </a-col>
        </a-row>
      </div>

      <a-card class="card" title="Base Information" :bordered="false">
        <form-item-validate label="Title" vid="title" required>
          <a-input v-model="form.title" :maxLength="64" :disabled="disabled()" />
        </form-item-validate>
        <form-item-validate label="Remark" vid="remark">
          <a-textarea v-model="form.remark" :maxLength="1024" :rows="5" :disabled="disabled()" />
        </form-item-validate>
      </a-card>

      <itinerary-list v-if="post_type == 'edit'" />
    </page-header-wrapper>

    <a-row v-if="post_type == 'edit'">
      <a-col :span="12">
        <a-popconfirm
          title="Are you sure cancel?"
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

        if (this.post_type == 'history') {
          return true
        }

        return true
      },
      form: {},
      historyData: [],
      history_index: 0,
      history_length: 0,
      content: ''
    }
  },
  watch: {
    history_index(val) {
      if (this.post_type == 'history') {
        this.form = Object.assign({}, this.historyData[val])
        this.setContent()
      }
    }
  },
  mounted() {
    if (this.$route.params.id) {
      this.getBookingData()
    }
  },
  methods: {
    setContent() {
      this.content =
        'author: ' +
        this.historyData[this.history_index].history_user +
        '  change at: ' +
        moment(this.historyData[this.history_index].history_date).format('YYYY-MM-DD HH:mm')
    },
    getBookingData() {
      this.loading = true
      getBooking(this.$route.params.id, { history: true })
        .then(res => {
          console.log(res.result)
          const { data, history } = res.result
          this.historyData = Object.assign([], history)
          this.history_length = history.length
          this.history_index = history.length - 1 > 0 ? history.length - 1 : 0

          if (this.post_type == 'edit') {
            this.form = Object.assign({}, data)
          }

          if (this.post_type == 'history') {
            this.form = Object.assign({}, this.historyData[this.history_index])
          }
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
              params: { id: res.result.id }
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
    onPreviou() {
      if (this.history_index > 0) {
        this.history_index--
      }
    },
    onNext() {
      if (this.history_index < this.history_length - 1) {
        this.history_index++
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
