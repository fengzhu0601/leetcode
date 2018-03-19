#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = 'fengzhu'
__date__ = '18-3-19 下午3:06'


# 引入Django表单
from django import forms

# 登录表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
