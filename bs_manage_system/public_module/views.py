# encoding:utf-8
from public_module.mymako import render_mako_context
from public_module.mymako import render_json
from user_module.user_interface import UserLoinInterface
import json


# Create your views here.
def login_html(request):
    """
    登录页面
    :param request:
    :return:
    """
    return render_mako_context(request, 'common/login.html')


def main_html(request):
    """
    主页
    :param request:
    :return:
    """
    return render_mako_context(request, 'common/main.html')


def user_login(request):
    """
    用户登录
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    username = request_body.get('username')
    password = request_body.get('password')
    temp_result = UserLoinInterface.user_login(username=username, password=password)
    if temp_result.get('code') == 0:
        request.session.setdefault('user', {u'username': username})
    return render_json(temp_result)
