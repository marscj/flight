<template>
  <a-modal :visible="visible" :title="title" @ok="submit" :confirmLoading="loading"> </a-modal>
</template>

<script>
import { createUser } from '@/api/user'
export default {
  data() {
    return {
      form: this.$form.createForm(this),
      loading: false,
      visible: false
    }
  },
  methods: {
    submit() {
      this.loading = true
      createUser(this.form).then(res => {
        this.loading = false
        this.setVisible(false)
      })
    },
    setVisible(b) {
      this.visible = b
    }
  },
  props: {
    title: {
      type: null,
      default: undefined
    }
  }
}
</script>

<style></style>
