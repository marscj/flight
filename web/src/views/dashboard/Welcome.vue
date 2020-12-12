<template>
  <page-header-wrapper>
    <template v-slot:title> Welcome {{ timeFix }} </template>
    <template v-slot:content>
      <div class="page-header-content">
        <div class="avatar">
          <a-avatar size="large" :src="currentUser.avatar" />
        </div>
        <div class="content">
          <div class="content-title">{{ user.name }}</div>
          <span>{{ user.department }}</span>
        </div>
      </div>
    </template>
    <template v-slot:extraContent>
      <div class="extra-content">
        <div class="stat-item">
          <a-statistic title="项目数" :value="56" />
        </div>
        <div class="stat-item">
          <a-statistic title="团队内排名" :value="8" suffix="/ 24" />
        </div>
        <div class="stat-item">
          <a-statistic title="项目访问" :value="2223" />
        </div>
      </div>
    </template>

    <div>
      <a-row :gutter="24">
        <a-col :xl="16" :lg="24" :md="24" :sm="24" :xs="24">
          <a-card :loading="loading" title="Messages" :bordered="false">
            <a-list>
              <a-list-item :key="index" v-for="(item, index) in messages">
                <a-list-item-meta>
                  <div slot="title">
                    <router-link
                      v-if="item.model == 'Booking'"
                      :to="{ name: 'BookingDetail', params: { id: item.model_id } }"
                    >
                      <span>{{ item.json }}</span>
                    </router-link>
                    <router-link
                      v-else-if="item.model == 'Ticket'"
                      :to="{ name: 'TicketDetail', params: { id: item.model_id } }"
                    >
                      <span>{{ item.json }}</span>
                    </router-link>
                    <router-link v-if="item.model == 'Itinerary'" :to="{ name: 'BookingDetail', params: { id: 1 } }">
                      <span>{{ item.json['booking'] }}</span>
                    </router-link>
                  </div>
                  <div slot="description">{{ item.json['history_date'] | moment }}</div>
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </a-card>
        </a-col>
        <a-col style="padding: 0 12px" :xl="8" :lg="24" :md="24" :sm="24" :xs="24">
          <a-card title="Navigation" style="margin-bottom: 24px" :bordered="false" :body-style="{ padding: 0 }">
            <div class="item-group">
              <router-link :to="{ name: 'AllBookings' }" v-action:view_booking> Bookings </router-link>
              <router-link :to="{ name: 'AllItineraries' }" v-action:view_itinerary> Itineraries </router-link>
              <router-link :to="{ name: 'AllTickets' }" v-action:view_ticket> Tickets </router-link>
              <router-link :to="{ name: 'AllUsers' }" v-action:view_user> Users </router-link>
            </div>
          </a-card>
        </a-col>
      </a-row>
    </div>
  </page-header-wrapper>
</template>

<script>
import { timeFix } from '@/utils/util'
import { mapState } from 'vuex'
import { getMessages } from '@/api/messages'

const DataSet = require('@antv/data-set')

export default {
  name: 'Welcome',
  components: {},
  data() {
    return {
      timeFix: timeFix(),
      avatar: '',
      user: {},

      projects: [],
      loading: true,
      messages: [],
      activities: []
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.user.info,
      welcome: state => state.user.welcome
    }),
    userInfo() {
      return this.$store.getters.userInfo
    }
  },
  created() {
    this.user = this.userInfo
    this.avatar = this.userInfo.avatar
  },
  mounted() {
    this.getMessageData()
  },
  methods: {
    getMessageData() {
      this.loading = true
      getMessages()
        .then(res => {
          this.messages = Object.assign(
            [],
            res.result.map(f => {
              f.json = JSON.parse(f.json)
              return f
            })
          )
        })
        .finally(() => (this.loading = false))
    }
  }
}
</script>

<style lang="less" scoped>
@import './Welcome.less';

.project-list {
  .card-title {
    font-size: 0;

    a {
      color: rgba(0, 0, 0, 0.85);
      margin-left: 12px;
      line-height: 24px;
      height: 24px;
      display: inline-block;
      vertical-align: top;
      font-size: 14px;

      &:hover {
        color: #1890ff;
      }
    }
  }

  .card-description {
    color: rgba(0, 0, 0, 0.45);
    height: 44px;
    line-height: 22px;
    overflow: hidden;
  }

  .project-item {
    display: flex;
    margin-top: 8px;
    overflow: hidden;
    font-size: 12px;
    height: 20px;
    line-height: 20px;

    a {
      color: rgba(0, 0, 0, 0.45);
      display: inline-block;
      flex: 1 1 0;

      &:hover {
        color: #1890ff;
      }
    }

    .datetime {
      color: rgba(0, 0, 0, 0.25);
      flex: 0 0 auto;
      float: right;
    }
  }

  .ant-card-meta-description {
    color: rgba(0, 0, 0, 0.45);
    height: 44px;
    line-height: 22px;
    overflow: hidden;
  }
}

.item-group {
  padding: 20px 0 8px 24px;
  font-size: 0;

  a {
    color: rgba(0, 0, 0, 0.65);
    display: inline-block;
    font-size: 14px;
    margin-bottom: 13px;
    width: 25%;
  }
}

.members {
  a {
    display: block;
    margin: 12px 0;
    line-height: 24px;
    height: 24px;

    .member {
      font-size: 14px;
      color: rgba(0, 0, 0, 0.65);
      line-height: 24px;
      max-width: 100px;
      vertical-align: top;
      margin-left: 12px;
      transition: all 0.3s;
      display: inline-block;
    }

    &:hover {
      span {
        color: #1890ff;
      }
    }
  }
}

.mobile {
  .project-list {
    .project-card-grid {
      width: 100%;
    }
  }

  .more-info {
    border: 0;
    padding-top: 16px;
    margin: 16px 0 16px;
  }

  .headerContent .title .welcome-text {
    display: none;
  }
}
</style>
