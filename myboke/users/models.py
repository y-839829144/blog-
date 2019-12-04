from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(models.Model):
    STATUS = (
        (1, '男'),
        (2, '女'),
        (3, '保密'),

    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    gender = models.IntegerField(choices=STATUS,verbose_name='用户性别')
    picture = models.ImageField(upload_to='uploads/user/%Y/',verbose_name='用户头像')