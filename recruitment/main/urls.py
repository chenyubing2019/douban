from django.urls import path
from django.conf.urls import url
from . import views
import re

urlpatterns = [
    path('', views.index),
    path("person/", views.personinfo),              # 个人资料管理
    path("company/", views.companyinfo),            # 公司资料管理
    path("resume/", views.resume),                  # 填写简历信息
    path("postjob/", views.postjob),                # 录入招聘信息
    url(r'^detail/(?P<id>[0-9]+)$', views.job_detail, name='detail'),              # 显示招聘详情
]
