<template>
  <validation-observer ref="observer">
    <a-form :form="form" @submit="submit">
      <slot> </slot>

      <validation-provider name="non_field_errors" v-slot="{ errors }">
        <span class="errorText">{{ errors[0] }}</span>
      </validation-provider>
    </a-form>
  </validation-observer>
</template>

<script>
export default {
  name: 'FormValidate',
  props: {
    form: {
      type: Object,
      default: undefined,
    },
    submit: {
      type: Function,
      default: () => {},
    },
    error: {
      type: Object,
      default: undefined,
    },
  },
  methods: {
    checkError(errors) {
      this.$refs.observer.setErrors(errors)
    },
  },
}
</script>
