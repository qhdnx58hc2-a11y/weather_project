/*
 * @Description: 
 * @Version: 2.0
 * @Autor: LMJ
 * @Date: 2021-09-27 13:40:21
 * @LastEditors: LMJ
 * @LastEditTime: 2021-09-27 14:21:50
 */
import Vue from 'vue'
import 'normalize.css/normalize.css'
import '@/styles/index.scss'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import echarts from 'echarts'
Vue.prototype.$echarts = echarts 
import dataV from '@jiaminghi/data-view'
Vue.use(dataV)


Vue.use(ElementUI);

Vue.config.productionTip = false

Vue.prototype.$http = axios
axios.defaults.baseURL = 'http://127.0.0.1:8084'
import {
  getLocalStorage, setLocalStorage, getObjectLocalStorage, setObjectLocalStorage, removeLocalStorage
} from './storage/storage'

Vue.prototype.$getLocalStorage = getLocalStorage
Vue.prototype.$setLocalStorage = setLocalStorage
Vue.prototype.$getObjectLocalStorage = getObjectLocalStorage
Vue.prototype.$setObjectLocalStorage = setObjectLocalStorage
Vue.prototype.$removeLocalStorage = removeLocalStorage

export default new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

axios.interceptors.request.use(
  config => {
    if (sessionStorage.getItem('logintoken')) {
      config.headers.Authorization = sessionStorage.getItem('logintoken')
    }
    return config
  },
  function (error) {
    console.log(error)
    return Promise.reject(error)
  }
)