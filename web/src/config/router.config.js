// eslint-disable-next-line
import { UserLayout, BasicLayout } from '@/layouts'
import { bxAnaalyse } from '@/core/icons'

const RouteView = {
  name: 'RouteView',
  render: h => h('router-view')
}

export const asyncRouterMap = [
  {
    path: '/',
    name: 'index',
    component: BasicLayout,
    meta: { title: 'menu.home' },
    redirect: '/dashboard/welcome',
    children: [
      // dashboard
      {
        path: '/dashboard',
        name: 'dashboard',
        redirect: '/dashboard/welcome',
        component: RouteView,
        meta: { title: 'menu.dashboard', keepAlive: true, icon: bxAnaalyse },
        children: [
          {
            path: '/dashboard/welcome',
            name: 'Welcome',
            component: () => import('@/views/dashboard/Welcome'),
            meta: { title: 'Welcome', keepAlive: true }
          }
        ]
      },
      {
        path: '/bookings',
        component: RouteView,
        meta: {
          title: 'Bookings',
          icon: 'safety',
          permission: ['view_booking', 'add_booking']
        },
        redirect: '/bookings/list',
        children: [
          {
            path: '/bookings/list',
            name: 'AllBookings',
            component: () => import('@/views/booking/List'),
            meta: {
              title: 'All Bookings',
              keepAlive: true,
              permission: ['view_booking']
            }
          },
          {
            path: '/booking/add',
            name: 'AddBooking',
            hidden: true,
            component: () => import('@/views/booking/Add'),
            meta: { title: 'Add Booking', permission: ['add_booking'] }
          },
          {
            path: '/bookings/:id/detail',
            name: 'BookingDetail',
            hidden: true,
            component: () => import('@/views/booking/Edit'),
            meta: {
              title: 'Booking Detail',
              permission: ['view_booking']
            }
          },
          {
            path: '/bookings/:id/history',
            name: 'BookingHistory',
            hidden: true,
            component: () => import('@/views/booking/History'),
            meta: {
              title: 'Booking History',
              permission: ['view_booking']
            }
          }
        ]
      },
      // user
      {
        path: '/users',
        name: 'Users',
        component: RouteView,
        redirect: '/users/list',
        meta: { title: 'Users', icon: 'team', permission: ['view_user'] },
        children: [
          {
            path: '/users/list/:pageNo([1-9]\\d*)?',
            name: 'AllUser',
            hideChildrenInMenu: false, // 强制显示 MenuItem 而不是 SubMenu
            component: () => import('@/views/user/List'),
            meta: { title: 'All Users', keepAlive: true }
          },
          {
            path: '/users/:id',
            name: 'UserDetail',
            hidden: true,
            hideChildrenInMenu: true,
            component: () => import('@/views/user/Index'),
            meta: {
              title: 'User Detail'
            }
          }
        ]
      },
      {
        path: '/departments',
        component: RouteView,
        meta: {
          title: 'Departments',
          icon: 'safety',
          permission: ['view_department']
        },
        redirect: '/departments/list',
        children: [
          {
            path: '/departments/list',
            name: 'AllDepartments',
            component: () => import('@/views/department/List'),
            meta: { title: 'All Departments', keepAlive: true }
          },
          {
            path: '/departments/:id',
            name: 'DepartmentDetail',
            hidden: true,
            hideChildrenInMenu: true,
            component: () => import('@/views/department/Index'),
            meta: {
              title: 'Department Detail'
            }
          }
        ]
      },
      {
        path: '/roles',
        component: RouteView,
        meta: { title: 'Roles', icon: 'safety', permission: ['view_group'] },
        redirect: '/roles/list',
        children: [
          {
            path: '/roles/list',
            name: 'AllRoles',
            component: () => import('@/views/role/List'),
            meta: { title: 'All Roles', keepAlive: true }
          },
          {
            path: '/roles/:id',
            name: 'RoleDetail',
            hidden: true,
            hideChildrenInMenu: true,
            component: () => import('@/views/role/Index'),
            meta: {
              title: 'Role Detail'
            }
          }
        ]
      }
    ]
  },
  {
    path: '*',
    redirect: '/404',
    hidden: true
  }
]

/**
 * 基础路由
 * @type { *[] }
 */
export const constantRouterMap = [
  {
    path: '/user',
    component: UserLayout,
    redirect: '/user/login',
    hidden: true,
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import(/* webpackChunkName: "user" */ '@/views/user/Login')
      },
      {
        path: 'recover',
        name: 'recover',
        component: undefined
      }
    ]
  },

  {
    path: '/404',
    name: '404',
    component: () => import(/* webpackChunkName: "fail" */ '@/views/exception/404')
  },
  {
    path: '/500',
    name: '500',
    component: () => import(/* webpackChunkName: "fail" */ '@/views/exception/500')
  }
]
