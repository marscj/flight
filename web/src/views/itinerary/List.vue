<template>
  <page-header-wrapper>
    <template slot="extra">
      <router-link v-action:view_itinerary :to="{ name: 'ItineraryHistory' }">
        <a-button type="primary">History</a-button>
      </router-link>
    </template>
    <a-card>
      <table-list />
    </a-card>
  </page-header-wrapper>
</template>

<script>
import TableList from './TableList'

export default {
  components: {
    TableList
  }
}
</script>
