<template>
  <a-modal v-model="visible" title="Rest Password" @ok="submit" :confirmLoading="loading">
    <form-validate ref="password">
      <form-item-validate label="New Password" vid="password">
        <a-input-password v-model="form.password" placeholder="Password" html-type="submit"> </a-input-password>
      </form-item-validate>
    </form-validate>
  </a-modal>
</template>

<script>
import { resetPassword } from '@/api/user'
import { FormValidate, FormItemValidate } from '@/components'
export default {
  components: { FormValidate, FormItemValidate },
  data() {
    return {
      form: {},
      loading: false,
      visible: false
    }
  },
  methods: {
    submit() {
      this.loading = true
      resetPassword(this.$route.params.id, this.form)
        .then(res => {
          this.setVisible(false)
        })
        .catch(error => {
          if (error.response) {
            this.$refs.password.setErrors(error)
          }
        })
        .finally(() => {
          this.loading = false
        })
    },
    setVisible(b) {
      this.visible = b
      if (this.visible) {
        this.form = {}
        this.$nextTick(() => {
          this.$refs.password.reset()
        })
      }
    }
  }
}
</script>

<style></style>
