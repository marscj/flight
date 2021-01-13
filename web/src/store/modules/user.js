import Vue from 'vue'
import { login, getInfo, logout } from '@/api/login'
import { ACCESS_TOKEN, BASE_AUTH } from '@/store/mutation-types'

const user = {
  state: {
    token: '',
    name: '',
    welcome: '',
    avatar: '',
    roles: [],
    info: {}
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_NAME: (state, { name, welcome }) => {
      state.name = name
      state.welcome = welcome
    },
    SET_AVATAR: (state, avatar) => {
      state.avatar = avatar
    },
    SET_ROLES: (state, roles) => {
      state.roles = roles
    },
    SET_INFO: (state, info) => {
      state.info = info
    }
  },

  actions: {
    // 登录
    Login({ commit, dispatch }, userInfo) {
      return new Promise((resolve, reject) => {
        login(userInfo)
          .then(response => {
            const result = response.result
            Vue.ls.set(ACCESS_TOKEN, result.token)
            Vue.ls.set(BASE_AUTH, {
              username: userInfo.email,
              password: userInfo.password,
              is_md5: false
            })
            commit('SET_TOKEN', result.token)

            dispatch('isInitJIM').then(res => {
              if (res) {
                dispatch('loginJIM')
              } else {
                dispatch('initJIM')
              }
            })
            resolve()
          })
          .catch(error => {
            reject(error)
          })
      })
    },

    // 获取用户信息
    GetInfo({ commit, dispatch }) {
      return new Promise((resolve, reject) => {
        getInfo()
          .then(response => {
            const result = response.result
            var roles = result.roles

            if (roles && roles.length > 0) {
              commit('SET_ROLES', result.roles)
            } else {
              commit('SET_ROLES', [])
            }
            commit('SET_INFO', result)

            resolve(response)
          })
          .catch(error => reject(error))
      })
    },

    // 登出
    Logout({ state, commit, dispatch }) {
      commit('SET_TOKEN', '')
      commit('SET_ROLES', [])
      commit('SET_ROUTERS', [])
      Vue.ls.remove(ACCESS_TOKEN)
      Vue.ls.remove(BASE_AUTH)
      dispatch('logoutJIM')

      return new Promise(resolve => {
        logout(state.token)
          .then(() => {
            resolve()
          })
          .catch(() => {
            resolve()
          })
      })
    }
  }
}

export default user
