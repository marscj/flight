<template>
  <validation-provider :vid="vid" :name="name" v-slot="{ errors }">
    <a-form-item>
      <slot> </slot>
    </a-form-item>
    <span class="errorText">{{ errors[0] }}</span>
  </validation-provider>
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
    }
  }
}
</script>

<style></style>
