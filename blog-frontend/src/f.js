import { get, post, put, del } from './request.js';
// refreshData函数 作用域内
get('/api/blogs/')
    .then(response => {
        console.log('GET success：', response);
        refreshData();
    })
    .catch(error => {
        console.error('GET fail：', error);
    });

const postData = {
    title: 'New Blog Post',
    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
};
post('/api/blogs/', postData)
    .then(response => {
        console.log('POST success：', response);
        refreshData();
    })
    .catch(error => {
        console.error('POST fail：', error);
    });

