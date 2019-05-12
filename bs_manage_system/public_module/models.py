# encoding:utf-8
from django.db import models


# Create your models here.
class UserLogin(models.Model):
    """
    用户登陆和类型表
    """
    user_id = models.CharField(max_length=64)
    user_name = models.CharField(max_length=32)
    user_password = models.CharField(max_length=64)
    user_type = models.IntegerField()
    science_type_id = models.CharField(max_length=64)


class UserInfo(models.Model):
    """
    用户详细信息表
    """
    user_id = models.CharField(max_length=64)
    user_phone = models.CharField(max_length=32)
    user_address = models.CharField(max_length=64)
    user_email = models.CharField(max_length=32)


class Notification(models.Model):
    """
    用户通知表
    """
    notification_id = models.CharField(max_length=64)
    notification_title = models.CharField(max_length=32)
    notification_content = models.TextField()
    create_user_id = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)


class Accessories(models.Model):
    """
    附件表
    """
    accessories_id = models.CharField(max_length=64)
    project_id = models.CharField(max_length=64)
    accessories_name = models.CharField(max_length=64)
    accessories_url = models.CharField(max_length=64)
    accessories_time = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    """
    审批信息表
    """
    review_id = models.CharField(max_length=64)
    project_id = models.CharField(max_length=64)
    review_user_id = models.CharField(max_length=64)
    review_status = models.IntegerField()
    review_message = models.CharField(max_length=255)
    review_user_name = models.CharField(max_length=32)
    review_time = models.DateTimeField(auto_now_add=True)


class ReviewProject(models.Model):
    """
    项目与评审信息关系表
    """
    project_id = models.CharField(max_length=64)
    review_id = models.CharField(max_length=64)


class Project(models.Model):
    """
    项目表(需要增加字段)
    project_status 0:未提交 1：已提交 2：审批中 3：审批通过 4：审批驳回
    """
    project_id = models.CharField(max_length=64)
    project_name = models.CharField(max_length=32)
    project_time = models.DateTimeField(auto_now_add=True)
    apply_user_name = models.CharField(max_length=32)  #
    apply_user_id = models.CharField(max_length=64)
    research_content = models.TextField()
    technology_new = models.TextField()
    expected_goal = models.TextField()
    participator = models.TextField()
    start_time = models.TimeField(auto_now_add=True)
    stop_time = models.TimeField(auto_now_add=True)
    project_status = models.IntegerField()
    science_type_id = models.CharField(max_length=64)


class ScienceType(models.Model):
    """
    科研类型
    """
    type_id = models.CharField(max_length=64)
    type_name = models.CharField(max_length=64)
