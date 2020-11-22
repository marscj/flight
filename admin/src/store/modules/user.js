import Vue from 'vue'
import { login, getInfo, logout } from '@/api/login'
import { ACCESS_TOKEN } from '@/store/mutation-types'
import { filterGroup } from './permission'

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
    Login({ commit }, userInfo) {
      return new Promise((resolve, reject) => {
        login(userInfo)
          .then((response) => {
            const result = response.result
            Vue.ls.set(ACCESS_TOKEN, result.token)
            commit('SET_TOKEN', result.token)
            resolve()
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    // 获取用户信息
    GetInfo({ commit }) {
      return new Promise((resolve, reject) => {
        getInfo()
          .then((response) => {
            const result = response.result
            var roles = result.roles

            if (roles && roles.length > 0) {
              var total = roles.map((f) => f.permissions.length).reduce((total, e) => total + e)
              var _roles = filterGroup(roles)

              if (total > 0 && _roles.length > 0) {
                commit('SET_ROLES', result.roles)
                commit('SET_INFO', result)
              } else {
                reject(new Error("You don't have permission to access."))
              }
            } else {
              reject(new Error("You don't have permission to access."))
            }
            resolve(response)
          })
          .catch((error) => reject(error))
      })
    },

    // 登出
    Logout({ commit, state }) {
      return new Promise((resolve) => {
        logout(state.token)
          .then(() => {
            commit('SET_TOKEN', '')
            commit('SET_ROLES', [])
            Vue.ls.remove(ACCESS_TOKEN)
            resolve()
          })
          .catch(() => {
            resolve()
          })
          .finally(() => {})
      })
    }
  }
}

export default user
