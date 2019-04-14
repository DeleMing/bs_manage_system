# encoding:utf-8
from django.db import models


# Create your models here.
class UserLogin(models.Model):
    """
    用户登陆和类型表
    """
    user_id = models.CharField(max_length=32)
    user_name = models.CharField(max_length=32)
    user_password = models.CharField(max_length=64)
    user_type = models.IntegerField()


class UserInfo(models.Model):
    """
    用户详细信息表
    """
    user_id = models.CharField(max_length=32)
    user_phone = models.CharField(max_length=32)
    user_address = models.CharField(max_length=64)
    user_email = models.CharField(max_length=32)


class Notification(models.Model):
    """
    用户通知表
    """
    notification_id = models.CharField(max_length=32)
    notification_title = models.CharField(max_length=32)
    notification_content = models.CharField(max_length=255)
    create_user_id = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)


class Accessories(models.Model):
    """
    附件表
    """
    accessories_id = models.CharField(max_length=32)
    project_id = models.CharField(max_length=32)
    accessories_name = models.CharField(max_length=64)
    accessories_url = models.CharField(max_length=64)
    accessories_time = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    """
    审批信息表
    """
    review_id = models.CharField(max_length=32)
    review_user_id = models.CharField(max_length=32)
    review_status = models.IntegerField()
    review_message = models.CharField(max_length=255)
    review_user_name = models.CharField(max_length=32)
    review_time = models.DateTimeField(auto_now_add=True)


class ReviewProject(models.Model):
    """
    项目与评审信息关系表
    """
    project_id = models.CharField(max_length=32)
    review_di = models.CharField(max_length=32)


class Project(models.Model):
    """
    项目表(需要增加字段)
    """
    project_id = models.CharField(max_length=32)
    project_name = models.CharField(max_length=32)
    project_time = models.DateTimeField(auto_now_add=True)
    apply_user_name = models.CharField(max_length=32)