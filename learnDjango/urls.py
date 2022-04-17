"""learnDjango URL Configuration

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

from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 例如：当用户访问www.xxx.com/index时，会进入index函数
    # 而函数写在view。py下
    path('index/', views.index),
    path('users/list/', views.user_list),
    path('users/add/', views.user_add),

    # 模板中心
    path('tpl/', views.tpl),

    #     联通新闻中心
    path('news/', views.news),

    #     请求和响应
    path('reandres/', views.reANDres),

    #     用户登录
    path('login/', views.login),

    # 测试orm操作MySQL数据库
    path('orm/', views.orm),

    # 案例：用户管理
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
    path('info/delete/', views.info_delete)

]
