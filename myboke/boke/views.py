from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import mixins
from .models import *
from .serializers import *
from .Schemas import *
from .filters import *
# Create your views here.


class BlogListView(generics.ListAPIView):
    """
    博客列表
    """
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializers

    def get_queryset(self):
        queryset = Blog.objects.all()
        return queryset

class BlogCreateView(generics.CreateAPIView):
    """
    新增博客  注意：blogtag的类型为int
    """
    serializer_class = BlogListSerializers
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try: # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            return Response(data={'code':400,'message':'创建失败'},status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        # 成功后返回信息的定制
        res.data['code'] = 200
        res.data['message'] = '创建成功'
        return res
class BlogDeleteView(generics.GenericAPIView):
    """
   博客删除
    """
    schema = BlogListSchema
    serializer_class = BlogListSerializers
    # 重写destory方法 ，自定义返回结果
    def get(self,request):
        # 获取地址url中的参数
        try:
            Blog.objects.get(pk=self.request.query_params.get('id')).delete() # 使用get获取单条数据 ,使用filter会获取一个列表 列表为空不会报错
        except:
            return Response(data={'code':400,'message':'删除失败'},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code':200,'message':'删除成功'},status=status.HTTP_200_OK)

class CommentListView(generics.ListAPIView):
    """
    评论列表
    """
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializers
    schema = CommentListSchema
    filter_backends = (DjangoFilterBackend,)
    filter_class = CommentFilter



class CommentCreateView(generics.CreateAPIView):
    """
    新增评论
    """
    serializer_class = CommentListSerializers
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try: # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            return Response(data={'code':400,'message':'创建失败'},status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        # 成功后返回信息的定制
        res.data['code'] = 200
        res.data['message'] = '创建成功'
        return res


class CommentDeleteView(generics.GenericAPIView):
    """
   评论删除
    """
    schema = CommentListSchema
    serializer_class = CommentListSerializers

    # 重写destory方法 ，自定义返回结果
    def get(self, request):
        # 获取地址url中的参数
        try:
            Blog.objects.get(pk=self.request.query_params.get('id')).delete()  # 使用get获取单条数据 ,使用filter会获取一个列表 列表为空不会报错
        except:
            return Response(data={'code': 400, 'message': '删除失败'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'message': '删除成功'}, status=status.HTTP_200_OK)