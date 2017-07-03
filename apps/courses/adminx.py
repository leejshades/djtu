# coding=utf-8
__author__ = 'ljs'
__date__ = '2017/3/13 10:36'


from  .models import Course,Lesson,Viedo,CourseResource
import xadmin

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']
class LessonAdmin(object):

    list_display = ['name','course','add_time']
    search_fields = ['name','course']
    list_filter = ['name','course__name','add_time']
class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['name', 'lesson', 'add_time']
class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download','add_time']
    search_fields = ['course', 'name','download']
    list_filter = ['name', 'course', 'download','add_time']

xadmin.site.register(Viedo,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Course,CourseAdmin)