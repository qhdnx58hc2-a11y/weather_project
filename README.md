# 江苏省气象灾害管理系统（Weather Disaster Management System）

## 📌 项目简介

本项目为基于 Django + Vue 的气象灾害管理系统，实现了气象数据管理、数据可视化展示、图片上传等功能。

系统采用前后端分离架构：

- 后端：Django + MySQL
- 前端：Vue + ECharts
- 文件存储：腾讯云 COS

---

## 🛠 技术栈

### 后端
- Python 3.x
- Django
- MySQL
- 腾讯云 COS SDK

### 前端
- Vue2
- Vue Router
- Axios
- ECharts

---

## 📂 项目结构
weather_project/
├── manage.py # Django 启动文件
├── weather_content.sql # 数据库初始化脚本
├── .gitignore # Git 忽略文件
├── visualization_weather/ # Django 后端代码
└── visualization_weather_vue/ # Vue 前端代码

---

## 🚀 运行方式

1️⃣ 后端运行（Django）

在项目根目录执行：

pip install -r requirements.txt
python manage.py runserver

2️⃣ 前端运行（Vue）

cd visualization_weather_vue
npm install
npm run serve

🗄 数据库初始化

创建 MySQL 数据库

导入 weather_content.sql

修改 Django settings.py 中的数据库配置

运行：

python manage.py migrate
☁ 图片上传说明

系统支持图片上传至腾讯云 COS，并返回可访问的图片 URL。

⚠ 注意：正式部署时请使用环境变量管理密钥信息，不建议将密钥直接写入代码。

📈 项目亮点

前后端分离架构

RESTful API 设计

ECharts 数据可视化展示

云存储图片管理

标准化项目结构

👩‍💻 作者

邹佳怡
