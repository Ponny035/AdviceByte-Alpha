// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import '../css/custom.css';
import VueRouter from 'vue-router'
import App from './App'
import Index from './components/index-avb' // component Foo
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/index', component: Index } 
    // { path: '/bar', component: Bar } 
  ]
})
new Vue({
  router,
  render: h => h(App) // Start component App.vue
}).$mount('#app')