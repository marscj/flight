import {
  API,
  updateSuccess,
  createSuccess,
  deleteSuccess,
  deleteFailed,
  createFailed,
  updateFailed,
  uploadSuccess,
  uploadFailed
} from './index'
import { axios } from '@/utils/request'

export function getBookings(parameter) {
  return axios({
    url: API.Booking,
    method: 'get',
    params: parameter
  })
}

export function getBooking(pk, parameter) {
  return axios({
    url: API.Booking + `${pk}/`,
    params: parameter,
    method: 'get'
  })
}

export function createBooking(data) {
  return axios({
    url: API.Booking,
    method: 'post',
    data: data
  })
    .then(createSuccess)
    .catch(createFailed)
}

export function updateBooking(pk, data) {
  return axios({
    url: API.Booking + `${pk}/`,
    method: 'patch',
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed)
}

export function deleteBooking(pk, data) {
  return axios({
    url: API.Booking + `${pk}/`,
    method: 'delete'
  })
    .then(deleteSuccess)
    .catch(deleteFailed)
}

export function getBookingHistories(parameter) {
  return axios({
    url: API.BookingHistory,
    method: 'get',
    params: parameter
  })
}

export function getHistory(pk, parameter) {
  return axios({
    url: API.BookingHistory + `${pk}/`,
    params: parameter,
    method: 'get'
  })
}
