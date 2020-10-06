import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'


// import Chartkick from 'vue-chartkick'




// Vue.use(Chartkick.use(Chart))

createApp(App)
    .use(store)
    .use(router)
    .mount('#app')
