/**
 * Created by zm on 17/11/06.
 *
 * templete封装
 *
 */
 import axios from "axios";
//  axios.defaults.baseURL = 'http://124.220.178.50:8084'
 axios.defaults.baseURL = 'http://127.0.0.1:8084'

export async function exportTempletes(path, param, fileName) {    
  const fullpath =  axios.defaults.baseURL + path;
  console.log("exportFileRequest fullpath", fullpath)
  await axios({
    method: 'post',
    url: fullpath, // 请求地址
    data: param, // 参数
    responseType: 'blob', // 表明返回服务器返回的数据类型
    headers: {
      // 'Content-Type': 'application/json'
    }
  }).then(response => {
    let blob = new Blob([response.data],{type:'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'});
    let url = window.URL.createObjectURL(blob);
    let link = document.createElement('a');
    link.style.display = 'none';
    link.href = url
    link.setAttribute('download',fileName);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
  });
}

