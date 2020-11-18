import { mapState } from '@/store/@/store/vuex'

const i18nMixin = {
  computed: {
    ...mapState({
      currentLang: state => state.app.lang
    })
  },
  methods: {
    setLang(lang) {
      this.$store.dispatch('setLang', lang)
    }
  }
}

export default i18nMixin
