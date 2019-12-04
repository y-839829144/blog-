from django_filters import rest_framework
from .models import *
# 自定义过滤器
class CommentFilter(rest_framework.FilterSet):
    time_min = rest_framework.DateTimeFilter(field_name='pdtime',lookup_expr='gte')
    time_max = rest_framework.DateTimeFilter(field_name='pdtime',lookup_expr='lte')

    class Meta:
        model = Comment
        fields = ['time_min','time_max','blog_id']
