<template>
  <validation-observer ref="observer">
    <a-form
      :form="form"
      :layout="layout"
      :labelCol="labelCol"
      :wrapperCol="wrapperCol"
      :colon="colon"
      :labelAlign="labelAlign"
      :prefixCls="prefixCls"
      :hideRequiredMark="hideRequiredMark"
      :autoFormCreate="autoFormCreate"
      :options="options"
      :selfUpdate="selfUpdate"
    >
      <slot> </slot>

      <validation-provider name="non_field_errors" v-slot="{ errors }">
        <span class="errorText">{{ errors[0] }}</span>
      </validation-provider>
    </a-form>
  </validation-observer>
</template>

<script>
import F from 'ant-design-vue/es/form/Form'
export default {
  name: 'FormValidate',
  props: Object.assign({}, F.props, {}),
  methods: {
    setErrors(error) {
      // setTimeout(() => {
      //   this.$notification.success({
      //     message: 'Error: ' + error.response.status,
      //     description: error.response.statusText
      //   })
      // }, 500)

      if (
        error != null &&
        error.response != null &&
        error.response.data != null &&
        error.response.data.result != null
      ) {
        this.$refs.observer.setErrors(error.response.data.result)
      } else {
        // this.$refs.observer.setErrors({ non_field_errors: error.response.data })
      }
    },
    reset() {
      this.$refs.observer.reset
    }
  }
}
</script>
