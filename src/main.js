import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'


// import Chartkick from 'vue-chartkick'



// Vue.use(Chartkick.use(Chart))

createApp(App)
    .use(VueAxios, axios)
    .use(store)
    .use(router)
    .mount('#app')
