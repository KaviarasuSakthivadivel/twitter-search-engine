import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './css/index.css'
import './scss/common-styles.scss'
import InlineSvg from './components/InlineSvg'
import locale from 'element-ui/lib/locale/lang/en'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import _ from 'lodash'
import axios from './helpers/axios'
import Charts from './components/Charts'
import moment from 'moment'

Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount('#app')
Vue.use(Element, { locale })
Vue.component('InlineSvg', InlineSvg)

Object.defineProperty(Vue.prototype, '$_', { value: _ })
Object.defineProperty(Vue.prototype, '$axios', { value: axios })

Vue.component('TwCharts', Charts)
Vue.prototype.moment = moment
