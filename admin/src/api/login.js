import request from '@/utils/request'

const userApi = {
  Login: '/auth/login/',
  Logout: '/auth/logout/',
  Register: '/auth/register',
  UserInfo: '/auth/info/',
}

/**
 * login func
 * parameter: {
 *     username: '',
 *     password: '',
 *     remember_me: true,
 *     captcha: '12345'
 * }
 * @param parameter
 * @returns {*}
 */
export function login(data) {
  return request({
    url: userApi.Login,
    method: 'post',
    data: data,
  })
}

export function getInfo() {
  return request({
    url: userApi.UserInfo,
    method: 'get',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8',
    },
  })
}

export function getCurrentUserNav() {
  return request({
    url: userApi.UserMenu,
    method: 'get',
  })
}

export function logout() {
  return request({
    url: userApi.Logout,
    method: 'post',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8',
    },
  })
}
