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
    (r'^insert_project/$', 'insert_project'),  # 新增项目
    (r'^static/upload/(?P<path>.*)$', views.serve, {'document_root': settings.STATIC_URL}),
    (r'^download_static/$', 'download_static'),  # 下载静态资源
    (r'^submit_project/$', 'submit_project'),  # 提交项目
    (r'^my_apply_html/$', 'my_apply_html'),  # 我的申请页面
    (r'^my_apply/$', 'my_apply'),  # 获取我的申请
    (r'^get_user_list_by_type/$', 'get_user_list_by_type'),  # 通过用户类型获取用户列表
    (r'^get_accessories_list_project_id/$', 'get_accessories_list_project_id'),  # 通过项目id获取附件列表(非session)
    (r'^my_review_html/$', 'my_review_html'),  # 需要我审批的页面
    (r'^get_username_by_session/$', 'get_username_by_session'),  # 通过session获取用户名
    (r'^get_project_by_status/$', 'get_project_by_status'),  # 通过项目状态获取项目列表
    (r'^project_to_review_html/$', 'project_to_review_html'),  # 设置评审专家页面
    (r'^submit_review/$', 'submit_review'),  # 设置评审专家
    (r'^get_project_by_review/$', 'get_project_by_review'),  # 通过评审专家用户ID获取需要审批的项目List
    (r'^detail_review_html/$', 'detail_review_html'),  # 跳转到审批详情页, 并设置session
    (r'^get_project_by_project_id/$', 'get_project_by_project_id'),  # 通过项目ID获取项目信息
    (r'^get_other_review_by_project_id/$', 'get_other_review_by_project_id'),  # 通过项目ID获取评审信息
    (r'^get_my_review_by_project_id/$', 'get_my_review_by_project_id'),  # 获取个人审批意见
    (r'^submit_my_review/$', 'submit_my_review'),  # 提交我的评审信息
    (r'^detail_user_list_html/$', 'detail_user_list_html'),  # 用户管理页面
    (r'^get_user_login_list/$', 'get_user_login_list'),  # 获取用户登录列表
    (r'^get_user_all_info/$', 'get_user_all_info'),  # 获取所有用户信息
    (r'^get_all_science_type/$', 'get_all_science_type'),  # 获取所有科研类型
    (r'^science_type_html/$', 'science_type_html'),  # 科研类型管理页面
    (r'^add_science_type/$', 'add_science_type'),  # 新增科研类型
    (r'^update_science_type/$', 'update_science_type'),  # 修改科研类型
    (r'^my_info_html/$', 'my_info_html'),  # 我的信息页面
    (r'^get_active_user_info/$', 'get_active_user_info'),  # 获取当前用户信息
    (r'^update_user_info/$', 'update_user_info'),  # 修改用户信息
    (r'^add_user_info/$', 'add_user_info'),  # 新增用户信息
    (r'^get_specialist_group_by_science_type/$', 'get_specialist_group_by_science_type'),  # 获取专家，并对其进行分组
    (r'^get_project_statement/$', 'get_project_statement'),  # 获取项目报表
    (r'^project_specialist_html/$', 'project_specialist_html'),  # 报表页面
    (r'^test_html/$', 'test_html'),  # 测试页面
    (r'^user_login/$', 'user_login'),  # 用户登陆
    (r'^get_project_by_project_name/$', 'get_project_by_project_name'),  # 用户登陆
    (r'^project_list_html/$', 'project_list_html'),  # 用户登陆
    (r'^detail_project_html/$', 'detail_project_html'),  # 用户登陆
    (r'^login_out/$', 'login_out'),  # 用户注销

)
