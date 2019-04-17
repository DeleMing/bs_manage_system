# encoding:utf-8
from django.conf.urls import patterns

urlpatterns = patterns(
    'public_module.views',
    (r'^$', 'login_html'),  # 登录页面
    (r'^main/$', 'main_html'),  # 主页
    (r'^issue_notices/$', 'issue_notices'),  # 通知公告查看页面
    (r'^get_notices/$', 'get_notices'),  # 通知公告查看页面
    (r'^insert_notice_html/$', 'insert_notice_html'),  # 通知公告新增页面
    (r'^insert_notice/$', 'insert_notice'),  # 通知公告新增
    (r'^detail_notice_html/$', 'detail_notice_html'),  # 通知公告新增
    (r'^get_notice_by_session/$', 'get_notice_by_session'),  # 通知公告新增
    (r'^get_user_login_by_id/$', 'get_user_login_by_id'),  # 通知公告新增
    (r'^apply_project_html/$', 'apply_project_html'),  # 通知公告新增

    (r'^user_login/$', 'user_login'),  # 登陆
)
