"""myboke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
import rest_framework.authtoken.views
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='杨泽博客 API')
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/', obtain_jwt_token),
    url(r'^api/', schema_view),
    path(r'boke/', include('boke.urls', namespace='boke')),
    path(r'users/', include('users.urls', namespace='users')),
]
