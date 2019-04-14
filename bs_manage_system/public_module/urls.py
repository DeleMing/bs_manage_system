# encoding:utf-8
from django.conf.urls import patterns

urlpatterns = patterns(
    'public_module.views',
    (r'^$', 'login_html'),  # 登录页面
    (r'^main/$', 'main_html'),  # 主页
    (r'^user_login/$', 'user_login'),  # 登陆
)
