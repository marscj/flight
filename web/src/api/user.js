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

export function getUsers(parameter) {
  return axios({
    url: API.User,
    method: 'get',
    params: parameter
  })
}

export function getUser(pk) {
  return axios({
    url: API.User + `${pk}/`,
    method: 'get'
  })
}

export function createUser(data) {
  return axios({
    url: API.User,
    method: 'post',
    data: data
  })
    .then(createSuccess)
    .catch(createFailed)
}

export function updateUser(pk, data) {
  return axios({
    url: API.User + `${pk}/`,
    method: 'patch', //'patch',
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed)
}

export function deleteUser(pk, data) {
  return axios({
    url: API.User + `${pk}/`,
    method: 'delete'
  })
    .then(deleteSuccess)
    .catch(deleteFailed)
}
