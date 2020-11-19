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
    checkError(error) {
      setTimeout(() => {
        this.$notification.success({
          message: 'Error: ' + error.response.status,
          description: error.response.statusText,
        })
      }, 500)

      if (
        error != null &&
        error.response != null &&
        error.response.data != null &&
        error.response.data.result != null
      ) {
        this.$refs.observer.setErrors(error.response.data.result)
      } else {
        this.$refs.observer.setErrors({ non_field_errors: error.response.data })
      }
    },
  },
}
</script>
