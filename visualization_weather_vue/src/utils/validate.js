/**
 * Created by PanJiaChen on 16/11/18.
 */

/**
 * @param {string} path
 * @returns {Boolean}
 */
export function isExternal(path) {
  return /^(https?:|mailto:|tel:)/.test(path);
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validUsername(str) {
  const valid_map = ["admin", "editor"];
  return valid_map.indexOf(str.trim()) >= 0;
}

/* 是否手机号码*/
export function validatePhone(rule, value, callback) {
  const reg = /^[1][3,4,5,7,8][0-9]{9}$/;
  if (value === "" || value === undefined || value == null) {
    callback();
  } else {
    if (!reg.test(value) && value !== "") {
      callback(new Error("请输入正确的手机号码"));
    } else {
      callback();
    }
  }
}

