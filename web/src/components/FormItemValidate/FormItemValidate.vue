<template>
  <a-form-item
    :id="id"
    :htmlFor="htmlFor"
    :prefixCls="prefixCls"
    :label="label"
    :labelCol="labelCol"
    :wrapperCol="wrapperCol"
    :help="help"
    :extra="extra"
    :validateStatus="validateStatus"
    :hasFeedback="hasFeedback"
    :required="required"
    :colon="colon"
    :fieldDecoratorId="fieldDecoratorId"
    :fieldDecoratorOptions="fieldDecoratorOptions"
    :selfUpdate="selfUpdate"
    :labelAlign="labelAlign"
  >
    <validation-provider :vid="vid" :name="name" v-slot="{ errors }">
      <slot> </slot>
      <span class="errorText">{{ errors[0] }}</span>
    </validation-provider>
  </a-form-item>
</template>

<script>
import F from 'ant-design-vue/es/form/FormItem'

export default {
  props: Object.assign({}, F.props, {
    vid: {
      type: String,
      default: undefined
    },
    name: {
      type: String,
      default: undefined
    }
  }),
  mounted() {},
  data() {
    return {
      nidaye: {
        label: 'caonima'
      }
    }
  }
}
</script>

<style></style>
