# encoding:utf-8
from public_module.mymako import render_mako_context


def success_return(message, results):
    """
    成功返回
    :param message:     信息
    :param results:     结果集
    :return:            0成功
    """
    return {
        'code': 0,
        'message': message,
        'results': results,
    }


def error_return(message):
    """
    错误放回
    :param message:     信息
    :return:
    """
    return {
        'code': 1,
        'message': message,
    }


def auth_skip(request, user_type):
    """
    权限跳转
    :param request:
    :param user_type: 用户类型 0超管 1申请人 2审批专家
    :return:
    """
    if user_type == 0:
        return render_mako_context(request, 'common/admin_main.html')
    if user_type == 1:
        return render_mako_context(request, 'common/apply_main.html')
    if user_type == 2:
        return render_mako_context(request, 'common/review_main.html')
