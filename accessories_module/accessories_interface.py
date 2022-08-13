# encoding:utf-8
from django.core.paginator import Paginator
from django.db import transaction

from public_module.public_tools import success_return
from public_module.public_tools import error_return
from public_module.models import Accessories


class AccessoriesInterface():
    """
    附件接口
    """

    def __init__(self):
        pass

    @classmethod
    def get_accessories_by_project_id(cls, project_id, page, page_size):
        """
        通过项目ID获取附件list 空则返回[]
        :param project_id:
        :param page:
        :param page_size:
        :return:
        """
        result_list = []
        if page == 0:

            try:
                accessories = Accessories.objects.values().filter(project_id=project_id).order_by('-accessories_time')
                for i in accessories:
                    i['accessories_time'] = i['accessories_time'].strftime("%Y-%m-%d %H:%M:%S")
                    result_list.append(i)
            except:
                pass
        else:
            accessories = Accessories.objects.values().filter(project_id=project_id).order_by('-accessories_time')
            paginator = Paginator(accessories, page_size)
            temp_list = paginator.page(page)
            for i in temp_list:
                i['accessories_time'] = i['accessories_time'].strftime("%Y-%m-%d %H:%M:%S")
                i['page'] = page
                i['page_count'] = paginator.num_pages
                i['count'] = paginator.count
                result_list.append(i)
        return success_return('获取附件成功', result_list)

    @classmethod
    def delete_accessories_by_accessories_id(cls, accessories_id):
        """
        通过附件ID删除附件
        :param accessories_id:
        :return:
        """
        try:
            exit_temp = Accessories.objects.filter(accessories_id=accessories_id)
            print exit_temp
            if len(exit_temp) != 0:
                temp = Accessories.objects.filter(accessories_id=accessories_id).delete()
                return success_return(u'删除成功', None)
            else:
                return error_return(u'附件不存在删除失败')
            # if temp is not None:
            #     return success_return(u'删除成功', None)
            # else:
            #     return error_return(u'附件不存在删除失败')
        except Exception as e:
            return error_return(u'删除失败' + str(e))

    @classmethod
    def insert_accessories(cls, project_id, accessories_id, accessories_name, accessories_url):
        """
        新增项目附件
        :param project_id:
        :param accessories_id:
        :param accessories_name:
        :param accessories_url:
        :return:
        """
        try:
            with transaction.atomic():
                Accessories.objects.create(project_id=project_id, accessories_id=accessories_id,
                                           accessories_name=accessories_name, accessories_url=accessories_url)
            return success_return(u'新增附件成功', None)
        except Exception as e:
            return error_return(u'新增附件失败' + str(e))
