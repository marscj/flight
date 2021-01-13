<template>
  <a-modal v-model="visible" title="Change Password" @ok="submit" :confirmLoading="loading">
    <form-validate ref="password">
      <form-item-validate label="New Password" vid="new_password1">
        <a-input-password v-model="form.new_password1"> </a-input-password>
      </form-item-validate>

      <form-item-validate label="Repeat Password" vid="new_password2">
        <a-input-password v-model="form.new_password2"> </a-input-password>
      </form-item-validate>
    </form-validate>
  </a-modal>
</template>

<script>
import { changePassword } from '@/api/user'
import { FormValidate, FormItemValidate } from '@/components'
import { BASE_AUTH } from '@/store/mutation-types'

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

      changePassword(this.form)
        .then(res => {
          this.setVisible(false)
          console.log(this.$store.getters.userInfo.email, this.form.new_password1)
          this.$ls.set(BASE_AUTH, {
            username: this.$store.getters.userInfo.email,
            password: this.form.new_password1,
            is_md5: false
          })
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
