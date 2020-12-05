import FormValidate from './FormValidate'

export default FormValidate

// import F from 'ant-design-vue/es/form/Form'

// export default {
//   props: Object.assign({}, F.props, {
//     vid: {
//       type: String,
//       default: undefined
//     },
//     name: {
//       type: String,
//       default: undefined
//     }
//   }),

//   methods: {
//     setErrors(error) {
//       if (
//         error != null &&
//         error.response != null &&
//         error.response.data != null &&
//         error.response.data.result != null
//       ) {
//         this.$refs.observer.setErrors(error.response.data.result)
//       } else {
//         this.$refs.observer.setErrors({ non_field_errors: error.response.data })
//       }
//     }
//   },

//   render() {
//     var props = {}

//     Object.keys(F.props).forEach(k => {
//       this[k] && (props[k] = this[k])
//       return props[k]
//     })

//     return (
//       <a-form {...{ props }}>
//         <validation-observer ref="observer">
//           {Object.keys(this.$slots).map(name => (
//             <template slot={name}>{this.$slots[name]}</template>
//           ))}
//         </validation-observer>
//       </a-form>
//     )
//   }
// }
