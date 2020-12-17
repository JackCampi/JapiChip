import vueRouter from 'vue-router'
import DocsEdit from './components/DocsEdit'
import App from './App'
import Home from './components/Home'

const router = new vueRouter({
        mode: 'history',
        base: __dirname,
        routes: [
            {
                path: '/',
                name: "root",
                component: App
            },
            {
                path: '/home/:email',
                name: "home",
                component: Home
            },
            {
                path: '/edit',
                name: "DocsEdit",
                component: DocsEdit
            },
        ]
    })

export default router