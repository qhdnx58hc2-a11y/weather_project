import csv

data = []
# 打开CSV文件
with open('data.txt', 'r', encoding='utf-8') as file:
    # 创建CSV读取器
    _content_list = []
    _classification_list = []
    reader = csv.reader(file)
    # 遍历每一行
    index = 1
    _name = ''
    _collect = ''
    _comment = ''
    _classification = ''
    for row in reader:
        # 打印每一行数据
        # print(row)
        _address = row[0]
        _time = row[1]
        _name = row[2]
        _classification = row[3]
        _alarm = row[4]
        print(_address)
        print(_time)
        print(_name)
        print(_classification)
        print(_alarm)
    index = index + 1
