import Vue from 'vue'
import md5 from 'js-md5'
import { BASE_AUTH } from '@/store/mutation-types'

const message = {
  state: {
    JIM: null
  },

  mutations: {
    SET_JIM(state, JIM) {
      state.JIM = JIM
    },
    ADD_MESSAGE(state, message) {}
  },

  actions: {
    initJIM({ commit, dispatch }) {
      const JIM = new JMessage()
      commit('SET_JIM', JIM)
      var timestamp = new Date().getTime()

      JIM.init({
        appkey: '001486b3ce6d38e6c013530f',
        random_str: '022cd9fd995849b',
        signature: md5(
          `appkey=001486b3ce6d38e6c013530f&timestamp=${timestamp}&random_str=022cd9fd995849b&key=cd17b4772965d340d791c6a0`
        ),
        timestamp: timestamp,
        flag: 1
      })
        .onSuccess(function(data) {
          console.log('success:' + JSON.stringify(data))
          if (location.pathname !== '/login') {
            dispatch('loginJIM')
          }
        })
        .onFail(function(data) {
          console.log('error:' + JSON.stringify(data))
        })
    },
    loginJIM({ state, commit, dispatch }) {
      let user = {
        username: 'admin',
        password: 'admin123'
      }
      Object.assign(user, { is_md5: true })
      state.JIM.login({
        username: 'admin',
        password: 'admin123'
      })
        .onSuccess(function() {
          dispatch('listenMessageReceive')
        })
        .onFail(function(data) {
          console.log('loginError' + JSON.stringify(data))
        })
        .onTimeout(function() {})
    },
    listenMessageReceive({ state, commit }) {
      state.JIM.onMsgReceive(data => {
        console.log(JSON.stringify(data))
        data.messages.forEach(x => commit('ADD_MESSAGE', x))
      })
    }
  }
}

export default message
