import notification from 'ant-design-vue/es/notification'
import message from 'ant-design-vue/es/message'

export const API = {
  Login: '/auth/login/',
  Logout: '/auth/logout/',
  Register: '/auth/register',
  UserInfo: '/auth/info/',
  Users: '/users/'
}

export function updateSuccess(res) {
  notification.success({
    message: 'Update Success'
  })
  return res
}

export function updateFailed(error) {
  message.error('Update Failed!')
  throw error
}

export function createSuccess(res) {
  notification.success({
    message: 'Create Success'
  })
  return res
}

export function createFailed(error) {
  message.error('Create Failed!')
  throw error
}

export function uploadSuccess(res) {
  notification.success({
    message: 'Upload Success'
  })
  return res
}

export function uploadFailed(error) {
  message.error('Upload Failed!')
  throw error
}

export function deleteSuccess(res) {
  notification.success({
    message: 'Delete Success'
  })
  return res
}

export function deleteFailed(error) {
  message.error('Delete Failed!')
  throw error
}
