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
]