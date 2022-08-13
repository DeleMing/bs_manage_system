# encoding:utf-8
from itertools import groupby
from operator import itemgetter

from django.db import transaction
from django.forms import model_to_dict
from public_module.public_tools import success_return
from public_module.public_tools import error_return
from public_module.models import ScienceType
from user_module.user_interface import UserLoinInterface
import uuid


class ScienceTypeInterface():
    """
    科研类型接口
    """

    def __init__(self):
        pass

    @classmethod
    def get_all_science_type(cls):
        """
        获取所有科研类型
        :return:
        """
        result_list = []
        science_type_list = ScienceType.objects.values().all()
        for i in science_type_list:
            result_list.append(i)
        return success_return(u'获取科研类型陈宫', result_list)

    @classmethod
    def insert_science_type(cls, type_name):
        """
        新增科研类型
        :param type_name:
        :return:
        """
        type_id = uuid.uuid1()
        try:
            with transaction.atomic():
                count = ScienceType.objects.filter(type_name=type_name).count()
                if count == 0:
                    ScienceType.objects.create(type_id=type_id, type_name=type_name)
                    return success_return(u'新增科研类型成功', None)
                else:
                    return error_return(u'科研类型名称已存在')
        except Exception as e:
            return error_return(u'新增科研类型失败')

    @classmethod
    def update_science_type(cls, type_id, type_name):
        """
        修改科研类型
        :param type_id:
        :param type_name:
        :return:
        """
        try:
            with transaction.atomic():
                count = ScienceType.objects.filter(type_name=type_name).count()
                if count == 0:
                    ScienceType.objects.filter(type_id=type_id).update(type_name=type_name)
                    return success_return(u'修改科研类型成功', None)
                else:
                    return error_return(u'修改科研类型名称已存在')
        except Exception as e:
            return error_return(u'修改科研类型异常')

    @classmethod
    def get_specialist_group_by_science(cls):
        """

        :return:
        """
        result_list = []
        temp_list = []
        science_type_list = ScienceType.objects.values().all()
        for i in science_type_list:
            temp_list.append(i)
            user_temp_list = []
            user_login_list = UserLoinInterface.get_specialist_by_type_id(science_type_id=i.get('type_id'))
            for j in user_login_list:
                user_temp_list.append(j)
            i['user_list'] = user_temp_list
            result_list.append(i)
        return success_return(u'获取专家列表成功', result_list)
