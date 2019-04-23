# encoding:utf-8
from django.core.paginator import Paginator
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
    def get_project_by_user_id(cls, apply_user_id, page, page_size):
        """
        通过用户ID获取项目列表(List)
        :param apply_user_id:
        :param page:
        :param page_size:
        :return:
        """
        result_list = []
        if page == 0:

            try:
                project = Project.objects.values().filter(apply_user_id=apply_user_id).order_by('-project_time')
                for i in project:
                    i['project_time'] = i['project_time'].strftime("%Y-%m-%d %H:%M:%S")
                    i['start_time'] = i['start_time'].strftime("%H:%M:%S")
                    i['stop_time'] = i['stop_time'].strftime("%H:%M:%S")
                    result_list.append(i)
            except:
                pass
        else:
            project = Project.objects.values().filter(apply_user_id=apply_user_id).order_by('-project_time')
            paginator = Paginator(project, page_size)
            temp_list = paginator.page(page)
            for i in temp_list:
                i['project_time'] = i['project_time'].strftime("%Y-%m-%d %H:%M:%S")
                i['start_time'] = i['start_time'].strftime("%H:%M:%S")
                i['stop_time'] = i['stop_time'].strftime("%H:%M:%S")
                i['page'] = page
                i['page_count'] = paginator.num_pages
                i['count'] = paginator.count
                result_list.append(i)
        return success_return('获取申请成功', result_list)

    @classmethod
    def get_project_by_status(cls, project_status, page, page_size):
        """
        通过项目状态获取项目列表
        :param project_status:
        :param page:
        :param page_size:
        :return:
        """
        result_list = []
        if page == 0:

            try:
                project = Project.objects.values().filter(project_status=project_status).order_by('-project_time')
                for i in project:
                    i['project_time'] = i['project_time'].strftime("%Y-%m-%d %H:%M:%S")
                    i['start_time'] = i['start_time'].strftime("%H:%M:%S")
                    i['stop_time'] = i['stop_time'].strftime("%H:%M:%S")
                    result_list.append(i)
            except:
                pass
        else:
            project = Project.objects.values().filter(project_status=project_status).order_by('-project_time')
            paginator = Paginator(project, page_size)
            temp_list = paginator.page(page)
            for i in temp_list:
                i['project_time'] = i['project_time'].strftime("%Y-%m-%d %H:%M:%S")
                i['start_time'] = i['start_time'].strftime("%H:%M:%S")
                i['stop_time'] = i['stop_time'].strftime("%H:%M:%S")
                i['page'] = page
                i['page_count'] = paginator.num_pages
                i['count'] = paginator.count
                result_list.append(i)
        return success_return(u'获取申请成功', result_list)

    @classmethod
    def get_project_by_project_id_list(cls, project_id_list, page, page_size):
        """

        :param project_id_list:
        :param page:
        :param page_size:
        :return:
        """
        result_list = []
        if page == 0:

            try:
                project = Project.objects.values().filter(project_id__in=project_id_list).order_by('-project_time')
                for i in project:
                    i['project_time'] = i['project_time'].strftime("%Y-%m-%d %H:%M:%S")
                    i['start_time'] = i['start_time'].strftime("%H:%M:%S")
                    i['stop_time'] = i['stop_time'].strftime("%H:%M:%S")
                    result_list.append(i)
            except:
                pass
        else:
            project = Project.objects.values().filter(project_status=project_status).order_by('-project_time')
            paginator = Paginator(project, page_size)
            temp_list = paginator.page(page)
            for i in temp_list:
                i['project_time'] = i['project_time'].strftime("%Y-%m-%d %H:%M:%S")
                i['start_time'] = i['start_time'].strftime("%H:%M:%S")
                i['stop_time'] = i['stop_time'].strftime("%H:%M:%S")
                i['page'] = page
                i['page_count'] = paginator.num_pages
                i['count'] = paginator.count
                result_list.append(i)
        return success_return(u'获取申请成功', result_list)

    @classmethod
    def get_project_by_id(cls):
        pass

    @classmethod
    def get_project_by_id_status(cls):
        pass


