import { API, LoginFailed, LoginSuccess, updateSuccess, updateFailed } from './index'
import { axios } from '@/utils/request'

export function login(data) {
  return axios({
    url: API.Login,
    method: 'post',
    data: data
  })
    .then(LoginSuccess)
    .catch(LoginFailed)
}

export function getInfo() {
  return axios({
    url: API.UserInfo,
    method: 'get'
  })
}

export function updateInfo(data) {
  return axios({
    url: API.UserInfo,
    method: 'patch',
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed)
}

export function logout() {
  return axios({
    url: API.Logout,
    method: 'post'
  })
}
