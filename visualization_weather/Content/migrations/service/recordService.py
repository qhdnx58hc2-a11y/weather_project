import datetime
import json
import uuid
from django.http import JsonResponse
from Content.models import Record


def record_list_service(request):
    _pageSize = 10
    _currentPage = 1
    list = Record.objects.filter(deleted=0)
    _list = []
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['amount'] = item.amount
        rest['price'] = item.price
        _list.append(rest)
    page = {
        "pageSize": _pageSize,
        "total": len(_list),
        "currentPage": _currentPage
    }
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


def record_add_service(request):
    data = json.load(request)
    Record.objects.create(
        uid=uuid.uuid4(),
        name=data.get('name', ''),
        amount=data.get('amount', ''),
        price=data.get('price', '')
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def record_modify_service(request):
    data = json.load(request)
    _uid = data['uid']
    _id = data['id']
    rest = Record.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Record.objects.filter(id=_id).update(
        name=data.get('name', ''),
        amount=data.get('amount', ''),
        price=data.get('price', ''),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def record_delete_service(request):
    data = json.load(request)
    _id = data['id']
    _uid = data['uid']
    rest = Record.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Record.objects.filter(id=_id).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def record_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Record.objects.filter(uid=_uid, deleted=0).first()
    if item is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    rest = {'id': item.id, 'uid': item.uid, 'name': item.name, 'user': item.user, 'image': item.image,
            'description': item.description}
    if item.createDate is not None:
        rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "product": rest,
        }
    }
    return JsonResponse(data1)
