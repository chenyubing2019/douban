from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
import requests
from django.utils import timezone #引入timezone模块


def login(request):
    if request.method == "GET":
        return render(request, "user_center/login.html")
    elif request.method == "POST":
        phone = request.POST.get("form-username")
        passw = request.POST.get("form-password")
        try:
            if models.UserInfo.objects.get(phone=phone).passw == passw:
                person = models.UserInfo.objects.get(phone=phone)
                return render(request, "user_center/index.html", {"person": person})
            else:
                return HttpResponse("用户名或密码不正确，登录失败！")
        except:
            return HttpResponse("登录失败")

def reg1(request):
     if request.method == "GET":
        return render(request, "user_center/reg1.html")
     elif request.method == "POST":
        # 手机号
        phone = request.POST.get("form-phone")
        
        # 验证码
        verify_code = request.POST.get("form-verify_code")

        # 企业还是个人
        priv = request.POST.get("priv")

        # 存到session
        request.session["phone"] = phone
        request.session["verify_code"] = verify_code
        request.session[phone] = verify_code
        request.session["priv"] = priv
        if verify_code == "123456":
            return redirect("../reg2")
        else:
            return HttpResponse("注册失败")
            
def reg2(request):
    if request.method == "GET":
        return render(request, "user_center/reg2.html")
    elif request.method == "POST":
        phone = str(request.session.get("phone"))
        check_phone_code = str(request.session.get(phone))
        verify_code = str(request.session.get("verify_code"))
        if check_phone_code == verify_code:
            # 第一个密码
            password1 = request.POST.get("form-password1")
            # 第二个密码
            password2 = request.POST.get("form-password2")
            if password1 == password2:
                time_now = timezone.now() # 输出time_now即为当然日期和时间
                priv = str(request.session.get("priv"))
                models.UserInfo(phone=phone, passw=password1, reg_time=time_now, priv=priv).save()
                return HttpResponse("注册成功")
            else:
                return HttpResponse("密码错误")
        else:
            return HttpResponse("验证码错误" + check_phone_code + " " + verify_code)