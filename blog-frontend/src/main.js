import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router.js'
import 'element-plus/theme-chalk/index.css'
// createApp(App).use(router).mount('#app')

// 这里定义refreshData函数
function refreshData() {
    console.log('Refreshing data...');
}


document.addEventListener('DOMContentLoaded', () => {
    const app = createApp(App) //实例
    app.use(router).mount('#app') //挂载
    refreshData();
    // catch error
    app.config.errorHandler = (err, vm, info) => {
        console.error('Vue Error:', err, info);
    };
});
