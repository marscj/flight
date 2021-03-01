<template>
  <div>
    <a-list class="comment-list" itemLayout="horizontal" :dataSource="comments" :loading="loading">
      <a-list-item slot="renderItem" slot-scope="item">
        <a-comment
          v-if="item.user"
          :author="item.user.name"
          :avatar="item.user.avatar ? item.user.avatar.thumbnail : null"
        >
          <div slot="content">
            <p>{{ item.content }}</p>
          </div>
          <span slot="datetime">{{ item.date }}</span>
          <a @click="openModal(item)">Reply to</a>

          <div v-for="(child, index) in item.children" :key="child.id">
            <a-comment
              v-if="child.user"
              :author="child.user.name"
              :avatar="child.user.avatar ? child.user.avatar.thumbnail : null"
            >
              <div slot="content">
                <p class="pt-4">{{ child.content }}</p>
                <a-divider v-if="index < item.children.length - 1"></a-divider>
              </div>
              <span slot="datetime">{{ child.date }}</span>
            </a-comment>
          </div>
        </a-comment>
      </a-list-item>
    </a-list>
    <a-modal v-model="modal" title="Reply to" @ok="submit">
      <validation-observer ref="observer">
        <validation-provider name="non_field_errors" v-slot="{ errors }">
          <span class="errorText">{{ errors[0] }}</span>
        </validation-provider>

        <a-form :form="form">
          <a-form-item>
            <validation-provider vid="content" v-slot="{ errors }">
              <a-input v-model="form.content"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-form>
      </validation-observer>
    </a-modal>
  </div>
</template>

<script>
import { getComments, createComment } from '@/api/comment'
export default {
  data() {
    return {
      modal: false,
      form: {},
      loading: false,
      comments: undefined
    }
  },
  mounted() {
    this.getListData()
  },
  methods: {
    openModal(val) {
      this.form = {
        object_id: val.id
      }
      this.modal = true
    },
    getListData() {
      getComments({ object_id: this.$route.params.id, content_type: 'ticket' })
        .then(res => {
          this.comments = res.result.data
          console.log(this.comments)
        })
        .finally(() => {
          this.loading = false
        })
    },
    submit() {
      createComment({
        object_id: this.form.object_id,
        content_type: 'comment',
        user_id: this.$store.getters.userInfo.id,
        content: this.form.content,
        rating: null
      })
        .then(res => {
          this.modal = false
          return this.getListData()
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result)
          }
        })
    }
  }
}
</script>
