import Vue from '@/utils/vue'
import moment from '@/utils/moment'
import '@/utils/moment/locale/zh-cn'
moment.locale('zh-cn')

Vue.filter('NumberFormat', function(value) {
  if (!value) {
    return '0'
  }
  const intPartFormat = value.toString().replace(/(\d)(?=(?:\d{3})+$)/g, '$1,') // 将整数部分逢三一断
  return intPartFormat
})

Vue.filter('dayjs', function(dataStr, pattern = 'YYYY-MM-DD HH:mm:ss') {
  return moment(dataStr).format(pattern)
})

Vue.filter('moment', function(dataStr, pattern = 'YYYY-MM-DD HH:mm:ss') {
  return moment(dataStr).format(pattern)
})
