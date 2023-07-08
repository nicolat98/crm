import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import HomeView from '../views/HomeView.vue'

import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Leads from '../views/dashboard/Leads'
import Lead from '../views/dashboard/Lead'
import AddLead from '../views/dashboard/AddLead'
import EditLead from '../views/dashboard/EditLead'
import AddTeam from '../views/dashboard/AddTeam'
import Team from '../views/dashboard/Team'
import AddMember from '../views/dashboard/AddMember'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta:{
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta:{
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/leads',
    name: 'Leads',
    component: Leads,
    meta:{
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/leads/:id',
    name: 'Lead',
    component: Lead,
    meta:{
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/leads/add',
    name: 'AddLead',
    component: AddLead,
    meta:{
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/leads/:id/edit',
    name: 'EditLead',
    component: EditLead,
    meta:{
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/add-team',
    name: 'AddTeam',
    component: AddTeam,
    meta:{
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/team',
    name: 'Team',
    component: Team,
    meta:{
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/team/add-member/',
    name: 'AddMember',
    component: AddMember,
    meta:{
      requiredLogin: true
    }
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to,from,next) => {
  if (to.matched.some(record => record.meta.requiredLogin) && !store.state.isAuthenticated){
    next('/log-in')
  }else{
    next()
  }
})

export default router
