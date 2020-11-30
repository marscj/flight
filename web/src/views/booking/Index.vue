<template>
  <form-validate ref="observer">
    <page-header-wrapper>
      <template slot="extra">
        <a-button v-action:change_booking type="primary" @click="submit" :loading="updateing" html-type="submit">
          Submit
        </a-button>
      </template>
      <a-card class="card" title="Base Information" :bordered="false">
        <form-item-validate label="Name" vid="name">
          <a-input v-model="form.name" :disabled="!$auth('change_booking')" />
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
          v-if="$auth('delete_booking')"
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
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import { getBooking, updateBooking, deleteBooking } from '@/api/booking'
import moment from 'moment'
import _ from 'lodash'

export default {
  components: { FormValidate, FormItemValidate },

  data() {
    return {
      loading: false,
      updateing: false,
      form: {}
    }
  },
  mounted() {
    this.getBookingData()
  },
  methods: {
    getBookingData() {
      this.loading = true
      getBooking(this.$route.params.id)
        .then(res => {
          const { data, extra } = res.result
          this.form = Object.assign({}, data)
        })
        .finally(() => {
          this.loading = false
        })
    },
    submit() {
      this.updateing = true
      var form = Object.assign({}, this.form, {})
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

table {
  border-collapse: collapse; //collapse separate;
}

tr:nth-child(2n + 1) {
  background-color: #edf2f7;
}

tr:nth-child(2n) {
  background-color: white;
}

tr:hover {
  background-color: rgba(255, 254, 200, 0.77);
}
</style>
