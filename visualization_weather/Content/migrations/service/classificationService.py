import json
import uuid

from django.http import JsonResponse

from Content.migrations.service import userService
from Content.models import Classification


#分页类表查询
def classification_list_service(request):
    # 解析请求中的JSON数据
    data = json.load(request)
    # 获取分页参数
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    # tuple
    # 获取可选的名字筛选参数（去除前后空格）
    _name = data.get('name', '').strip()
    # 查询未删除的分类列表，并根据名称筛选
    list = Classification.objects.filter(deleted=0, name__contains=_name)
    _list = []
    # 构建返回的数据列表
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['content'] = item.content
        rest['description'] = item.description
        rest['image'] = item.image
        # 格式化创建日期
        if item.createDate is not None:
            rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
        _list.append(rest)
        # 构建分页信息
    page = {
        "pageSize": _pageSize,
        "total": len(_list),
        "currentPage": _currentPage
    }
    # 分页处理
    if _pageSize < len(_list):
        if _pageSize * _currentPage > len(_list):
            _start = (_currentPage - 1) * _pageSize
            _list = _list[_start: len(_list)]
        if _pageSize * _currentPage <= len(_list):
            _start = (_currentPage - 1) * _pageSize
            _end = _currentPage * _pageSize
            _list = _list[_start: _end]
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "list": _list,
            "page": page,
        }
    }
    return JsonResponse(data1)
#分页添加服务
def classification_add_service(request):
    data = json.load(request);
    _user = userService.getCurrentUser(request)
    # 创建新的分类记录
    Classification.objects.create(
        uid=uuid.uuid4(),
        name=data['name'],
        content=data.get('content', ''),
        description=data.get('description', ''),
        image=data.get('image'),
    )
    # 构造成功响应
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)

#分类修改服务
def classification_modify_service(request):
    _user = userService.getCurrentUser(request)
    # 获取当前用户信息
    data = json.load(request)
    _uid = data['uid']
    # 查询要修改的分类是否存在
    rest = Classification.objects.filter(uid=_uid, deleted=0).first()
    # 如果分类不存在，返回错误响应
    if rest is None:
        data1 = {
            "success": "false",
            "message": "内容不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    # 更新分类信息
    Classification.objects.filter(uid=_uid).update(
        name=data['name'],
        content=data.get('content', ''),
        description=data.get('description', ''),
        image=data.get('image'),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def classification_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Classification.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "内容不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Classification.objects.filter(uid=_uid).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)

#分类删除信息
def classification_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Classification.objects.filter(uid=_uid, deleted=0).first()
    if item is None:
        data1 = {
            "success": "false",
            "message": "内容不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    rest = {}
    rest['id'] = item.id
    rest['uid'] = item.uid
    rest['name'] = item.name
    rest['content'] = item.content
    rest['description'] = item.description
    rest['image'] = item.image
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "rest": rest,
        }
    }
    return JsonResponse(data1)
