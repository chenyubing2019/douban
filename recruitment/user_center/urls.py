from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('reg1/', views.reg1),
    path('reg2/', views.reg2),
    path('', views.login),
    path("check_phone/", views.check_phone),     # 校验手机号
    path("send_yzm/", views.send_yzm),           # 发送验证码
    path("logout/", views.logout),
    
    
]
