<template>
  <div class="main">
    <a-form
      id="formLogin"
      class="user-layout-login"
      ref="formLogin"
      :form="form"
      @submit="handleSubmit"
    >
      <div>
        <a-form-item>
          <a-input
            size="large"
            type="text"
            placeholder="Email"
          >
            <a-icon slot="prefix" type="mail" :style="{ color: 'rgba(0,0,0,.25)' }"/>
          </a-input>
        </a-form-item>

        <a-form-item>
          <a-input-password
            size="large"
            placeholder="Password"
          >
            <a-icon slot="prefix" type="lock" :style="{ color: 'rgba(0,0,0,.25)' }"/>
          </a-input-password>
        </a-form-item>
        <a-form-item>
          <a-checkbox>Remember Me</a-checkbox>
        </a-form-item>
        <a-form-item>
          <vue-recaptcha
            ref="recaptcha"
            @verify="onVerify"
            @expired="onExpired"
            :sitekey="sitekey">
          </vue-recaptcha>
        </a-form-item>
        <a-form-item style="margin-top:24px">
          <a-button
            size="large"
            type="primary"
            htmlType="submit"
            class="login-button"
            :loading="state.loginBtn"
            :disabled="state.loginBtn"
          >Login</a-button>
        </a-form-item>

      </div>
    </a-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { timeFix } from '@/utils/util'
import VueRecaptcha from 'vue-recaptcha'

export default {
  el: '#root',
  components: {
    VueRecaptcha
  },
  data () {
    return {
      sitekey: '6LfV6doZAAAAAHlHV67QLRkMAFOT9GWpyBIM7TcO',
      loginBtn: false,
      form: this.$form.createForm(this)
    }
  },
  created () {
  },
  methods: {
    ...mapActions(['Login', 'Logout']),
    onVerify: function (response) {
      this.loginBtn = true
    },
    onExpired: function () {
      this.loginBtn = false
    },
    handleSubmit (e) {
    },
    loginSuccess (res) {
      this.$router.push({ path: '/' })
      setTimeout(() => {
        this.$notification.success({
          message: 'Welcome',
          description: `${timeFix()}，Welcome Back`
        })
      }, 1000)
      this.isLoginError = false
    },
    requestFailed (err) {
      this.isLoginError = true
      this.$notification['error']({
        message: '错误',
        description: ((err.response || {}).data || {}).message || '请求出现错误，请稍后再试',
        duration: 4
      })
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
