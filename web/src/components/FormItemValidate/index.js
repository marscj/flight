import FormItemValidate from './FormItemValidate'

export default FormItemValidate

// import F from 'ant-design-vue/es/form/FormItem'

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

//   render() {
//     var props = {}

//     Object.keys(F.props).forEach(k => {
//       this[k] && (props[k] = this[k])
//       return props[k]
//     })

//     return (
//       <a-form-item {...{ props }}>
//         <validation-provider>
//           {Object.keys(this.$slots).map(name => (
//             <template slot={name}>{this.$slots[name]}</template>
//           ))}
//           <span class="errorText"></span>
//         </validation-provider>
//       </a-form-item>
//     )
//   }
// }
