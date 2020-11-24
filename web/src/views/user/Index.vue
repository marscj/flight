<template>
  <page-header-wrapper>
    <form-validate>
      <a-card class="card" title="Base" :bordered="false">
        <a-row class="form-row" :gutter="16">
          <a-col :lg="6" :md="12" :sm="24">
            <form-item-validate label="仓库名" vid="Email">
              <a-input placeholder="请输入仓库名称" />
            </form-item-validate>
          </a-col>
        </a-row>
      </a-card>

      <a-card class="card" title="Passport" :bordered="false"> </a-card>

      <a-card class="card" title="Role" :bordered="false"> </a-card>
    </form-validate>
  </page-header-wrapper>
</template>

<script>
import { FormItemValidate } from '@/components'
import FormValidate from '../../components/FormValidate/FormValidate.vue'
export default {
  components: { FormValidate, FormItemValidate },

  data() {
    return {
      loading: false,
      updateing: false,
      form: {},
      fileList: []
    }
  }
}
</script>

<style></style>
