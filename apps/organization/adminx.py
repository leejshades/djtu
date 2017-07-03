# coding=utf-8
__author__ = 'ljs'
__date__ = '2017/3/13 10:56'

from .models import CourseOrg,CityDict,Teacher
import  xadmin

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums','fav_nums','image','address','city','add_time']
    search_fields = ['name', 'desc', 'click_nums','fav_nums','image','address','city']
    list_filter = ['name', 'desc', 'click_nums','fav_nums','image','address','city','add_time']
class TeacherAdmin(object):
    list_display = ['name', 'org', 'add_time','work_years','work_company','work_position','point','click_nums','fav_nums']
    search_fields = ['name', 'org','work_years','work_company','work_position','point','click_nums','fav_nums']
    list_filter = ['name', 'org', 'add_time','work_years','work_company','work_position','point','click_nums','fav_nums']
xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)