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

export function getDepartments(parameter) {
  return axios({
    url: API.Department,
    method: 'get',
    params: parameter
  })
}

export function getDepartment(pk) {
  return axios({
    url: API.Department + `${pk}/`,
    method: 'get'
  })
}

export function createDepartment(data) {
  return axios({
    url: API.Department,
    method: 'post',
    data: data
  })
    .then(createSuccess)
    .catch(createFailed)
}

export function updateDepartment(pk, data) {
  return axios({
    url: API.Department + `${pk}/`,
    method: 'patch',
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed)
}

export function deleteDepartment(pk, data) {
  return axios({
    url: API.Department + `${pk}/`,
    method: 'delete'
  })
    .then(deleteSuccess)
    .catch(deleteFailed)
}
