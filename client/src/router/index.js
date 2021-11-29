import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
        children: [
            {
                path: 'search',
                props: true,
                name: 'SearchHome',
                component: () => import('@/views/SearchHomePage.vue'),
            },
            {
                path: 'searchresults',
                props: true,
                name: 'SearchResults',
                component: () =>
                    import('@/views/searchresults/SearchResults.vue'),
            },

            {
                path: 'analytics',
                props: true,
                name: 'Analytics',
                component: () => import('@/views/Analytics.vue'),
            },
        ],
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
})

export default router
