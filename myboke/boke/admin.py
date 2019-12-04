from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Blog)
admin.site.register(BlogType)
admin.site.register(BlogTag)
admin.site.register(Comment)

