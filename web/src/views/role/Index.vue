<template>
  <form-validate ref="observer">
    <page-header-wrapper>
      <template slot="extra">
        <a-button v-action:change_group type="primary" @click="submit" :loading="updateing" html-type="submit">
          Submit
        </a-button>
      </template>
      <a-card class="card" title="Base Information" :bordered="false">
        <form-item-validate label="Name" vid="name">
          <a-input v-model="form.name" />
        </form-item-validate>
      </a-card>

      <a-card class="card" title="Passport" :bordered="false"> </a-card>
    </page-header-wrapper>
  </form-validate>
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import { getRole, updateRole } from '@/api/role'
import moment from 'moment'

export default {
  components: { FormValidate, FormItemValidate },

  data() {
    return {
      loading: false,
      updateing: false,
      form: {},
      extra: {}
    }
  },
  mounted() {
    this.getUserData()
  },
  methods: {
    getUserData() {
      this.loading = true
      getRole(this.$route.params.id)
        .then(res => {
          const { data, extra } = res.result

          this.form = Object.assign({}, data)

          this.extra = Object.assign({}, extra)
        })
        .finally(() => {
          this.loading = false
        })
    },
    submit() {
      this.updateing = true
      var form = Object.assign({}, this.form, {})
      updateRole(this.$route.params.id, form)
        .then(res => {
          const { data, extra } = res.result

          this.extra = extra
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.checkError(error)
          }
        })
        .finally(() => {
          this.updateing = false
        })
    }
  }
}
</script>

<style lang="less" scoped>
.card {
  margin-bottom: 24px;
}
.popover-wrapper {
  /deep/ .antd-pro-pages-forms-style-errorPopover .ant-popover-inner-content {
    min-width: 256px;
    max-height: 290px;
    padding: 0;
    overflow: auto;
  }
}
.antd-pro-pages-forms-style-errorIcon {
  user-select: none;
  margin-right: 24px;
  color: #f5222d;
  cursor: pointer;
  i {
    margin-right: 4px;
  }
}
.antd-pro-pages-forms-style-errorListItem {
  padding: 8px 16px;
  list-style: none;
  border-bottom: 1px solid #e8e8e8;
  cursor: pointer;
  transition: all 0.3s;

  &:hover {
    background: #e6f7ff;
  }
  .antd-pro-pages-forms-style-errorIcon {
    float: left;
    margin-top: 4px;
    margin-right: 12px;
    padding-bottom: 22px;
    color: #f5222d;
  }
  .antd-pro-pages-forms-style-errorField {
    margin-top: 2px;
    color: rgba(0, 0, 0, 0.45);
    font-size: 12px;
  }
}
</style>
