var path = require('path')
module.exports = {
    devServer: {
        port: 8080,
    },
    configureWebpack: {
        resolve: {
            alias: {
                '@': path.resolve(__dirname, 'src'),
            },
        },
    },
}
