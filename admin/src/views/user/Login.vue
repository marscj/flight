<template>
  <div class="main">
    <form-validate class="user-layout-login" :form="form" @submit="handleSubmit">
      <div>
        <form-item-validate vid="email">
          <a-input v-model="form.email" size="large" type="text" placeholder="Email">
            <a-icon slot="prefix" type="mail" :style="{ color: 'rgba(0,0,0,.25)' }" />
          </a-input>
        </form-item-validate>

        <a-form-item>
          <a-input-password v-model="form.password" size="large" placeholder="Password">
            <a-icon slot="prefix" type="lock" :style="{ color: 'rgba(0,0,0,.25)' }" />
          </a-input-password>
        </a-form-item>
        <a-form-item>
          <a-checkbox v-model="form.remember">Remember Me</a-checkbox>
        </a-form-item>
        <a-form-item style="margin-top: 24px">
          <a-button
            size="large"
            type="primary"
            htmlType="submit"
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
import FormValidate from '@/components/FormValidate'
import FormItemValidate from '@/components/FormItemValidate'

export default {
  components: {
    FormValidate,
    FormItemValidate,
  },
  data() {
    return {
      sitekey: '6LfV6doZAAAAAHlHV67QLRkMAFOT9GWpyBIM7TcO',
      response: undefined,
      loginBtn: {
        loading: false,
      },
      form: {
        email: '',
        password: '',
        backend: true,
      },
    }
  },
  created() {},
  mounted() {},
  methods: {
    ...mapActions(['Login', 'Logout']),
    handleSubmit(e) {
      e.preventDefault()
      const { Login } = this

      console.log({
        email: this.form.email,
        password: this.form.password,
        backend: true,
      })

      Login({
        email: this.form.email,
        password: this.form.password,
        backend: true,
      })
        .then((res) => {
          this.loginSuccess(res)
        })
        .catch((error) => {
          console.log(error)
          // if (error.response) {
          //   this.$refs.observer.setErrors(error.response.data.result)
          // }
        })
    },
    loginSuccess(res) {
      this.$router.push({ path: '/' })
      setTimeout(() => {
        this.$notification.success({
          message: 'Welcome',
          description: `${timeFix()}，Welcome Back`,
        })
      }, 500)
      this.isLoginError = false
    },
  },
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
