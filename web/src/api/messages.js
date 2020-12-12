import { API } from './index'
import { axios } from '@/utils/request'

export function getMessages(parameter) {
  return axios({
    url: API.Message,
    method: 'get',
    params: parameter
  })
}

export function getMessage(pk, parameter) {
  return axios({
    url: API.Message + `${pk}/`,
    params: parameter,
    method: 'get'
  })
}
