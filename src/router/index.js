import { createRouter, createWebHistory } from 'vue-router'

import CenterContext from '../components/CenterContext.vue'
import Mission from '../components/Mission.vue'
import Stat from '../components/Stat.vue'
import Login from '../components/Login.vue'
import Dashboard from '../components/Dashboard.vue'
import getMission from '../components/components-view/getMission.vue'
import getDashboard from '../components/components-view/getDashboard.vue'
import Profile from '../components/components-view/Profile.vue'
// import Week from '../components/Week.vue';
import Charty from '../components/components-view/Chart.vue'
import getForum from '../components/getForum.vue'
import getGeneral from '../components/getGeneral.vue'
import Layout from '../components/Layout.vue'
import Register from '../components/Register.vue'
import Activity from '../components/Activity.vue'
import Response from '../components/Response.vue'

const guardAuth = async (to, from, next) => {
    if (localStorage.getItem('userId')) {
      next(); // TODO: implement token expire check
    } else {
      next({ name: 'Login' });
    }
  };

const routes = [

    {
        path: '/login',
        component: Login,
        name: 'Login'
    },
    {
        path: '/register',
        component: Register,
        name: ''
    },
    {
        path: '/',
        component: Layout,
        beforeEnter: guardAuth,
        children: [
            {
                path: '/activity/:id',
                component: Activity,
                name: 'activity-id',
            },
            {
                path: '',
                name: 'home',
                redirect: { name: 'profile'},
            },
            {
                path: '/chart',
                component: Charty,
                name: ''
            },
            {
                path: '/dashboard',
                component: Dashboard,
                meta: { test: '150' },
                name: 'dashboard',
                children: [
                    {
                        path: '',
                        component: getDashboard,
                        name: 'getDashboard',
                        meta: {},
                    },
                    {
                        path: '',
                        component: getForum,
                        name: '1'
                    },
                ]
            },
            {
                path: '/mission',
                component: Mission,
                name: 'mission',
                children: [
                    {
                        path: '',
                        component: getGeneral,
                        name: 'getGeneral',
                        meta: {}
                    },
                    {
                        path: ':id',
                        component: getMission,
                        name: 'algo',
                        meta: {}
                    }
                ]
            },
            {
                path: '/profile',
                component: CenterContext,
                meta: { test: '100' },
                name: 'main-view',
                children: [
                    {
                        path: '',
                        component: Profile,
                        name: 'profile',
                        meta: { displayTitle: 'Profile_Test' }
                    },
                    {
                        path: 'stat',
                        component: Stat,
                        name: 'stat',
                        meta: { displayTitle: 'Stat_Test' }
                    }
                ]
            },
            {
                path: '/response/:id',
                component: Response,
                name: 'response'
            }
        ]
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
