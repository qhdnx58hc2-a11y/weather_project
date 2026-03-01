//获取
export function getLocalStorage(key){
    return localStorage.getItem(key);
}
//保存
export function setLocalStorage(key,value){
    localStorage.setItem(key,value);
}
//获取
export function getObjectLocalStorage(key){
    return JSON.parse(localStorage.getItem(key));
}
//保存
export function setObjectLocalStorage(key,value){
    localStorage.setItem(key,JSON.stringify(value));
}
//删除
export function removeLocalStorage(key){
    localStorage.removeItem(key)
}



