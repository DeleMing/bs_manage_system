# encoding:utf-8
import os
import datetime

from django.http import HttpResponse
from bs_manage_system.settings import STATIC_URL
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
from review_module.review_interface import ReviewInterface
from user_module.user_interface import UserInfoInterface
from science_type_module.science_type_interface import ScienceTypeInterface


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
            del request.session['user_type']
            del request.session['user_id']
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
        print type(file_name.name)
        destination = open(
            os.path.join("static/upload", str(accessories_id) + '.' + file_name.name.encode('utf-8').split('.')[-1]),
            'wb+')
        for chunk in file_name.chunks():
            destination.write(chunk)
        destination.close()
        accessories_url = str(accessories_id) + '.' + file_name.name.encode('utf-8').split('.')[-1]
        res = AccessoriesInterface.insert_accessories(project_id=project_id, accessories_id=accessories_id,
                                                      accessories_name=file_name.name, accessories_url=accessories_url)
    return render_json(res)


def get_accessories_by_project_id(request):
    """
    通过项目ID获取附件List 没有附件则返回空
    :param request:
    :return:
    """
    try:
        project_id = request.session['apply_project_id']
    except:
        project_id = request.session['project_id']
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
    try:
        del request.session['apply_project_id']
    except:
        pass
    if res.get('code') == 0:
        request.session['apply_project_id'] = res.get('results').get('project_id')
    print request.session['apply_project_id']
    return render_json(res)


def download_static(request):
    """
    下载资源
    :param request:
    :return:
    """
    file_url = request.GET.get('accessories_url')
    file_name = request.GET.get('accessories_name')
    print file_name.encode('utf-8')
    url = "static/upload/" + str(file_url)
    with open(url, 'rb') as code:
        response = HttpResponse(code)
        code.close()
    response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename="' + file_name.encode('utf-8')
    return response


def submit_project(request):
    """
    提交项目
    :param request:
    :return:
    """
    project_id = request.session['apply_project_id']
    res = ProjectInterface.change_project_status(project_id=project_id, project_status=1)
    if res.get('code') == 0:
        res['message'] = u'提交项目成功'
    else:
        res['message'] = u'提交项目失败'
    return render_json(res)


def my_apply_html(request):
    """
    我的申请页面HTML
    :param request:
    :return:
    """
    return render_mako_context(request, 'apply/my_apply.html')


def my_apply(request):
    """
    获取我的申请
    :param request:
    :return:
    """
    user_id = request.session['user_id']
    print user_id
    res = ProjectInterface.get_project_by_user_id(apply_user_id=user_id, page=0, page_size=2)
    return render_json(res)


def get_user_list_by_type(request):
    """
    通过用户类型获取用户列表
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    user_type = request_body.get('user_type')
    # user_type = 2
    res = UserLoinInterface.get_user_list_by_type(user_type=user_type)
    return render_json(res)


def get_accessories_list_project_id(request):
    """
    通过项目id获取附件列表(非session)
    :param request:
    :return:
    """
    project_id = request.GET.get('project_id')
    res = AccessoriesInterface.get_accessories_by_project_id(project_id=project_id, page=0, page_size=0)
    return render_json(res)


def my_review_html(request):
    """
    需要我审批的页面
    :param request:
    :return:
    """
    return render_mako_context(request, 'review/my_review.html')


def get_username_by_session(request):
    """
    通过session获取用户名
    :param request:
    :return:
    """
    try:
        username = request.session.get('user')['username']
        res = success_return(u'获取用户名成功', {'username': username})
    except Exception as e:
        res = error_return(u'获取用户名失败')
    return render_json(res)


def get_project_by_status(request):
    """
    通过项目状态获取项目列表
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    project_status = request_body.get('project_status')
    res = ProjectInterface.get_project_by_status(project_status=project_status, page=0, page_size=0)
    return render_json(res)


def project_to_review_html(request):
    """
    设置评审专家页面
    :param request:
    :return:
    """
    return render_mako_context(request, 'review/project_to_review.html')


def submit_review(request):
    """
    设置评审专家
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    project_id = request_body.get('project_id')
    user_name_list = request_body.get('review_list')
    review_id = uuid.uuid1()
    user_list = UserLoinInterface.get_user_list_by_name_list(user_name_list).get('results')
    temp = ProjectInterface.change_project_status(project_id=project_id, project_status=2)
    for i in user_list:
        init_review_res = ReviewInterface.init_review(review_id=review_id, review_user_id=i.get('user_id'),
                                                      review_user_name=i.get('user_name'), project_id=project_id)
        if init_review_res.get('code') == 0:
            res = success_return(u'设置评审专家成功', None)
            continue
        else:
            ReviewInterface.delete_review(review_id=review_id)
            ProjectInterface.change_project_status(project_id=project_id, project_status=1)
            res = success_return(u'设置评审专家失败', None)
            return render_json(res)
    return render_json(res)


def get_project_by_review(request):
    """
    通过评审专家用户ID获取需要审批的项目List
    :param request:
    :return:
    """
    user_id = request.session['user_id']
    res = ReviewInterface.get_review_list_by_user_id(review_user_id=user_id)
    project_id_list = []
    for i in res.get('results'):
        project_id = i.get('project_id')
        project_id_list.append(project_id)
    project_id_list = list(set(project_id_list))
    print project_id_list
    res = ProjectInterface.get_project_by_project_id_list(project_id_list=project_id_list, page=0, page_size=10)
    return render_json(res)


def detail_review_html(request):
    """
    跳转到审批详情页, 并设置session
    :param request:
    :return:
    """
    try:
        del request.session['project_id']
    except:
        pass
    project_id = request.GET.get('project_id')
    request.session['project_id'] = project_id
    return render_mako_context(request, 'review/detail_review.html')


def get_project_by_project_id(request):
    """
    通过项目ID获取项目信息
    :param request:
    :return:
    """
    project_id_list = []
    project_id = request.session['project_id']
    print project_id
    project_id_list.append(project_id)
    res = ProjectInterface.get_project_by_project_id_list(project_id_list=project_id_list, page=0, page_size=0)
    return render_json(res)


def get_other_review_by_project_id(request):
    """
    通过项目ID获取评审信息
    :param request:
    :return:
    """
    project_id = request.session['project_id']
    print project_id
    res = ReviewInterface.get_review_list_by_project_id(project_id=project_id)
    print res
    user_id = request.session['user_id']
    result_list = []
    for i in res.get('results'):
        if user_id != i.get('review_user_id'):
            result_list.append(i)
    return render_json(success_return(u'获取成功', result_list))


def get_my_review_by_project_id(request):
    """
    获取个人审批意见
    :param request:
    :return:
    """
    project_id = request.session['project_id']
    res = ReviewInterface.get_review_list_by_project_id(project_id=project_id)
    user_id = request.session['user_id']
    result_list = []
    for i in res.get('results'):
        if user_id == i.get('review_user_id'):
            result_list.append(i)
            return render_json(success_return(u'获取成功', result_list))


def submit_my_review(request):
    """
    提交我的评审信息
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    review_id = request_body.get('review_id')
    review_message = request_body.get('review_message')
    review_status = request_body.get('review_status')
    res = ReviewInterface.update_review(review_id=review_id, review_message=review_message, review_status=review_status)
    return render_json(res)


def detail_user_list_html(request):
    """
    用户管理页面
    :param request:
    :return:
    """
    return render_mako_context(request, 'user/detail_user_list.html')


def get_user_login_list(request):
    """
    获取用户登录列表
    :param request:
    :return:
    """
    res = UserLoinInterface.get_user_login_list(page=0, page_size=0)
    return render_json(res)


def get_user_all_info(request):
    """
    获取所有用户信息
    :param request:
    :return:
    """
    user_login = UserLoinInterface.get_user_login_list(page=0, page_size=0)
    try:
        res = UserInfoInterface.get_user_detail_list_by_user_login(user_login_list=user_login.get('results'))
        return render_json(success_return(u'获取用户列表成功', res))
    except Exception as e:
        return render_json(error_return(u'获取用户列表失败' + str(e)))


def get_all_science_type(request):
    """
    获取所有科研类型
    :param request:
    :return:
    """
    res = ScienceTypeInterface.get_all_science_type()
    print res
    return render_json(res)


def science_type_html(request):
    """
    科研类型管理页面
    :param request:
    :return:
    """
    return render_mako_context(request, '/science_type/science_type.html')


def add_science_type(request):
    """
    新增科研类型
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    type_name = request_body.get('type_name')
    res = ScienceTypeInterface.insert_science_type(type_name)
    return render_json(res)


def update_science_type(request):
    """
    修改科研类型
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    type_name = request_body.get('type_name')
    type_id = request_body.get('type_id')
    res = ScienceTypeInterface.update_science_type(type_id=type_id, type_name=type_name)
    return render_json(res)


def my_info_html(request):
    """
    我的信息页面
    :param request:
    :return:
    """
    return render_mako_context(request, '/user/my_info.html')


def get_active_user_info(request):
    """
    获取当前用户信息
    :param request:
    :return:
    """
    user_id = request.session['user_id']
    user_login = UserLoinInterface.get_user_login_by_id(user_id=user_id)
    user_login_list = []
    user_login_list.append(user_login.get('results'))
    try:
        res = UserInfoInterface.get_user_detail_list_by_user_login(user_login_list=user_login_list)
        return render_json(success_return(u'获取用户列表成功', res))
    except Exception as e:
        return render_json(error_return(u'获取用户列表失败' + str(e)))


def update_user_info(request):
    """
    修改用户信息
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    user_id = request_body.get('user_id')
    user_name = request_body.get('user_name')
    user_password = request_body.get('user_password')
    user_type = request_body.get('user_type')
    user_email = request_body.get('user_email')
    user_address = request_body.get('user_address')
    user_phone = request_body.get('user_phone')
    science_type_id = request_body.get('science_type_id')
    res = UserInfoInterface.update_user_info(user_id=user_id, user_name=user_name, user_password=user_password,
                                             user_type=user_type, user_email=user_email, user_address=user_address,
                                             user_phone=user_phone, science_type_id=science_type_id)
    return render_json(res)


def add_user_info(request):
    """
    新增用户信息
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    user_id = uuid.uuid1()
    user_name = request_body.get('user_name')
    user_password = request_body.get('user_password')
    user_type = request_body.get('user_type')
    user_email = request_body.get('user_email')
    user_address = request_body.get('user_address')
    user_phone = request_body.get('user_phone')
    science_type_id = request_body.get('science_type_id')
    res = UserInfoInterface.add_user_info(user_id=user_id, user_name=user_name, user_password=user_password,
                                          user_type=user_type, user_email=user_email, user_address=user_address,
                                          user_phone=user_phone, science_type_id=science_type_id)
    return render_json(res)


def get_specialist_group_by_science_type(request):
    """
    获取专家列表，并对其进行分组
    :param request:
    :return:
    """
    specialist_res = UserLoinInterface.get_specialist()
    specialist = specialist_res.get('results')
    res = ScienceTypeInterface.get_specialist_group_by_science_type(specialist)
    res = res
    return render_json(res)
