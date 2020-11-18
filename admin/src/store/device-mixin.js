import { mapState } from '@/store/vuex'

const deviceMixin = {
  computed: {
    ...mapState({
      isMobile: state => state.app.isMobile
    })
  }
}

export { deviceMixin }
