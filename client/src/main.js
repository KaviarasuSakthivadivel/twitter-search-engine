import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './index.css'
import SvgLoader from './components/SvgLoader.vue'
import InlineSvg from 'vue-inline-svg'

const app = createApp(App)
app.use(ElementPlus)
app.component('SvgLoader', SvgLoader)
app.component('InlineSvg', InlineSvg)
app.mount('#app')
