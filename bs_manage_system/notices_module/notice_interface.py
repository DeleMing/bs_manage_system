# encoding:utf-8
from public_module.models import Notification
from django.core.paginator import Paginator
from public_module.public_tools import success_return
from public_module.public_tools import error_return
from django.forms.models import model_to_dict
import json
import math
import uuid
import datetime
from django.db import transaction


class NoticeInterface():
    """
    通知接口
    """

    @classmethod
    def get_notices(cls, page, page_size):
        """
        获取通知
        :param page:            页数
        :param page_size:
        :return:
        """
        result_list = []
        if page == 0:
            # 全部取出
            pass
        else:
            notices = Notification.objects.values().all().order_by('-create_time')
            paginator = Paginator(notices, page_size)
            temp_list = paginator.page(page)
            for i in temp_list:
                i['create_time'] = i['create_time'].strftime("%Y-%m-%d %H:%M:%S")
                i['page'] = page
                i['page_count'] = paginator.num_pages
                i['count'] = paginator.count

                result_list.append(i)
        return success_return(u'获取通知成功', result_list)

    @classmethod
    def insert_notice(cls, notification_title, notification_content, create_user_id):
        """

        :param notification_title:
        :param notification_content:
        :param create_user_id:
        :return:
        """
        notification_id = uuid.uuid1()
        try:
            # 添加事物控制防止异常时事物不回滚，这里事物必须放在try...catch里面
            # 否则事物被try...catch捕获了就不起作用了
            with transaction.atomic():
                Notification.objects.create(notification_id=notification_id, notification_title=notification_title,
                                            notification_content=notification_content, create_user_id=create_user_id)
            return success_return(u'发布通知成功', [])
        except Exception as e:
            return error_return(u'新增通知失败')

    @classmethod
    def get_notice_by_id(cls, notification_id):
        """
        通过通知ID获取通知信息
        :param notification_id:
        :return:
        """
        try:
            notice = Notification.objects.values().get(notification_id=notification_id)
            notice['create_time'] = notice['create_time'].strftime("%Y-%m-%d %H:%M:%S")
            return success_return(u'获取通知成功', notice)
        except Exception as e:
            return error_return(u'获取通知失败')
