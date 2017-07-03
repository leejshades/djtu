# coding=utf-8
__author__ = 'ljs'
__date__ = '2017/3/13 11:05'

from .models import UserAsk,UserCourse,UserFavorite,UserMessage,CourseComment
import  xadmin

class UserAskAdmin(object):
    list_display = ['name', 'moble', 'add_time','course_name']
    search_fields = ['name', 'moble','course_name']
    list_filter = ['name', 'moble', 'add_time','course_name']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'add_time','fav_type']
    search_fields = ['user', 'fav_id','fav_type']
    list_filter = ['user', 'fav_id', 'add_time','fav_type']

class UserMessageAdmin(object):
    list_display = ['user', 'message', 'add_time','has_read']
    search_fields = ['user', 'message','has_read']
    list_filter = ['user', 'message', 'add_time','has_read']


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'add_time','comments']
    search_fields = ['user', 'course','comments']
    list_filter =  ['user', 'course', 'add_time','comments']


xadmin.site.register(CourseComment,CourseCommentAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserAsk,UserAskAdmin)

