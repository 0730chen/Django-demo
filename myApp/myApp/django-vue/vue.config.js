module.exports = {
    publicPath: './',
    outputDir:'dist',
    assetsDir: 'static',
    devServer: {
     proxy: {
         '/allin': {
             //要访问的跨域的api的域名
             target: 'http://www.test.com/allin/policy',
             ws: true,
             secure:false, // 使用的是http协议则设置为false，https协议则设置为true
             changOrigin: true,
             pathRewrite: {
                 '^/allin': '/'  //必须这样写
             }
         }
     }
 }
}