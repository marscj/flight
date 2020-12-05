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
        name: 'Bookings',
        component: RouteView,
        redirect: '/bookings/list',
        meta: {
          title: 'Bookings',
          icon: 'safety',
          permission: ['view_booking', 'add_booking']
        },
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
      {
        path: '/tickets',
        component: RouteView,
        meta: {
          title: 'Tickets',
          icon: 'safety',
          permission: ['view_ticket', 'add_ticket']
        },
        redirect: '/tickets/list',
        children: [
          {
            path: '/tickets/list',
            name: 'AllTickets',
            component: () => import('@/views/ticket/List'),
            meta: {
              title: 'All Tickets',
              keepAlive: true,
              permission: ['view_ticket']
            }
          },
          {
            path: '/ticket/add',
            name: 'AddTicket',
            hidden: true,
            component: () => import('@/views/ticket/Add'),
            meta: { title: 'Add Ticket', permission: ['add_ticket'] }
          },
          {
            path: '/tickets/:id/detail',
            name: 'TicketDetail',
            hidden: true,
            component: () => import('@/views/ticket/Edit'),
            meta: {
              title: 'Ticket Detail',
              permission: ['view_ticket']
            }
          },
          {
            path: '/tickets/:id/history',
            name: 'TicketHistory',
            hidden: true,
            component: () => import('@/views/ticket/History'),
            meta: {
              title: 'Ticket History',
              permission: ['view_ticket']
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
        meta: { title: 'Users', icon: 'team', permission: ['view_user', 'add_user'] },
        children: [
          {
            path: '/users/list',
            name: 'AllUser',
            component: () => import('@/views/user/List'),
            meta: { title: 'All Users', keepAlive: true, permission: ['view_user'] }
          },
          {
            path: '/users/add',
            name: 'AddUser',
            component: () => import('@/views/user/Add'),
            meta: { title: 'Add User', permission: ['add_user'] }
          },
          {
            path: '/users/:id/detail',
            name: 'UserDetail',
            hidden: true,
            component: () => import('@/views/user/Edit'),
            meta: {
              title: 'User Detail',
              permission: ['view_user']
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
          permission: ['view_department', 'add_department']
        },
        redirect: '/departments/list',
        children: [
          {
            path: '/departments/list',
            name: 'AllDepartments',
            component: () => import('@/views/department/List'),
            meta: { title: 'All Departments', keepAlive: true, permission: ['view_department'] }
          },
          {
            path: '/roles/add',
            name: 'AddDepartment',
            component: () => import('@/views/department/Add'),
            meta: { title: 'Add Department', permission: ['add_department'] }
          },
          {
            path: '/departments/:id/detail',
            name: 'DepartmentDetail',
            hidden: true,
            hideChildrenInMenu: true,
            component: () => import('@/views/department/Edit'),
            meta: {
              title: 'Department Detail',
              permission: ['view_department']
            }
          }
        ]
      },
      {
        path: '/roles',
        component: RouteView,
        meta: { title: 'Roles', icon: 'safety', permission: ['view_group', 'add_group'] },
        redirect: '/roles/list',
        children: [
          {
            path: '/roles/list',
            name: 'AllRoles',
            component: () => import('@/views/role/List'),
            meta: { title: 'All Roles', keepAlive: true, permission: ['view_group'] }
          },
          {
            path: '/roles/add',
            name: 'AddRole',
            component: () => import('@/views/role/Add'),
            meta: { title: 'Add Role', permission: ['add_group'] }
          },
          {
            path: '/roles/:id/detail',
            name: 'RoleDetail',
            hidden: true,
            hideChildrenInMenu: true,
            component: () => import('@/views/role/Edit'),
            meta: {
              title: 'Role Detail',
              permission: ['view_group']
            }
          }
        ]
      },
      {
        path: '/account',
        component: RouteView,
        redirect: '/account/settings',
        meta: { title: 'Account', icon: 'user' },
        hidden: true,
        hideChildrenInMenu: true,
        children: [
          {
            path: '/account/settings',
            name: 'settings',
            hidden: true,
            component: () => import('@/views/user/Profile'),
            meta: { title: 'User Profile' }
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
