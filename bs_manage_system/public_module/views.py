# encoding:utf-8
import os
import datetime
from public_module.mymako import render_mako_context
from public_module.mymako import render_json
from public_module.public_tools import auth_skip
from user_module.user_interface import UserLoinInterface
import json
from notices_module.notice_interface import NoticeInterface
import uuid
from public_module.public_tools import success_return
from public_module.public_tools import error_return
from accessories_module.accessories_interface import AccessoriesInterface
from project_module.project_interface import ProjectInterface


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
    return auth_skip(request, request.session.get('user').get('user_type'))


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


def detail_notice_html(request):
    """
    通知详情页面
    :param request:
    :return:
    """
    try:
        try:
            del request.session['notification_id']
        except:
            pass
        notification_id = request.GET.get('notification_id')
        request.session.setdefault('notification_id', notification_id)
        print notification_id
    except Exception as e:
        pass
    return render_mako_context(request, 'right/detail_notice.html')


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
    print request_body
    username = request_body.get('username')
    password = request_body.get('password')
    temp_result = UserLoinInterface.user_login(username=username, password=password)
    if temp_result.get('code') == 0:
        try:
            del request.session['user']
            print request.session.get('user')
        except:
            pass
        request.session.setdefault('user',
                                   {u'username': username, u'user_type': temp_result.get('results').get('user_type')})
        request.session.setdefault('user_type', temp_result.get('results').get('user_type'))
        request.session.setdefault('user_id', temp_result.get('results').get('user_id'))
    print request.session.get('user')
    return render_json(temp_result)


def get_notice_by_session(request):
    """
    通过session中的通知ID获取通知
    :param request:
    :return:
    """
    notification_id = request.session.get('notification_id')
    res = NoticeInterface.get_notice_by_id(notification_id)
    return render_json(res)


def get_user_login_by_id(request):
    """
    通过用户ID获取
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    user_id = request_body.get('user_id')
    res = UserLoinInterface.get_user_login_by_id(user_id)
    return render_json(res)


def apply_project_html(request):
    """
    项目申报页面
    :param request:
    :return:
    """
    return render_mako_context(request, 'apply/apply_project.html')


def upload_file_accessories(request):
    """
    上传附件
    :param request:
    :return:
    """
    file_name = request.FILES.get('file')
    project_id = request.session['apply_project_id']
    accessories_id = uuid.uuid1()
    if not file_name:
        # error
        return render_json(error_return(u'文件不存在'))
    else:
        destination = open(os.path.join("static/upload", str(uuid.uuid1()) + file_name.name), 'wb+')
        for chunk in file_name.chunks():
            destination.write(chunk)
        destination.close()
        accessories_url = str(uuid.uuid1()) + file_name.name
        res = AccessoriesInterface.insert_accessories(project_id=project_id, accessories_id=accessories_id,
                                                      accessories_name=file_name.name, accessories_url=accessories_url)
    return render_json(res)


def get_accessories_by_project_id(request):
    """
    通过项目ID获取附件List 没有附件则返回空
    :param request:
    :return:
    """
    project_id = request.session['apply_project_id']
    print project_id
    res = AccessoriesInterface.get_accessories_by_project_id(project_id=project_id, page=0, page_size=0)
    return render_json(res)


def delete_accessories_by_accessories_id(request):
    """
    通过附加ID删除附件
    :param request:
    :return:
    """

    res = AccessoriesInterface.delete_accessories_by_accessories_id(accessories_id=2)
    return render_json(res)


def insert_accessories(request):
    """
    新增附件
    :param request:
    :return:
    """
    print request.body
    json.loads(request.body)
    # res = AccessoriesInterface.insert_accessories()
    return render_json({})


def insert_project(request):
    """
    新增项目
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    project_name = request_body.get('project_name')
    research_content = request_body.get('research_content')
    technology_new = request_body.get('technology_new')
    expected_goal = request_body.get('expected_goal')
    participator = request_body.get('participator')
    start_time = request_body.get('start_time')
    stop_time = request_body.get('stop_time')
    apply_user_id = request.session['user_id']
    apply_user_name = request.session['user'].get('username')
    now_time = datetime.datetime.now()
    res = ProjectInterface.insert_project(project_name=project_name, project_time=now_time,
                                          research_content=research_content,
                                          technology_new=technology_new, expected_goal=expected_goal,
                                          participator=participator,
                                          start_time=now_time, stop_time=now_time, apply_user_id=apply_user_id,
                                          apply_user_name=apply_user_name)
    if res.get('code') == 0:
        request.session['apply_project_id'] = res.get('results').get('project_id')
    print request.session['apply_project_id']
    return render_json(res)
