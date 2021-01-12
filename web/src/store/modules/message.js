import Vue from 'vue'
import md5 from 'js-md5'
import { BASE_AUTH } from '@/store/mutation-types'

const message = {
  state: {
    JIM: null,
    isLogin: false
  },

  mutations: {
    SET_JIM(state, JIM) {
      state.JIM = JIM
    },
    SET_ISLOGIN(state, login) {
      state.isLogin = login
    },
    ADD_MESSAGE(state, message) {}
  },

  actions: {
    initJIM({ commit, dispatch }, action) {
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
          if (action == null) {
            dispatch('loginJIM')
          } else {
            dispatch(action)
          }
        })
        .onFail(function(data) {
          console.log('error:' + JSON.stringify(data))
        })
    },
    isInitJIM({ state }) {
      return state.JIM.isInit()
    },
    registJIM({ state, commit, dispatch }) {
      let user = Vue.ls.get(BASE_AUTH)

      if (user != null) {
        state.JIM.register(user)
          .onSuccess(function(data) {
            console.log('success:' + JSON.stringify(data))
          })
          .onFail(function(data) {
            console.log('error:' + JSON.stringify(data))
            appendToDashboard('error: ' + JSON.stringify(data))
          })
      }
    },
    loginJIM({ state, commit, dispatch }) {
      let user = Vue.ls.get(BASE_AUTH)
      if (user != null && !state.isLogin) {
        state.JIM.login(user)
          .onSuccess(function(data) {
            console.log('success:' + JSON.stringify(data))
            commit('SET_ISLOGIN', true)
            dispatch('listenSyncConversation')
            dispatch('listenMsgReceive')
            dispatch('listenDisconnect')
            dispatch('listenEventNotification')
            dispatch('listenMutiUnreadMsgUpdate')
          })
          .onFail(function(data) {
            if (data != null && data.code == '880103') {
              dispatch('registJIM')
            }
            console.log('loginError' + JSON.stringify(data))
          })
          .onTimeout(function() {})
      }
    },
    logoutJIM({ state, commit }) {
      state.JIM.loginOut()
      commit('SET_ISLOGIN', false)
    },
    //离线消息
    listenSyncConversation({ state, commit }) {
      state.JIM.onSyncConversation(data => {
        console.log(data)
      })
    },
    //聊天消息实时监听
    listenMsgReceive({ state, commit }) {
      state.JIM.onMsgReceive(data => {
        console.log(JSON.stringify(data))
        data.messages.forEach(x => commit('ADD_MESSAGE', x))
      })
    },
    //断线监听
    listenDisconnect({ state, commit }) {
      state.JIM.onDisconnect(() => {
        commit('SET_ISLOGIN', false)
      })
    },
    //业务事件监听
    listenEventNotification({ state, commit }) {
      state.JIM.onEventNotification(data => {
        if (data.event_type === 1) {
        }
      })
    },
    //会话未读数变更监听
    listenMutiUnreadMsgUpdate({ state, commit }) {
      state.JIM.onMutiUnreadMsgUpdate(function(data) {
        // data.type 会话类型
        // data.gid 群 id
        // data.appkey 所属 appkey
        // data.username 会话 username
      })
    }
  }
}

export default message