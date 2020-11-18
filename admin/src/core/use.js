import Vue from '@/core/vue'

// base library
import Antd from '@/core/ant-design-vue'
import Viser from '@/core/viser-vue'
import VueCropper from '@/core/vue-cropper'
import '@/core/ant-design-vue/dist/antd.less'

// ext library
import VueClipboard from '@/core/vue-clipboard2'
import MultiTab from '@/core/@/components/MultiTab'
import PageLoading from '@/core/@/components/PageLoading'
import PermissionHelper from '@/core/@/core/permission/permission'
// import '@/components/use'
import './directives/action'

VueClipboard.config.autoSetContainer = true

Vue.use(Antd)
Vue.use(Viser)
Vue.use(MultiTab)
Vue.use(PageLoading)
Vue.use(VueClipboard)
Vue.use(PermissionHelper)
Vue.use(VueCropper)

process.env.NODE_ENV !== 'production' && console.warn('[antd-pro] WARNING: Antd now use fulled imported.')
