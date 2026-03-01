import json
import os
import random
import uuid
import csv
from django.http import JsonResponse
from django.db.models import Count, Sum, Func, Value, IntegerField, Q
from django.db.models.functions import Substr

from Content.migrations.service import userService
from Content.models import Content, User, Classification

class StrIndex(Func):
    """自定义函数模拟 SQL 的字符串位置查找"""
    function = 'INSTR'  # MySQL/SQLite 使用 INSTR，PostgreSQL 用 STRPOS
    template = "%(function)s(%(expressions)s)"
    output_field = IntegerField()
    def __init__(self, expression, substring, **extra):
        super().__init__(expression, Value(substring), **extra)

def content_list_service(request):
    # 内容分页查询+多维度统计
    """内容列表服务，支持分页查询和多种图表数据统计"""
    data = json.load(request)
    #图表 chart 灾害分布
    _type = data.get('type')
    _field = data.get('field')
    # 1. 基础分类统计（饼图/柱状图数据）
    if _type == 'chart':
        if _field:
            _list = []
            # 按指定字段分组统计数量（如按灾害类型统计）# 按分类统计未删除的内容数量
            stats = Content.objects.filter(deleted=0).values(_field).annotate(
                value=Count('id')
            ).order_by(_field)
            for item in stats:
                rest = {}
                rest['name'] = item[_field]
                rest['value'] = item['value']
                _list.append(rest)
            data1 = {
                "success": "true",
                "message": "操作成功",
                "returnCode": "200",
                "returnData": _list
            }
            return JsonResponse(data1)
    # 2. 预警级别-分类交叉统计（堆叠柱状图数据）
    if _type == 'chartAlarm':
        _list = []
        # 按alarm统计未删除的内容数量
        stats = Content.objects.filter(deleted=0).values('alarm','classification').annotate(
            value=Count('id')
        ).order_by('alarm','classification')
        # print(stats)
        for item in stats:
            rest = {}
            rest['alarm'] = item['alarm']# 预警级别
            rest['name'] = item['classification'] # 灾害类型
            rest['value'] = item['value'] # 数量
            _list.append(rest)
        data1 = {
            "success": "true",
            "message": "操作成功",
            "returnCode": "200",
            "returnData": _list
        }
        return JsonResponse(data1)
    if _type == 'chartAddress':
        """处理逻辑：
               1. 从address字段提取城市名（逗号前部分）
               2. 按城市分组统计各预警级别的数量
               """
        _list = []
        # 按address alarm统计未删除的内容数量
        # 先提取城市名称(逗号前的部分)
        queryset = Content.objects.filter(deleted=0).values('address').annotate(
            city=Substr('address', 1, StrIndex('address', ',') - 1)
        )
        # 按城市分组统计各预警级别的数量
        stats = queryset.values('city').annotate(
            红色=Count("id",filter=Q(alarm__contains='红色')),
            橙色=Count("id",filter=Q(alarm__contains='橙色')),
            黄色=Count("id",filter=Q(alarm__contains='黄色')),
            蓝色=Count("id",filter=Q(alarm__contains='蓝色')),
        ).order_by('city')

        # print(stats)
        _list = list(stats)
        # print(_list)

        data1 = {
            "success": "true",
            "message": "操作成功",
            "returnCode": "200",
            "returnData": _list
        }
        return JsonResponse(data1)
    # 普通内容列表查询(带分页)
    # 分页及筛选参数
    _pageSize = data.get('pageSize', 10)
    _currentPage = data.get('currentPage', 1)
    _name = data.get('name', '').strip()
    _classification = data.get('classification', '')
    _alarm = data.get('alarm', '')
    # 基础查询-未删除的内容
    listC = Content.objects.filter(deleted=0)
    if _name:
        listC = listC.filter(name__contains=_name)
    if _classification:
        listC = listC.filter(classification__contains=_classification)
    if _alarm:
        listC = listC.filter(alarm__contains=_alarm)

    _list = []
    # 获取关联的分类列表（用于前端筛选
    classificationList = Classification.objects.filter(deleted=0)
    _classification_list = []
    _dict = {}# 分类UID到名称的映射
    _data_list = [] # 简化数据格式1
    _data_list1 = [] # 简化数据格式2
    # 处理分类数据
    for item in classificationList:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['image'] = item.image
        _classification_list.append(rest)
        _dict[item.uid] = item.name
    for item in listC:
        rest = {}
        data = []
        data1 = []
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['classification'] = item.classification
        rest['description'] = item.description
        rest['image'] = item.image
        rest['alarm'] = item.alarm
        rest['time'] = item.time
        rest['address'] = item.address
        # 格式化日期
        if item.createDate is not None:
            rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
        data.append(item.time)
        data.append(item.name)
        data.append(item.address)
        data1.append(item.time)
        data1.append(item.address)
        data1.append(item.name)
        data1.append(item.classification)
        data1.append(item.alarm)
        _data_list.append(data)
        _data_list1.append(data1)
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
            _data_list = _data_list[_start: len(_data_list)]
            # _data_list1 = _data_list1[_start: len(_data_list1)]
        if _pageSize * _currentPage <= len(_list):
            _start = (_currentPage - 1) * _pageSize
            _end = _currentPage * _pageSize
            _list = _list[_start: _end]
            _data_list = _data_list[_start: _end]
            # _data_list1 = _data_list1[_start: _end]
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "list": _list,
            "data": _data_list,
            "data1": _data_list1,
            "classificationList": _classification_list,
            "page": page,
        }
    }
    return JsonResponse(data1)


def content_add_service(request):
    """添加内容服务"""
    data = json.load(request)
    _user = userService.getCurrentUser(request)
    # 创建新内容
    Content.objects.create(
        uid=uuid.uuid4(),# 生成唯一ID
        name=data['name'],
        description=data.get('description', ''),
        classification=data.get('classification', ''),
        image=data.get('image', ''),
        address=data.get('address', ''),
        time=data.get('time', ''),
        alarm=data.get('alarm', ''),

    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def content_generate_service(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 江苏省城市区域数据
    jiangsu = {
        '南京市': ["玄武区","秦淮区","建邺区","鼓楼区","浦口区","栖霞区","雨花台区","江宁区","六合区","溧水区","高淳区"],
        '无锡市': ["锡山区","惠山区","滨湖区","梁溪区","新吴区","江阴市","宜兴市"],
        '徐州市': ["鼓楼区","云龙区","贾汪区","泉山区","铜山区","丰县","沛县","睢宁县","新沂市","邳州市"],
        '常州市': ["天宁区", "钟楼区", "新北区", "武进区", "金坛区", "溧阳市"],
        '苏州市': ["虎丘区","吴中区","相城区","姑苏区","吴江区","常熟市","张家港市","昆山市","太仓市"],
        '南通市': ["通州区","崇川区","海门区","如东县","启东市","如皋市","海安市"],
        '连云港市': ["连云区", "海州区", "赣榆区", "东海县", "灌云县", "灌南县"],
        '淮安市': ["淮安区","淮阴区","清江浦区","洪泽区","涟水县","盱眙县","金湖县"],
        '盐城市': ["亭湖区","盐都区","大丰区","响水县","滨海县","阜宁县","射阳县","建湖县","东台市"],
        '扬州市': ["广陵区", "邗江区", "江都区", "宝应县", "仪征市", "高邮市"],
        '镇江市': ["京口区", "润州区", "丹徒区", "丹阳市", "扬中市", "句容市"],
        '泰州市': ["海陵区", "高港区", "姜堰区", "兴化市", "靖江市", "泰兴市"],
        '宿迁市': ["宿城区", "宿豫区", "沭阳县", "泗阳县", "泗洪县"],
    }
    
    data = json.load(request)
    _dataSize = int(data.get('dataSize', 10))
    
    _content_list = []
    _classification_list = []
    txt_path = os.path.join(BASE_DIR, 'utils', 'data.txt')
    # print('--path--',BASE_DIR,txt_path)
    # 打开CSV文件
    with open(txt_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        _content_list = list(reader)
        
    random_samples = random.sample(_content_list, min(_dataSize, len(_content_list)))
    
    for row in random_samples:
        # 随机选择一个城市
        random_city = random.choice(list(jiangsu.keys()))
        # 随机选择该城市的一个区县
        random_district = random.choice(jiangsu[random_city])
        # print(f"随机抽取: {random_city} - {random_district}")
        _address = row[0] = f"{random_city},{random_district}"
        _time = row[1]
        _name = row[2]
        _classification = row[3]
        _alarm = row[4] = row[4].strip()
        Content.objects.create(
            uid=uuid.uuid4(),
            name=_name,
            address=_address,
            time=_time,
            alarm=_alarm,
            classification=_classification,
        )
        """ classification = Classification.objects.filter(name=_classification).first()
        if classification is None:
            Classification.objects.create(
                uid=uuid.uuid4(),
                name=_classification,
            ) """

    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": random_samples
    }
    return JsonResponse(data1)


def content_modify_service(request):
    """修改内容服务"""
    data = json.load(request)
    _uid = data['uid']
    # 检查内容是否存在
    rest = Content.objects.filter(uid=_uid, deleted=0).first()
    _user = userService.getCurrentUser(request)
    if rest is None:
        data1 = {
            "success": "false",
            "message": "内容不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    # 更新内容
    Content.objects.filter(uid=_uid).update(
        name=data['name'],
        description=data.get('description', ''),
        classification=data.get('classification', ''),
        image=data.get('image', ''),
        address=data.get('address', ''),
        time=data.get('time', ''),
        alarm=data.get('alarm', ''),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def content_delete_service(request):
    """删除内容服务"""
    data = json.load(request)
    _uid = data['uid']
    # 检查内容是否存在
    rest = Content.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "内容不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Content.objects.filter(uid=_uid).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def content_detail_service(request):
    """获取内容详情服务"""
    data = json.load(request)
    _uid = data['uid']
    # 查询内容
    item = Content.objects.filter(uid=_uid, deleted=0).first()
    if item is None:
        data1 = {
            "success": "false",
            "message": "内容不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    # 构建返回数据
    rest = {}
    rest['id'] = item.id
    rest['uid'] = item.uid
    rest['name'] = item.name
    rest['description'] = item.description
    rest['image'] = item.image
    rest['classification'] = item.classification
    rest['alarm'] = item.alarm
    rest['time'] = item.time
    rest['address'] = item.address

    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": rest
    }
    return JsonResponse(data1)
