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

export function getItineraries(parameter) {
  return axios({
    url: API.Itinerary,
    method: 'get',
    params: parameter
  })
}

export function getItinerary(pk, parameter) {
  return axios({
    url: API.Itinerary + `${pk}/`,
    params: parameter,
    method: 'get'
  })
}

export function createItinerary(data) {
  return axios({
    url: API.Itinerary,
    method: 'post',
    data: data
  })
    .then(createSuccess)
    .catch(createFailed)
}

export function updateItinerary(pk, data) {
  return axios({
    url: API.Itinerary + `${pk}/`,
    method: 'patch',
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed)
}

export function deleteItinerary(pk, data) {
  return axios({
    url: API.Itinerary + `${pk}/`,
    method: 'delete'
  })
    .then(deleteSuccess)
    .catch(deleteFailed)
}
