const BundleTracker = require('webpack-bundle-tracker')

// Change this to match the path to your files in production (could be S3, CloudFront, etc.)
const DEPLOYMENT_PATH = '/static/dist/'

module.exports = {
  publicPath: 'http://127.0.0.1:8080/',
  outputDir: './dist/',

  devServer: {
    client: {
      // Can be `string`:
      //
      // To get protocol/hostname/port from browser
      // webSocketURL: 'auto://0.0.0.0:0/ws'
      webSocketURL: {
        hostname: "127.0.0.1",
        pathname: "http",
        port: 8080,
      },
    },
    host: '127.0.0.1',
    port: 8080,
    hot: true,
    https: false,
    headers: {
      'Access-Control-Allow-Origin': '\*',
    },
  },

  configureWebpack: {
    plugins: [
      new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
    ],
  },
}