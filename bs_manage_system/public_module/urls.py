# encoding:utf-8
from django.conf.urls import patterns

urlpatterns = patterns(
    'public_module.views',
    (r'^$', 'login_html'),  # 登录页面
)
