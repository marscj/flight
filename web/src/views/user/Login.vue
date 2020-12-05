<template>
  <div class="main">
    <form-validate ref="observer" :submit="handleSubmit" :form="form" class="user-layout-login">
      <div>
        <form-item-validate vid="email">
          <a-input v-model="form.email" size="large" type="text" placeholder="Email">
            <a-icon slot="prefix" type="mail" :style="{ color: 'rgba(0,0,0,.25)' }" />
          </a-input>
        </form-item-validate>

        <form-item-validate vid="password">
          <a-input-password v-model="form.password" size="large" placeholder="Password">
            <a-icon slot="prefix" type="lock" :style="{ color: 'rgba(0,0,0,.25)' }" />
          </a-input-password>
        </form-item-validate>
        <a-form-item style="margin-top: 24px">
          <a-button
            size="large"
            type="primary"
            html-type="submit"
            class="login-button"
            @click="handleSubmit"
            :loading="loginBtn.loading"
            >Login
          </a-button>
        </a-form-item>
      </div>
    </form-validate>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { timeFix } from '@/utils/util'
import { FormItemValidate } from '@/components/'
import FormValidate from '@/components/FormValidate'

export default {
  components: {
    FormValidate,
    FormItemValidate
  },
  data() {
    return {
      sitekey: '6LfV6doZAAAAAHlHV67QLRkMAFOT9GWpyBIM7TcO',
      response: undefined,
      loginBtn: {
        loading: false
      },
      form: {
        email: 'admin@admin.com',
        password: 'admin123',
        backend: true
      },
      error: undefined
    }
  },
  methods: {
    ...mapActions(['Login']),
    handleSubmit(e) {
      e.preventDefault()
      const { Login } = this

      Login({
        email: this.form.email,
        password: this.form.password,
        backend: true
      })
        .then(res => {
          this.loginSuccess(res)
        })
        .catch(error => {
          this.$refs.observer.setErrors(error)
        })
    },
    loginSuccess(res) {
      this.$router.push({ path: '/' })
    }
  }
}
</script>

<style lang="less" scoped>
.user-layout-login {
  label {
    font-size: 14px;
  }

  button.login-button {
    padding: 0 15px;
    font-size: 16px;
    height: 40px;
    width: 100%;
  }
}
</style>
