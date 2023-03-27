from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("ventas.urls")),
    path('admin/', admin.site.urls),
]