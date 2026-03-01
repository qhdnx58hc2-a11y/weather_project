"""subscribe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from Content import views

urlpatterns = [
    path("rest/user/validate", views.validate),
    path("rest/user/register", views.register),
    path("rest/user/list", views.user_list),
    path("rest/user/add", views.user_add),
    path("rest/user/modify", views.user_modify),
    path("rest/user/reset", views.user_reset),
    path("rest/user/delete", views.user_delete),
    path("rest/user/detail", views.user_detail),
    path("rest/user/currentUser", views.user_currentUser),
    path("rest/image/upload", views.image_upload),
    path("rest/image/uploadBase64", views.image_upload_base64),

    path("rest/content/list", views.content_list),
    path("rest/content/generate", views.content_generate),
    path("rest/content/add", views.content_add),
    path("rest/content/modify", views.content_modify),
    path("rest/content/delete", views.content_delete),
    path("rest/content/detail", views.content_detail),

    path("rest/classification/list", views.classification_list),
    path("rest/classification/add", views.classification_add),
    path("rest/classification/modify", views.classification_modify),
    path("rest/classification/delete", views.classification_delete),
    path("rest/classification/detail", views.classification_detail),

    path("rest/notice/list", views.notice_list),
    path("rest/notice/add", views.notice_add),
    path("rest/notice/modify", views.notice_modify),
    path("rest/notice/delete", views.notice_delete),
    path("rest/notice/detail", views.notice_detail),

    path("rest/record/list", views.record_list),
    path("rest/record/add", views.record_add),
    path("rest/record/modify", views.record_modify),
    path("rest/record/delete", views.record_delete),
    path("rest/record/detail", views.record_detail),
]
