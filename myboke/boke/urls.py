from django.conf.urls import url
from .views import *
from django.urls import path


app_name = '[boke]'
urlpatterns = [
    path(r'bloglist/',BlogListView.as_view(),name='bloglist'),
    path(r'blogcreate/',BlogCreateView.as_view(),name='blogcreate'),
    path(r'blogdelete/',BlogDeleteView.as_view(),name='blogdelete'),
    path(r'commentcreate/',CommentCreateView.as_view(),name='commentcreate'),
    path(r'commentlist/',CommentListView.as_view(),name='commentlist'),
]