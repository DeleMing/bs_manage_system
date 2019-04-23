# encoding:utf-8
from django.db import transaction
from public_module.models import Review
from public_module.public_tools import success_return
from public_module.public_tools import error_return
import datetime


class ReviewInterface():
    """
    评审表接口
    """

    def __init__(self):
        pass

    @classmethod
    def init_review(cls, review_id, project_id, review_user_id, review_user_name):
        """
        初始化项目评审信息
        :param review_id:
        :param project_id:
        :param review_user_id:
        :param review_user_name:
        :return:
        """
        try:
            # review_status: 0未审批 1审批通过 2审批完成
            with transaction.atomic():
                Review.objects.create(review_id=review_id, project_id=project_id, review_user_id=review_user_id,
                                      review_status=0, review_user_name=review_user_name)
            return success_return(u'新增评审信息成功', None)
        except Exception as e:
            return error_return(u'新增评审信息失败')

    @classmethod
    def update_review(cls, review_id, review_message, review_status):
        """
        更新评审信息
        :param review_id:
        :param review_message:
        :param review_status:
        :return:
        """
        try:
            with transaction.atomic():
                Review.objects.filter(review_id=review_id).update(review_status=review_status,
                                                                  review_message=review_message,
                                                                  review_time=datetime.datetime.now())
            return success_return(u'修改评审信息成功', None)
        except Exception as e:
            return error_return(u'修改评审信息失败')

    @classmethod
    def delete_review(cls, review_id):
        """
        删除评审信息
        :param review_id:
        :return:
        """
        try:
            with transaction.atomic():
                Review.objects.get(review_id=review_id).delete()
            return success_return(u'删除成功', None)
        except Exception as e:
            return error_return(u'删除失败')

    @classmethod
    def get_review_list_by_user_id(cls, review_user_id):
        """
        通过评审员ID获取评审List
        :param review_user_id:
        :return:
        """
        result_list = []
        review = Review.objects.values().filter(review_user_id=review_user_id).order_by('-review_time')
        for i in review:
            i['review_time'] = i['review_time'].strftime("%Y-%m-%d %H:%M:%S")
            result_list.append(i)
        return success_return(u'获取评审信息列表成功', result_list)

    @classmethod
    def get_review_list_by_project_id(cls, project_id):
        """
        通过项目ID获取审批信息
        :param project_id:
        :return:
        """
        result_list = []
        review = Review.objects.values().filter(project_id=project_id).order_by('-review_time')
        for i in review:
            i['review_time'] = i['review_time'].strftime("%Y-%m-%d %H:%M:%S")
            result_list.append(i)
        return success_return(u'获取评审信息列表成功', result_list)