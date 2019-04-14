# encoding:utf-8
from public_module.models import UserInfo
from public_module.models import UserLogin
from public_module.public_tools import success_return
from public_module.public_tools import error_return
from django.forms.models import model_to_dict


class UserInfoInterface():
    """

    """
    def __init__(self):
        pass


class UserLoinInterface():
    """

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