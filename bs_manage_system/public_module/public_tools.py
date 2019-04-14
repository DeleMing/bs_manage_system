# encoding:utf-8


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
