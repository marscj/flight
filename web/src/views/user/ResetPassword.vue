<template>
  <a-modal :visible="visible" title="Rest Password" @ok="submit" :confirmLoading="loading">
    <form-item-validate label="New Password" vid="password">
      <a-input-password v-model="form.password" placeholder="Password"> </a-input-password>
    </form-item-validate>
  </a-modal>
</template>

<script>
import { resetPassword } from '@/api/user'
import { FormItemValidate } from '@/components'
export default {
  components: { FormItemValidate },
  data() {
    return {
      form: {},
      loading: false,
      visible: false
    }
  },
  mounted() {
    this.$nextTick(() => {})
  },
  methods: {
    submit() {
      this.loading = true
      resetPassword(this.$route.params.id, this.form)
        .then(res => {
          this.setVisible(false)
        })
        .catch(error => {
          this.$emit('checkError', error)
        })
        .finally(() => {
          this.loading = false
        })
    },
    setVisible(b) {
      this.visible = b
    }
  }
}
</script>

<style></style>
