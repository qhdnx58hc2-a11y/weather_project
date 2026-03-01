import uuid
from django.db import models


class User(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    role = models.CharField(max_length=64)
    image = models.CharField(max_length=1024)
    age = models.IntegerField()
    mobile = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'visualization_weather_user'


class Content(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    classification = models.CharField(max_length=64)
    image = models.CharField(max_length=1024)
    alarm = models.CharField(max_length=1024)
    time = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'visualization_weather_content'


class Classification(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    image = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        db_table = 'visualization_weather_classification'


class Notice(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    image = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        db_table = 'visualization_weather_notice'

class Record(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    amount = models.CharField(max_length=64)
    name = models.CharField(max_length=1024)
    price = models.CharField(max_length=1024)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'visualization_weather_record'