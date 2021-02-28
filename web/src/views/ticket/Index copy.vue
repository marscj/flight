<template>
  <a-card
    :bordered="false"
    :tabList="[
      {
        key: 'tickets',
        scopedSlots: { tab: 'tab_ticket' }
      },
      {
        key: 'messages',
        scopedSlots: { tab: 'tab_message' }
      }
    ]"
    :activeTabKey="$route.query.tab"
    @tabChange="tabChange"
  >
    <template slot="tab_ticket">
      <span class="text-lg">Tickets</span>
    </template>

    <template slot="tab_message">
      <a-badge :count="data.comments == null ? 0 : data.comments.length" :offset="[12]">
        <span class="text-lg">Messages</span>
      </a-badge>
    </template>

    <detail v-if="tab === 'tickets'"></detail>
    <message v-else-if="tab === 'messages'"></message>
  </a-card>
</template>

<script>
import { PageView } from '@/layouts'
import Detail from './Detail'
import Message from './Message'

export default {
  components: {
    PageView,
    Detail,
    Message
  },
  data() {
    return {
      data: {},
      title: 'Order'
    }
  },
  computed: {
    tab() {
      return this.$route.query.tab ? this.$route.query.tab : 'tickets'
    }
  },
  methods: {
    setData(val) {
      this.data = val
      this.title = 'Order: '
    },
    tabChange(val) {
      this.$router.push({
        ...this.$route,
        name: this.$route.name,
        query: Object.assign({}, this.$route.query, {
          tab: val
        })
      })
    }
  }
}
</script>
