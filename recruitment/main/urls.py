from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("pinfo", views.Person_Infor),  # 添加个人资料的url
]
