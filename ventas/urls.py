"""ventas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from ventasApp import views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("insert/", views.insert, name="insert"),
    path("update", views.update, name="update"),
    path("update/<int:task_id>", views.update_form, name="update_form"),
    path("delete/<int:task_id>", views.delete, name="delete"),
    path('register/', views.register, name='register'),
    path('',views.login,name="loginurl"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('logout/',logout_then_login,name = 'logout')
]
