from django.shortcuts import render

# Create your views here.
from django.contrib.auth.backends import ModelBackend
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework import mixins
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User



def jwt_response_payload_handler(token,user=None,request=None):
    # 通过用户user对象即可获取用户相关权限等其他信息
    return {
        'token':token,
        'user':user.username,
        'test':'test',
    }
# 自定义登陆验证
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except:
            return None

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它。
    """
    def has_object_permission(self, request, view, obj):
        # 读取权限被允许用于任何请求，
        # 所以我们始终允许 GET，HEAD 或 OPTIONS 请求。
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # 写入权限只允许给 snippet 的所有者。
        return obj.user == request.user