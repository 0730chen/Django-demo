import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component:()=>import('../components/Rank.vue')
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/digital',
    name:'digital',
    component:()=>import('../components/rd-digital-flop.vue')
  },
  {
    path:'/time',
    name:'time',
    component:()=>import('../components/rd-time-flop.vue')
  },
  {
    path:'/Rank',
    name:'name',
    component:Home
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
