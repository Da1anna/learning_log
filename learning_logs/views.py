# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """学习笔记项目的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """显示某个主题及其具体内容"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')   #-号表示降序
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)
