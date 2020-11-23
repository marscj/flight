import { API } from './index'
import { axios } from '@/utils/request'

export function login(data) {
  return axios({
    url: API.Login,
    method: 'post',
    data: data
  })
}

export function getInfo() {
  return axios({
    url: API.UserInfo,
    method: 'get',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8'
    }
  })
}

export function getCurrentUserNav() {
  return axios({
    url: API.UserMenu,
    method: 'get'
  })
}

export function logout() {
  return axios({
    url: API.Logout,
    method: 'post',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8'
    }
  })
}
