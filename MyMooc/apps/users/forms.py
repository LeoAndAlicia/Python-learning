# -*- coding:utf-8 -*-
__author__ = 'Leonardo'
__date__ = '2019/3/28 16:42'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
