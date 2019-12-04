from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class BlogType(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名称')
    level = models.IntegerField(verbose_name='分类级别')
    uper_type = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='上级编号', null=True, blank=True,
                                  related_name='sonm')

    class Meta():
        verbose_name = '博客分类表'

    def __str__(self):
        return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=20,verbose_name='标签名称')

    class Meta:
        verbose_name = '博客标签表'

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=30,verbose_name='博客标题')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='博客作者')
    content = models.TextField(max_length=255,verbose_name='发表内容')
    pbtime = models.DateTimeField(auto_now_add=True,verbose_name='发表时间')
    blogtype = models.ForeignKey(BlogType,verbose_name='博客类别',on_delete=models.CASCADE)
    blogtag = models.ManyToManyField(BlogTag,verbose_name='博客标签')
    one_typename = models.ForeignKey('BlogType', on_delete=models.CASCADE, related_name='one', null=True, blank=True)
    two_typename = models.ForeignKey('BlogType', on_delete=models.CASCADE, related_name='two', null=True, blank=True)
    three_typename = models.ForeignKey('BlogType', on_delete=models.CASCADE, related_name='three', null=True,
                                       blank=True)

    class Meta:
        verbose_name = '博客表'

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,verbose_name='博客',on_delete=models.CASCADE)
    name = models.CharField('称呼',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=240)
    pbtime = models.DateTimeField(auto_now_add=True,verbose_name='发表时间')

    class Meta:
        verbose_name = '评论表'

    def __str__(self):
        return self.content