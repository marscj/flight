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
    },
    q: {
      type: String,
      default: 'default'
    }
  },
  mounted() {
    console.log(this.$route.props)
    console.log(this.$route.query)
    console.log(this.q)
    console.log(this.post_type)
  }
}
</script>

<style></style>
