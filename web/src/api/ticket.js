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

export function getTickets(parameter) {
  return axios({
    url: API.Ticket,
    method: 'get',
    params: parameter
  })
}

export function getTicket(pk, parameter) {
  return axios({
    url: API.Ticket + `${pk}/`,
    params: parameter,
    method: 'get'
  })
}

export function createTicket(data) {
  return axios({
    url: API.Ticket,
    method: 'post',
    data: data
  })
    .then(createSuccess)
    .catch(createFailed)
}

export function updateTicket(pk, data) {
  return axios({
    url: API.Ticket + `${pk}/`,
    method: 'patch',
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed)
}

export function deleteTicket(pk, data) {
  return axios({
    url: API.Ticket + `${pk}/`,
    method: 'delete'
  })
    .then(deleteSuccess)
    .catch(deleteFailed)
}

export function getTicketHistories(parameter) {
  return axios({
    url: API.TicketHistory,
    method: 'get',
    params: parameter
  })
}
