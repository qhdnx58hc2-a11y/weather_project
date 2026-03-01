import json
import uuid

from django.http import JsonResponse
from Content.models import User
import hashlib
import jwt


def validate_service(request):
    """用户登录验证服务
       Args:
           request: 包含username和password的请求对象
       Returns:
           JsonResponse: 包含登录状态、JWT令牌和用户基本信息
       """
    # MD5加盐加密密码
    data = json.load(request)
    username = data['username']
    password = data['password']
    md5 = hashlib.md5(password.encode())  # 创建一个md5对象
    salt = "$1$asd"# 固定盐值
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest() # 加密后的密码
    _user = User.objects.filter(username=username, password=encrypted_data, deleted=0).first()
    # 生成JWT令牌
    payload = {
        "username": username
    }
    _token = jwt.encode(payload=payload, key="tk123")
    # decoded_token = _token.decode('utf-8')
    decoded_token = _token
    if _user is not None:
        # 返回用户基本信息及Token
        rest = {}
        rest['id'] = _user.id
        rest['uid'] = _user.uid
        rest['name'] = _user.name
        rest['username'] = _user.username
        rest['gender'] = _user.gender
        rest['age'] = _user.age
        rest['role'] = _user.role
        rest['mobile'] = _user.mobile
        rest['email'] = _user.email
        rest['image'] = _user.image
        data1 = {
            "success": "true",
            "message": "请求成功",
            "returnCode": "200",
            "returnData": {
                "logintoken": decoded_token,
                "user": rest
            }
        }
        return JsonResponse(data1)
    data1 = {
        "success": "false",
        "message": "账号或者密码错误",
        "returnCode": "500",
        "returnData": ""
    }
    return JsonResponse(data1)


def register_service(request):
    """用户注册服务
       Args:
           request: 包含用户注册信息的请求对象
       Returns:
           JsonResponse: 注册成功或失败响应
       """
    data = json.load(request)
    username = data['username']
    # 检查用户名是否已存在
    password = data['password']# 密码加密处理
    rest = User.objects.filter(username=username, deleted=0).first()
    if rest is not None:
        # 用户名已存在，返回错误响应
        data1 = {
            "success": "false",
            "message": "用户已存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    # 密码加密处理
    md5 = hashlib.md5(password.encode())  # 创建一个md5对象
    salt = "$1$asd"
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest()
    # 创建用户
    User.objects.create(
        name=data['name'],
        username=data['username'],
        password=encrypted_data,
        mobile=data['mobile'],
        email=data['email'],
        role=data['role'],
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def user_list_service(request):
    """用户列表查询服务
       """
    data = json.load(request) # 解析请求数据
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    _name = data.get('name', '').strip()
    _mobile = data.get('mobile', '')
    _gender = data.get('gender', '')
    _role = data['role']
    list = User.objects.filter(deleted=0, role='1')
    # 应用筛选条件
    if _name is not None and _name != '':# 姓名模糊查询(不区分大小写)
        list = list.filter(name__icontains=_name)
    if _mobile:
        list = list.filter(mobile__contains=_mobile)
    if _gender:
        list = list.filter(gender=_gender)

    _list = []
    genderMap = {
        "male": "男",
        "female": "女"
    }
    genderList = [
        {
            "value": "male",
            "label": "男"
        },
        {
            "value": "female",
            "label": "女"
        }
    ]
    # 构建用户数据列表
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['username'] = item.username
        rest['password'] = item.password
        rest['gender'] = item.gender

        # 添加性别显示名(如果有性别数据)
        if item.gender is not None and item.gender != '':
            rest['genderName'] = genderMap[item.gender]
        rest['age'] = item.age
        rest['role'] = item.role
        rest['mobile'] = item.mobile
        rest['email'] = item.email
        rest['image'] = item.image
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
    # 构建最终响应数据
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "list": _list,
            "page": page,
            "genderList": genderList
        }
    }
    return JsonResponse(data1)


def user_add_service(request):
    """用户添加
       """
    data = json.load(request)
    username = data['username']
    password = data['password']
    rest = User.objects.filter(username=username, deleted=0).first()
    # 验证用户存在性
    if rest is not None:
        data1 = {
            "success": "false",
            "message": "用户已存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    # 密码加密处理
    md5 = hashlib.md5(password.encode())  # 创建一个md5对象
    salt = "$1$asd"
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest()
    # 创建新用户
    User.objects.create(
        uid=uuid.uuid4(),
        name=data['name'],
        username=data['username'],
        password=encrypted_data,
        gender=data.get('gender', ''),
        mobile=data.get('mobile', ''),
        email=data.get('email', ''),
        role=data['role'],
        image=data.get('image', ''),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def user_modify_service(request):
    """用户信息修改服务
        Args:
            request: Django请求对象，包含以下JSON格式参数:
                - uid: 用户唯一标识(必填)
                - username: 新用户名(必填)
                - name: 新真实姓名(必填)
                - password: 新密码(可选，为空则不修改)
                - gender: 性别(可选，默认为"male")
                - mobile: 手机号(可选，默认为空)
                - email: 邮箱(可选，默认为空)
                - image: 头像URL(可选，默认为空)
        Returns:
            JsonResponse: 操作结果响应(格式同上)
        """
    data = json.load(request)
    _uid = data['uid']
    password = data.get('password', '')
    # 字典不存在，加一个默认值
    gender = data.get('gender', "male")
    rest = User.objects.filter(username=data['username'], deleted=0).exclude(uid=_uid).first()
    # 检查用户名是否已被其他用户使用(排除当前用户)
    if rest is not None:
        # 用户名已存在，返回错误
        data1 = {
            "success": "false",
            "message": "账号名已存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    # 检查用户是否存在
    rest = User.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "用户不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    md5 = hashlib.md5(password.encode())  # 创建一个md5对象
    salt = "$1$asd"
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest()
    # 更新用户信息
    User.objects.filter(uid=_uid).update(
        name=data['name'],
        username=data['username'],
        password=encrypted_data if password != '' else rest.password,
        gender=gender,
        mobile=data.get('mobile', ''),
        email=data.get('email', ''),
        image=data.get('image', ''),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)

def user_reset_service(request):
    """用户密码重置服务(需验证旧密码)
       Args:
           request: Django请求对象，包含以下JSON参数:
               - uid: 用户唯一标识(必填)
               - oldPassword: 旧密码(必填)
               - newPassword: 新密码(必填)
       Returns:
           JsonResponse: 操作结果响应(格式同上)
       """
    data = json.load(request)
    _uid = data['uid']
    oldPassword = data['oldPassword']
    newPassword = data['newPassword']
    # 检查用户是否存在
    rest = User.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "用户不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)

    md5 = hashlib.md5(oldPassword.encode())  # 创建一个md5对象
    salt = "$1$asd"
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest()

    if rest.password != encrypted_data:
        data1 = {
            "success": "false",
            "message": "旧密码错误",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    # 验证旧密码
    md5 = hashlib.md5(newPassword.encode())  # 创建一个md5对象
    salt = "$1$asd"
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest()
    User.objects.filter(uid=_uid).update(

        password=encrypted_data,

    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": ""
    }
    return JsonResponse(data1)


def user_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = User.objects.filter(uid=_uid, deleted=0).first() #用户无权限
    if rest is None:
        data1 = {
            "success": "false",
            "message": "用户不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    User.objects.filter(uid=_uid).update(deleted=1,)#管理员权限
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


    data = json.load(request)
    _uid = data['uid']
    item = User.objects.filter(uid=_uid, deleted=0).first()
    if item is None:
        data1 = {
            "success": "false",
            "message": "用户不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    rest = {}
    rest['id'] = item.id
    rest['uid'] = item.uid
    rest['name'] = item.name
    rest['username'] = item.username
    rest['password'] = item.password
    rest['gender'] = item.gender
    rest['age'] = item.age
    rest['mobile'] = item.mobile
    rest['email'] = item.email
    rest['image'] = item.image
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": rest
    }
    return JsonResponse(data1)


def user_currentUser_service(request):
    """获取当前登录用户信息服务
       Args:
           request: Django请求对象，需包含有效的Authorization头(JWT令牌)
       Returns:
           JsonResponse: 包含以下结构的响应数据:
               - success: 操作是否成功(true/false)
               - message: 操作结果描述
               - returnCode: 状态码(200成功/500失败)
               - returnData: 用户详细信息(若成功)
       """
    data = json.load(request)
    item = getCurrentUser(request)
    # 用户不存在处理
    if item is None:
        data1 = {
            "success": "false",
            "message": "用户不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    rest = {}
    rest['id'] = item.id
    rest['uid'] = item.uid
    rest['name'] = item.name
    rest['username'] = item.username
    rest['password'] = item.password
    rest['gender'] = item.gender
    rest['age'] = item.age
    rest['role'] = item.role
    rest['mobile'] = item.mobile
    rest['email'] = item.email
    rest['image'] = item.image
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": rest
    }
    return JsonResponse(data1)


def getCurrentUser(request):
    """通过JWT令牌获取当前用户
       Args:
           request: Django请求对象，需包含HTTP_AUTHORIZATION头
       Returns:
           User: 用户对象或None(未找到时)
       """
    # 从请求头获取JWT令牌
    _authorization = request.META.get('HTTP_AUTHORIZATION')
    # _payload = jwt.decode(_authorization, key="tk123")
    _payload = jwt.decode(_authorization, key="tk123", algorithms='HS256')
    _username = _payload['username']
    # 查询未删除的用户
    _user = User.objects.filter(username=_username, deleted=0).first()# 根据用户名查询用户
    return _user
