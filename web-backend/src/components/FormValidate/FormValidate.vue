<template>
  <validation-observer ref="observer">
    <a-form :form="form" @submit="submit"> </a-form>
  </validation-observer>
</template>

<script>
export default {
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

<style></style>
