# encoding:utf-8
from django.core.paginator import Paginator
from django.db import transaction

from public_module.models import UserInfo
from public_module.models import UserLogin
from public_module.public_tools import success_return
from public_module.public_tools import error_return
from django.forms.models import model_to_dict
import uuid


class UserInfoInterface():
    """
    用户信息接口
    """

    def __init__(self):
        pass

    @classmethod
    def get_user_detail_list_by_user_login(cls, user_login_list):
        """
        通过用户登录列表列表获取用户信息列表
        :param user_login_list:
        :return:
        """
        result_list = []
        for i in user_login_list:
            user_id = i.get('user_id')
            user_info = UserInfo.objects.values().get(user_id=str(user_id))
            i['user_address'] = user_info['user_address']
            i['user_phone'] = user_info['user_phone']
            i['user_email'] = user_info['user_email']
            result_list.append(i)
        return result_list

    @classmethod
    def update_user_info(cls, user_id, user_name, user_password, user_type, user_email, user_address, user_phone,
                         science_type_id, ):
        """
        修改用户信息
        :param user_id:
        :param user_name:
        :param user_password:
        :param user_type:
        :param user_email:
        :param user_address:
        :param user_phone:
        :param science_type_id:
        :return:
        """
        try:
            with transaction.atomic():
                UserLogin.objects.filter(user_id=user_id).update(user_password=user_password, user_type=user_type,
                                                                 science_type_id=science_type_id)
                with transaction.atomic():
                    UserInfo.objects.filter(user_id=user_id).update(user_email=user_email, user_address=user_address,
                                                                    user_phone=user_phone)
                return success_return(u'修改用户信息成功', None)
        except Exception as e:
            return error_return(u'修改用户信息失败' + str(e))

    @classmethod
    def add_user_info(cls, user_id, user_name, user_password, user_type, user_email, user_address, user_phone,
                      science_type_id, ):
        """
        新增用户信息
        :param user_id:
        :param user_name:
        :param user_password:
        :param user_type:
        :param user_email:
        :param user_address:
        :param user_phone:
        :param science_type_id:
        :return:
        """
        try:
            with transaction.atomic():
                UserLogin.objects.create(user_password=user_password, user_type=user_type,user_name=user_name,
                                         science_type_id=science_type_id, user_id=user_id)
                with transaction.atomic():
                    UserInfo.objects.create(user_id=user_id, user_email=user_email, user_address=user_address,
                                            user_phone=user_phone)
                return success_return(u'新增用户信息成功', None)
        except Exception as e:
            return error_return(u'新增用户信息失败' + str(e))


class UserLoinInterface():
    """
    用户登录信息接口
    """

    def __init__(self):
        pass

    @classmethod
    def user_login(cls, username, password):
        """
        用户登陆验证
        :param username:    用户名称
        :param password:    用户密码
        :return:            json 0 验证成功 1 验证失败
        """
        query_result = UserLogin.objects.filter(user_name=username)
        if query_result is None:
            return error_return(u'用户名不存在')
        else:
            query_dict = model_to_dict(query_result[0])
            query_password = query_dict['user_password']
            if query_password == password:
                return success_return(u'登录成功', query_dict)
            else:
                return error_return(u'密码错误')

    @classmethod
    def get_user_login_by_id(cls, user_id):
        """
        通过用户ID获取用户信息
        :param user_id:
        :return:
        """
        try:
            query_result = UserLogin.objects.values().get(user_id=user_id)
            return success_return(u'获取用户登录信息成功', query_result)
        except Exception as e:
            return error_return(u'获取用户登录信息失败')

    @classmethod
    def get_user_list_by_type(cls, user_type):
        """

        :param user_type:
        :return:
        """
        result_list = []
        try:
            user_login = UserLogin.objects.values().filter(user_type=user_type)
            for i in user_login:
                result_list.append(i)
        except:
            pass
        return success_return(u'获取用户列表成功', result_list)

    @classmethod
    def get_user_list_by_name_list(cls, user_name_list):
        """
        通过用户名列表获取用户列表
        :param user_name_list:
        :return:
        """
        result_list = []
        try:
            user_login = UserLogin.objects.values().filter(user_name__in=user_name_list)
            for i in user_login:
                result_list.append(i)
        except:
            pass
        return success_return(u'获取用户列表成功', result_list)

    @classmethod
    def get_user_login_list(cls, page, page_size):
        """
        获取用户列表
        :param page:
        :param page_size:
        :return:
        """
        result_list = []
        if page == 0:
            try:
                user_login_list = UserLogin.objects.values().all().order_by('user_id')
                for i in user_login_list:
                    result_list.append(i)
            except:
                pass
        else:
            accessories = UserLogin.objects.values().all().order_by('user_id')
            paginator = Paginator(accessories, page_size)
            temp_list = paginator.page(page)
            for i in temp_list:
                i['page'] = page
                i['page_count'] = paginator.num_pages
                i['count'] = paginator.count
                result_list.append(i)
        return success_return(u'获取用户登录信息成功', result_list)

    @classmethod
    def get_specialist_by_type_id(cls, science_type_id):
        """
        通过领域id获取用户
        :param science_type_id:
        :return:
        """
        result_list = []
        user_list = UserLogin.objects.values().filter(science_type_id=science_type_id, user_type=2)
        for i in user_list:
            result_list.append(i)
        return result_list
