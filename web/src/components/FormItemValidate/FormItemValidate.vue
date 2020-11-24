<template>
  <a-form-item :label="label">
    <validation-provider :vid="vid" :name="name" v-slot="{ errors }">
      <slot> </slot>
      <span class="errorText">{{ errors[0] }}</span>
    </validation-provider>
  </a-form-item>
</template>

<script>
export default {
  props: {
    vid: {
      type: String,
      default: undefined
    },
    name: {
      type: String,
      default: undefined
    },
    label: {
      type: String,
      default: undefined
    }
  }
}
</script>

<style></style>
