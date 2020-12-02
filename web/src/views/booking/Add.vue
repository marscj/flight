<template>
  <index :isEdit="false"> </index>
</template>

<script>
import Index from './Index'
export default {
  components: { Index },
  props: {
    post_type: {
      type: String,
      default: 'default'
    }
  },
  mounted() {}
}
</script>

<style></style>
