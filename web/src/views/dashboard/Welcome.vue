<template>
  <page-header-wrapper>
    <template v-slot:title> Welcome {{ timeFix }} </template>
    <template v-slot:content>
      <div class="page-header-content">
        <a-avatar size="large" icon="user" :src="currentUser.avatar.thumbnail" alt="center" />
        <div class="content">
          <div class="content-title">{{ user.name }}</div>
          <span>{{ user.department }}</span>
        </div>
      </div>
    </template>
    <!-- <template v-slot:extraContent>
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
    </template> -->

    <div>
      <a-row :gutter="24">
        <a-col :xl="16" :lg="24" :md="24" :sm="24" :xs="24">
          <a-card
            :loading="loading"
            title="Messages"
            :bordered="false"
            :tab-list="tabList"
            @tabChange="
              key => {
                if (key == 'today') {
                  today()
                } else if (key == 'yesterday') {
                  yesterday()
                } else {
                  week()
                }
              }
            "
          >
            <a-list item-layout="vertical" size="large" :pagination="{ pageSize: 10 }" :data-source="messages">
              <a-list-item slot="renderItem" :key="index" slot-scope="data, index">
                <a-list-item-meta>
                  <div slot="title">
                    <template v-if="data.json['model'] == 'Booking'">
                      <!-- <a-avatar slot="avatar" icon="user" :src="item.user.avatar" /> -->
                      <span>{{ data.json['history_user'] }} </span>
                      <span>{{ actionString[data.json['history_type']] }}</span>
                      <router-link
                        v-if="data.json['history_type'] == '-'"
                        :to="{ name: 'BookingHistory', params: { id: data.json['id'] } }"
                      >
                        Booking for ID:{{ data.json['id'] }}
                      </router-link>
                      <router-link v-else :to="{ name: 'BookingDetail', params: { id: data.json['id'] } }">
                        Booking for ID:{{ data.json['id'] }}
                      </router-link>
                      <a-icon type="inbox" v-if="!data.read"> </a-icon>
                    </template>
                    <template v-if="data.json['model'] == 'Ticket'">
                      <span>{{ data.json['history_user'] }} </span>
                      <span>{{ actionString[data.json['history_type']] }}</span>
                      <router-link
                        v-if="data.json['history_type'] == '-'"
                        :to="{ name: 'TicketHistory', params: { id: data.json['id'] } }"
                      >
                        Ticket for ID:{{ data.json['id'] }}
                      </router-link>
                      <router-link v-else :to="{ name: 'TicketDetail', params: { id: data.json['id'] } }">
                        Ticket for ID:{{ data.json['id'] }}
                      </router-link>
                      <a-icon type="inbox" v-if="!data.read"> </a-icon>
                    </template>
                    <template v-if="data.json['model'] == 'Itinerary'">
                      <span>{{ data.json['history_user'] }} </span>
                      <span>{{ actionString[data.json['history_type']] }}</span>
                      <router-link
                        v-if="data.json['history_type'] == '-'"
                        :to="{ name: 'ItineraryHistory', params: { id: data.json['booking'] } }"
                      >
                        Itinerary for ID:{{ data.json['id'] }}
                      </router-link>
                      <router-link v-else :to="{ name: 'BookingDetail', params: { id: data.json['booking'] } }">
                        Itinerary for ID:{{ data.json['id'] }}
                      </router-link>
                      <a-icon type="inbox" v-if="!data.read"> </a-icon>
                    </template>
                    <template v-if="data.json['model'] == 'Comment'">
                      <span>{{ data.json['message'] }} </span>
                      <router-link :to="{ name: 'TicketDetail', params: { id: data.json['id'] } }">
                        Ticket for ID:{{ data.json['id'] }}
                      </router-link>
                      <a-icon type="inbox" v-if="!data.read"> </a-icon>
                    </template>
                  </div>
                  <div slot="description">{{ data.date | moment }}</div>
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
import moment from 'moment'

const ActionString = {
  '+': 'Added',
  '~': 'Changed',
  '-': 'Deleted'
}

export default {
  name: 'Welcome',
  components: {},
  data() {
    return {
      actionString: ActionString,
      timeFix: timeFix(),
      avatar: '',
      user: {},
      queryParams: {},
      tabList: [
        {
          key: 'today',
          tab: 'Today'
        },
        {
          key: 'yesterday',
          tab: 'Yesterday'
        },
        {
          key: 'last_week',
          tab: 'Last Week'
        }
      ],
      loading: true,
      messages: []
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
    this.today()
  },
  methods: {
    today() {
      return this.getMessageData({
        date: moment().format('YYYY-MM-DD')
      })
    },
    yesterday() {
      return this.getMessageData({
        date: moment()
          .add(-1, 'days')
          .format('YYYY-MM-DD')
      })
    },
    week() {
      return this.getMessageData({
        week_after: moment()
          .add(-7, 'days')
          .format('YYYY-MM-DD'),
        week_before: moment().format('YYYY-MM-DD')
      })
    },
    getMessageData(queryParams) {
      this.loading = true
      getMessages(queryParams)
        .then(res => {
          this.messages = Object.assign([], res.result)
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
