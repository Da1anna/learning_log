# -*- coding:utf-8 -*-
# @Time: 2020/7/7 16:35
# @Author: Lj
# @File: forms.py

from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}