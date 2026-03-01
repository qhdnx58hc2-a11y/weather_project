/*
 * @Description: 
 * @Version: 2.0 
 * @Autor: LMJ
 * @Date: 2021-09-27 13:40:21
 * @LastEditors: LMJ
 * @LastEditTime: 2021-09-27 14:00:02
 */
module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ],
  'env': {
    'development': {
      'plugins': ['dynamic-import-node']
    }
  }
}
