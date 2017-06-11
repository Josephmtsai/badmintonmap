import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import GMap from '@/components/GMap'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/map',
      name: 'GMap',
      component: GMap
    }
  ]
})
