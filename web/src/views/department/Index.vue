<template>
  <form-validate ref="observer">
    <page-header-wrapper>
      <a-card class="card" title="Base Information" :bordered="false">
        <form-item-validate label="Name" vid="name" required>
          <a-input v-model="form.name" :disabled="disabled()" />
        </form-item-validate>
      </a-card>
    </page-header-wrapper>

    <a-row v-if="post_type == 'edit'">
      <a-col :span="12">
        <a-popconfirm
          title="Are you sure delete?"
          @confirm="onDelete"
          okText="Yes"
          cancelText="No"
          v-if="$auth('delete_department')"
        >
          <a-button href="javascript:;" type="danger">Delete</a-button>
        </a-popconfirm>
      </a-col>

      <a-col :span="12" class="text-right">
        <a-button v-action:change_department type="primary" @click="submit" :loading="updateing" html-type="submit">
          Submit
        </a-button>
      </a-col>
    </a-row>

    <a-row v-if="post_type == 'add'">
      <a-col :span="24" class="text-right">
        <a-button v-action:add_department type="primary" @click="submit" :loading="updateing" html-type="submit">
          Submit
        </a-button>
      </a-col>
    </a-row>
  </form-validate>
</template>

<script>
import { FormValidate, FormItemValidate } from '@/components'
import { getDepartment, updateDepartment, deleteDepartment, createDepartment } from '@/api/department'

export default {
  components: { FormValidate, FormItemValidate },
  props: {
    post_type: {
      type: String,
      default: 'edit'
    }
  },
  data() {
    return {
      loading: false,
      updateing: false,
      disabled: () => {
        if (this.post_type == 'add' && this.$auth('add_department')) {
          return false
        }

        if (this.post_type == 'edit' && this.$auth('change_department')) {
          return false
        }

        return true
      },
      form: {}
    }
  },
  mounted() {
    if (this.post_type == 'edit') this.getDepartmentData()
  },
  methods: {
    getDepartmentData() {
      this.loading = true
      getDepartment(this.$route.params.id)
        .then(res => {
          const { result } = res
          this.form = Object.assign({}, result)
        })
        .finally(() => {
          this.loading = false
        })
    },
    submit() {
      this.updateing = true
      var form = Object.assign({}, this.form, {})

      if (this.post_type == 'edit') {
        updateDepartment(this.$route.params.id, form)
          .then(res => {
            const { result } = res
          })
          .catch(error => {
            if (error.response) {
              this.$refs.observer.setErrors(error)
            }
          })
          .finally(() => {
            this.updateing = false
          })
      } else if (this.post_type == 'add') {
        createDepartment(form)
          .then(res => {
            this.$router.replace({
              name: 'DepartmentDetail',
              params: { id: res.result.id }
            })
          })
          .catch(error => {
            if (error.response) {
              this.$refs.observer.setErrors(error)
            }
          })
          .finally(() => {
            this.updateing = false
          })
      }
    },
    onDelete() {
      this.updateing = true
      deleteDepartment(this.$route.params.id)
        .then(() => {
          this.$router.go(-1)
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
</style>
