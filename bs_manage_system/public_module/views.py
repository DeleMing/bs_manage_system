# encoding:utf-8
from public_module.mymako import render_mako_context
from public_module.mymako import render_json
from public_module.public_tools import auth_skip
from user_module.user_interface import UserLoinInterface
import json
from notices_module.notice_interface import NoticeInterface


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
    print type(request.session.get('user_type'))
    return auth_skip(request, request.session.get('user_type'))


def issue_notices(request):
    """
    通知公告页面
    :param request:
    :return:
    """
    return render_mako_context(request, 'right/issue_notices.html')


def insert_notice_html(request):
    """
    新增通知页面
    :param request:
    :return:
    """

    return render_mako_context(request, 'right/insert_notice.html')


def insert_notice(request):
    """
    新增通知
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    notice_title = request_body.get('title')
    notice_content = request_body.get('content')
    create_user_id = request.session.get('user_id')
    res = NoticeInterface.insert_notice(notice_title, notice_content, create_user_id)
    return render_json(res)


def get_notices(request):
    """
    获取通知
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    page = request_body.get('page')
    page_size = request_body.get('page_size')
    result_json = NoticeInterface.get_notices(page=page, page_size=page_size)
    return render_json(result_json)


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
        request.session.setdefault('user',
                                   {u'username': username, u'user_type': temp_result.get('results').get('user_type')})
        request.session.setdefault('user_type', temp_result.get('results').get('user_type'))
        request.session.setdefault('user_id', temp_result.get('results').get('user_id'))
    print request.session.get('user')
    return render_json(temp_result)
