<template>
  <div :class="wrpCls">
    <span> {{ messageStatus }}</span>
    <avatar-dropdown :menu="showMenu" :current-user="currentUser" :class="prefixCls" />
    <!-- <select-lang :class="prefixCls" /> -->
  </div>
</template>

<script>
import AvatarDropdown from './AvatarDropdown'
// import SelectLang from '@/components/SelectLang'
import { mapState } from 'vuex'

export default {
  name: 'RightContent',
  components: {
    AvatarDropdown
    // SelectLang
  },
  props: {
    prefixCls: {
      type: String,
      default: 'ant-pro-global-header-index-action'
    },
    isMobile: {
      type: Boolean,
      default: () => false
    },
    topMenu: {
      type: Boolean,
      required: true
    },
    theme: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      showMenu: true
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.user.info,
      welcome: state => state.user.welcome
    }),
    wrpCls() {
      return {
        'ant-pro-global-header-index-right': true,
        [`ant-pro-global-header-index-${this.isMobile || !this.topMenu ? 'light' : this.theme}`]: true
      }
    },
    messageStatus() {
      return this.$store.getters.message.status
    }
  },
  mounted() {}
}
</script>
