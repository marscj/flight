<template>
  <validation-observer ref="observer">
    <a-form :form="form" :submit="submit">
      <slot> </slot>
    </a-form>
  </validation-observer>
</template>

<script>
export default {
  name: 'FormValidate',
  props: {
    form: {
      type: Object,
      default: undefined
    },
    submit: {
      type: Function,
      default: undefined
    }
  }
}
</script>
