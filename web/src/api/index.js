import notification from 'ant-design-vue/es/notification'
import message from 'ant-design-vue/es/message'

export const API = {
  Login: '/auth/login/',
  Logout: '/auth/logout/',
  Register: '/auth/register',
  ChangePassword: '/auth/password/change/',
  UserInfo: '/auth/info/',
  User: '/users/',
  ResetPassword: pk => `/users/${pk}/reset_password/`,
  Role: '/roles/',
  Department: '/departments/',
  Booking: '/bookings/',
  BookingHistory: '/booking/histories/',
  Itinerary: '/itineraries/',
  ItineraryHistory: '/itinerary/histories/',
  Ticket: '/tickets/',
  TicketHistory: '/ticket/histories/'
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

export function LoginSuccess(res) {
  notification.success({
    message: 'Login Success'
  })
  return res
}

export function LoginFailed(error) {
  message.error('Login Failed!')
  throw error
}
