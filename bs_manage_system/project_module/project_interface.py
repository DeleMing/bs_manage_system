# encoding:utf-8
from django.db import transaction
from public_module.models import Project
from public_module.public_tools import success_return
from public_module.public_tools import error_return
import uuid


class ProjectInterface():
    """
    项目接口
    """

    def __init__(self):
        pass

    @classmethod
    def insert_project(cls, project_name, project_time, apply_user_name, apply_user_id, research_content,
                       technology_new, expected_goal, participator, start_time, stop_time):
        """
        新增项目信息
        :param project_name:
        :param project_time:
        :param apply_user_name:
        :param apply_user_id:
        :param research_content:
        :param technology_new:
        :param expected_goal:
        :param participator:
        :param start_time:
        :param stop_time:
        :return:
        """
        project_id = uuid.uuid1()
        try:
            with transaction.atomic():
                Project.objects.create(project_id=project_id, project_name=project_name, project_time=project_time,
                                       apply_user_name=apply_user_name, apply_user_id=apply_user_id,
                                       research_content=research_content, technology_new=technology_new,
                                       expected_goal=expected_goal, participator=participator, start_time=start_time,
                                       stop_time=stop_time, project_status=0)
            return success_return(u'新增项目成功', {'project_id': str(project_id)})
        except Exception as e:
            return error_return(u'新增项目失败' + str(e))

    @classmethod
    def change_project_status(cls, project_id, project_status):
        """
        更改项目状态
        :param project_id:
        :param project_status:
        :return:
        """
        try:
            with transaction.atomic():
                Project.objects.filter(project_id=project_id).update(project_status=project_status)
            return success_return(u'修改状态成功', None)
        except Exception as e:
            return error_return(u'修改项目状态失败')

    @classmethod
    def get_project_by_id(cls):
        pass

    @classmethod
    def get_project_by_status(cls):
        pass

    @classmethod
    def get_project_by_id_status(cls):
        pass

    @classmethod
    def get_project_by_user_id(cls):
        pass
