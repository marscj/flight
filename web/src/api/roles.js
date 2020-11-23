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

export function getRoles(parameter) {
  return axios({
    url: API.Roles,
    method: 'get',
    params: parameter
  })
}

export function getRole(pk) {
  return axios({
    url: API.Roles + `${pk}/`,
    method: 'get'
  })
}

export function createRole(data) {
  return axios({
    url: API.Roles,
    method: 'post',
    data: data
  })
    .then(createSuccess)
    .catch(createFailed)
}

export function updateRole(pk, data) {
  return axios({
    url: API.Roles + `${pk}/`,
    method: 'put',
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed)
}
