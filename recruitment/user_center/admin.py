from django.contrib import admin
from . import models as userm
from main import models as mainm
admin.site.register(userm.UserInfo)
admin.site.register(mainm.PersonInfo)
admin.site.register(mainm.CompanyInfo)
admin.site.register(mainm.PostJob)