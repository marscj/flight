import '@/assets/js/jmessage-sdk-web.2.6.0.min.js'

const message = {
  state: {
    JIM: null
  },

  mutations: {
    SET_JIM(state, JIM) {
      state.JIM = JIM
    },
    SET_ISLOGIN(state, login) {
      state.isLogin = login
    }
  },

  actions: {
    initJIM({ commit, dispatch }) {
      const JIM = new JMessage()
      commit('SET_JIM', JIM)

      JIM.init({
        appkey: '001486b3ce6d38e6c013530f',
        random_str: '404',
        signature: '7db047a67a9d7293850ac69d14cc82bf',
        timestamp: 1507882399401,
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
    }
  }
}

export default message
