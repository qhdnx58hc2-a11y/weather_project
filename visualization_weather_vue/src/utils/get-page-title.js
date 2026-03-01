/*
 * @Description: 
 * @Version: 2.0
 * @Autor: LMJ
 * @Date: 2021-09-27 13:58:54
 * @LastEditors: LMJ
 * @LastEditTime: 2021-09-27 13:58:55
 */
import defaultSettings from '@/settings'

const title = defaultSettings.title || 'Vue Admin Template'

export default function getPageTitle(pageTitle) {
  if (pageTitle) {
    return `${pageTitle} - ${title}`
  }
  return `${title}`
}
