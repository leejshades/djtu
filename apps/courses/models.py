# coding=utf-8
from __future__ import unicode_literals
from django.db import  models
from datetime import datetime


class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'课程名字')
    desc = models.CharField(max_length=300,verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(choices=(('cj',u'初级'),('zj',u'中级'),('gj',u'高级')),max_length=3,verbose_name='课程难度')
    learn_times = models.IntegerField(default=0,verbose_name=u'学习时长(分钟)')
    students = models.IntegerField(default=0,verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='course/%Y/%m',verbose_name=u'封面图',max_length=200)
    click_nums = models.IntegerField(default=0,verbose_name=u'点击数字')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name
    def __unicode__(self):

        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'课程')
    name = models.CharField(max_length=100,verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name


class Viedo(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u'章节')
    name = models.CharField(max_length=100,verbose_name=u'视频名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name



class CourseResource(models.Model):
    course = models.ForeignKey(Lesson,verbose_name=u'课程')
    name = models.CharField(max_length=100,verbose_name=u'资源名')
    download = models.FileField(upload_to='course/resource/%Y/%m',verbose_name=u'资源文件',max_length=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'资源'
        verbose_name_plural = verbose_name
