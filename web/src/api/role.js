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
    url: API.Role,
    method: 'get',
    params: parameter
  })
}

export function getRole(pk) {
  return axios({
    url: API.Role + `${pk}/`,
    method: 'get'
  })
}

export function createRole(data) {
  return axios({
    url: API.Role,
    method: 'post',
    data: data
  })
    .then(createSuccess)
    .catch(createFailed)
}

export function updateRole(pk, data) {
  return axios({
    url: API.Role + `${pk}/`,
    method: 'put',
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed)
}

export function deleteRole(pk, data) {
  return axios({
    url: API.Role + `${pk}/`,
    method: 'delete'
  })
    .then(deleteSuccess)
    .catch(deleteFailed)
}
