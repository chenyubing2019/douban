from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
import random, urllib.parse, urllib.request
from .models import UserInfo
import json
import requests
from django.utils import timezone #引入timezone模块


def logout(request):
    del request.session["person"]
    return redirect("../")


def login(request):
    if request.method == "GET":
        return render(request, "user_center/login.html")
    elif request.method == "POST":
        phone = request.POST.get("form-username")
        passwd = request.POST.get("form-password")
        # print(phone ,type(phone),passw, type(phone))
        try:
            if models.UserInfo.objects.get(phone=phone).passwd == passwd:
                person = models.UserInfo.objects.get(phone=phone)
                # 登录后的session值
                request.session["person"] = {
                    "phone": person.phone,
                    "name": person.name,
                    "state": person.priv
                }
                return redirect("../")
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
        verify_code = request.POST.get("form-verify_code")     # 从前端接收的验证码

        # 企业还是个人
        priv = request.POST.get("priv")

        # 存到session
        request.session["phone"] = phone
        request.session["verify_code"] = verify_code
        request.session[phone] = verify_code      # 有疑问
        request.session["priv"] = priv

        ver = str(request.session.get(phone))     # 得到系统发送给手机号的验证码
        if verify_code == ver:
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
                models.UserInfo(phone=phone, passwd=password1, reg_time=time_now, priv=priv).save()
                return HttpResponse("注册成功,<a href='../'>去登陆</a>")
            else:
                return HttpResponse("密码错误")
        else:
            return HttpResponse("验证码错误" + check_phone_code + " " + verify_code)


# 校验手机号
def check_phone(request):
    rsp = {}
    phone = request.GET.get("phone")  # 获取手机号
    # print(phone)
    if UserInfo.objects.filter(phone=phone):
        rsp["err"] = 1    # 手机号已注册
    else:
        rsp["err"] = 0   # 手机号未注册
    return HttpResponse(json.dumps(rsp), content_type="application/json")

# 发送验证码
def send_sms_code(phone):
    '''
    函数功能：发送短信验证码（6位随机数字）
    函数参数：
    phone 接收短信验证码的手机号
    返回值：发送成功返回验证码，失败返回False
    '''
    verify_code = str(random.randint(100000, 999999))
    try:
        url = "http://v.juhe.cn/sms/send"
        params = {
            "mobile": phone,  # 接受短信的用户手机号码
            "tpl_id": "162901",  # 您申请的短信模板ID，根据实际情况修改
            "tpl_value": "#code#=%s" % verify_code,  # 您设置的模板变量，根据实际情况修改
            "key": "ab75e2e54bf3044898459cb209b195e4",  # 应用APPKEY(应用详细页查询)
        }
        params = urllib.parse.urlencode(params).encode()

        f = urllib.request.urlopen(url, params)
        content = f.read()
        res = json.loads(content)

        # print(res)

        if res and res['error_code'] == 0:
            return verify_code
        else:
            return False
    except:
        return False

# 发送验证码及给前端响应
def send_yzm(request):
    phone = request.GET.get("phone")
    result = {"err": 1, "desc": "内部错误！"}
    # verify_code = send_sms_code(phone)   # 真验证码
    verify_code = "123456"   # 假验证码
    if verify_code:
        # 发送短信验证码成功
        request.session[phone] = verify_code  # session值， 如果发送成功为验证码
        result["err"] = 0
        result["desc"] = "发送短信验证码成功！"
    # print(result)
    return HttpResponse(json.dumps(result), content_type="application/json")
