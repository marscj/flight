import { asyncRouterMap, constantRouterMap } from '@/config/router.config'

/**
 * 过滤账户是否拥有某一个权限，并将菜单从加载列表移除
 *
 * @param permission
 * @param route
 * @returns {boolean}
 */
function hasPermission(permission, route) {
  if (route.meta && route.meta.permission) {
    let flag = false
    for (let i = 0, len = permission.length; i < len; i++) {
      flag = route.meta.permission.includes(permission[i].codename)
      if (flag) {
        return true
      }
    }
    return false
  }
  return true
}

export function hasRole(roles) {
  if (roles) {
    return roles
      .reduce((f1, f2) => f1.concat(f2.permissions), [])
      .filter(f => {
        return f
      })
  }
  return []
}

function filterAsyncRouter(routerMap, roles) {
  const accessedRouters = routerMap.filter(route => {
    if (hasPermission(roles, route)) {
      if (route.children && route.children.length) {
        route.children = filterAsyncRouter(route.children, roles)
      }
      return true
    }
    return false
  })
  return accessedRouters
}

export const permission = {
  state: {
    routers: constantRouterMap,
    addRouters: []
  },
  mutations: {
    SET_ROUTERS: (state, routers) => {
      state.addRouters = routers
      state.routers = constantRouterMap.concat(routers)
    }
  },
  actions: {
    GenerateRoutes({ commit }, data) {
      return new Promise((resolve, reject) => {
        var superuser = data.is_superuser
        if (superuser) {
          commit('SET_ROUTERS', asyncRouterMap)
        } else {
          var roles = data.roles
          const _roles = hasRole(roles)
          const accessedRouters = filterAsyncRouter(asyncRouterMap, _roles)
          commit('SET_ROUTERS', accessedRouters)
        }
        resolve()
      })
    }
  }
}

export default permission
