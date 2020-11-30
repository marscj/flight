import _ from 'lodash'
/**
 * <a-button v-if="$auth('change_user')">Button</a-button>
 * @param Vue
 */
function plugin(Vue) {
  if (plugin.installed) {
    return
  }

  !Vue.prototype.$auth &&
    Object.defineProperties(Vue.prototype, {
      $auth: {
        get() {
          const _this = this
          return permissions => {
            let _permissions = _.uniq(_this.$store.getters.roles.reduce((f1, f2) => f1.concat(f2.permissions), [])).map(
              f => f.codename
            )
            return _permissions.find(val => val === permissions)
          }
        }
      }
    })
}

export default plugin
