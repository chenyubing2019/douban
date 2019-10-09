from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('reg1/', views.reg1),
    path('reg2/', views.reg2),
    path('', views.login),
    
]
