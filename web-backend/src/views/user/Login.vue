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
            v-model="form.email"
            size="large"
            type="text"
            placeholder="Email"
          >
            <a-icon slot="prefix" type="mail" :style="{ color: 'rgba(0,0,0,.25)' }"/>
          </a-input>
        </a-form-item>

        <a-form-item>
          <a-input-password
            v-model="form.password"
            size="large"
            placeholder="Password"
          >
            <a-icon slot="prefix" type="lock" :style="{ color: 'rgba(0,0,0,.25)' }"/>
          </a-input-password>
        </a-form-item>
        <a-form-item>
          <a-checkbox v-model="form.remember">Remember Me</a-checkbox>
        </a-form-item>
        <a-form-item>
          <div id="grecaptcha" align='center'></div>
        </a-form-item>
        <a-form-item style="margin-top:24px">
          <a-button
            size="large"
            type="primary"
            htmlType="submit"
            class="login-button"
            @click="handleSubmit"
            :loading="loginBtn.loading"
            :disabled="loginBtn.disabled"
          >Login</a-button>
        </a-form-item>
      </div>
    </a-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { timeFix } from '@/utils/util'

export default {
  components: {
  },
  data () {
    return {
      sitekey: '6LfV6doZAAAAAHlHV67QLRkMAFOT9GWpyBIM7TcO',
      response: undefined,
      loginBtn: {
        loading: false,
        disabled: true
      },
      form: {
        email: '',
        password: '',
        backend: true,
        recaptcha: '',
        remember: true
      }
    }
  },
  created () {
  },
  mounted() {
    setTimeout(() => {
        window.grecaptcha.render('grecaptcha', {
          'sitekey': this.sitekey,
          'callback': this.onVerify,
          'expired-callback': this.onExpired
        })
      }, 100)
  },
  methods: {
    ...mapActions(['Login', 'Logout']),
    onVerify: function (response) {
      console.log(response)
      this.response = response
      this.loginBtn.disabled = false
    },
    onExpired: function () {
      this.response = null
      this.loginBtn.disabled = true
    },
    handleSubmit (e) {
      e.preventDefault()
      const {
        Login
      } = this

      console.log({
        email: this.form.email,
        password: this.form.password,
        backend: true,
        recaptcha: this.response
      })

      Login({
        email: this.form.email,
        password: this.form.password,
        backend: true,
        recaptcha: this.response,
        remember: this.form.remember
      }).then(res => {
        this.loginSuccess(res)
      }).catch(
        error => {
          console.log(error)
        }
      )
    },
    loginSuccess (res) {
      this.$router.push({ path: '/' })
      setTimeout(() => {
        this.$notification.success({
          message: 'Welcome',
          description: `${timeFix()}，Welcome Back`
        })
      }, 500)
      this.isLoginError = false
    }
  }
}
</script>

<style lang="less" scoped>
.user-layout-login {
  label {
    font-size: 14px;
  }

  .grecaptcha {
    transform:scale(1);
    transform-origin:0 0;
  }

  button.login-button {
    padding: 0 15px;
    font-size: 16px;
    height: 40px;
    width: 100%;
  }
}
</style>
