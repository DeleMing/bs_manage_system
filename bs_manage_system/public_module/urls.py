# encoding:utf-8
from django.conf.urls import patterns
from django.contrib.staticfiles import views
from bs_manage_system import settings

urlpatterns = patterns(
    'public_module.views',
    (r'^$', 'login_html'),  # 登录页面
    (r'^main/$', 'main_html'),  # 主页
    (r'^issue_notices/$', 'issue_notices'),  # 通知公告查看页面
    (r'^get_notices/$', 'get_notices'),  # 通知公告查看页面
    (r'^insert_notice_html/$', 'insert_notice_html'),  # 通知公告新增页面
    (r'^insert_notice/$', 'insert_notice'),  # 通知公告新增
    (r'^detail_notice_html/$', 'detail_notice_html'),  # 通知公告新增
    (r'^get_notice_by_session/$', 'get_notice_by_session'),  # 通过session获取通知公告
    (r'^get_user_login_by_id/$', 'get_user_login_by_id'),  # 通过用户ID获取用户登录信息
    (r'^apply_project_html/$', 'apply_project_html'),  # 申请项目页面
    (r'^upload_file_accessories/$', 'upload_file_accessories'),  # 上传项目附件
    (r'^get_accessories_by_project_id/$', 'get_accessories_by_project_id'),  # 通过项目ID获取附件列表(session)
    (r'^delete_accessories_by_accessories_id/$', 'delete_accessories_by_accessories_id'),  # 通过项目ID获取附件列表
    (r'^insert_accessories/$', 'insert_accessories'),  # 通过项目ID获取附件列表
    (r'^insert_project/$', 'insert_project'),  # 通过项目ID获取附件列表
    (r'^static/upload/(?P<path>.*)$', views.serve, {'document_root': settings.STATIC_URL}),
    (r'^download_static/$', 'download_static'),
    (r'^submit_project/$', 'submit_project'),
    (r'^my_apply_html/$', 'my_apply_html'),
    (r'^my_apply/$', 'my_apply'),
    (r'^get_user_list_by_type/$', 'get_user_list_by_type'),  # 通过用户类型获取用户列表
    (r'^get_accessories_list_project_id/$', 'get_accessories_list_project_id'),
    (r'^my_review_html/$', 'my_review_html'),
    (r'^get_username_by_session/$', 'get_username_by_session'),
    (r'^get_project_by_status/$', 'get_project_by_status'),
    (r'^project_to_review_html/$', 'project_to_review_html'),
    (r'^submit_review/$', 'submit_review'),
    (r'^get_project_by_review/$', 'get_project_by_review'),
    (r'^detail_review_html/$', 'detail_review_html'),
    (r'^get_project_by_project_id/$', 'get_project_by_project_id'),
    (r'^user_login/$', 'user_login'),  # 登陆
)
