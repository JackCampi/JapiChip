import vueRouter from 'vue-router'
import DocsEdit from './components/DocsEdit'
import App from './App'

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
                path: '/edit',
                name: "DocsEdit",
                component: DocsEdit
            },
        ]
    })

export default router