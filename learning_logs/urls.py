# -*- coding:utf-8 -*-
# @Time: 2020/7/7 10:06
# @Author: Lj
# @File: urls.py

""" 定义 learning_logs 的 URL 模式 """

from django.conf.urls import url

from . import views

urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),
    #主题页
    url(r'^topics/$', views.topics, name='topics'),
    #具体主题
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #添加新主题
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #添加新条目
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #编辑既有条目
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]