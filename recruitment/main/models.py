from django.db import models
from user_center.models import UserInfo

# Create your models here.
class PositionTable(models.Model):
    name = models.CharField(max_length=20)
    total = models.CharField(max_length=20)  # 总分类
    next = models.CharField(max_length=20)  # 次分类

# 个人资料表
class PersonInfor(models.Model):
    # 手机号,unique=True 唯一属性，个人信息，为UserInfor表的外键
    # phone = models.ForeignKey(UserInfo, to_field="phone", on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, null=True)
    # 姓名
    name = models.CharField(max_length=20, null=True)
    # 性别
    sex = models.CharField(max_length=20, null=True)
    # 生日
    birthday = models.DateField(null=True)
    # 所在地区
    area = models.CharField(max_length=50, null=True)
    # 邮箱
    email = models.CharField(max_length=80, null=True)
    # 是否为学生
    student = models.CharField(max_length=4, null=True)
    # 参加工作时间
    worktime = models.CharField(max_length=30, null=True)
    # 学校
    school = models.CharField(max_length=40, null=True)
    # 入学时间
    admdate = models.DateField(null=True)
    # 毕业时间
    gradtime = models.DateField(null=True)
    # 专业
    prof = models.CharField(max_length=50, null=True)
    # 学历
    education = models.CharField(max_length=50, null=True)
    # 标签
    # label = models.CharField(max_length=60, null=True)
    # 自我描述(selfdes): 150
    selfdes = models.CharField(max_length=150, null=True)
    # 社交主页(shejiao): 如GitHub的url
    shejiao = models.CharField(max_length=200, null=True)
    # 工作类型(type_work): python / java
    type_work = models.CharField(max_length=50, null=True)
    # 工作性质(nature_work)：实习/全职
    nature_work = models.CharField(max_length=20, null=True)
    # 期望薪资(expecte_salary)
    expecte_salary = models.CharField(max_length=20, null=True)
    # 最低薪资(low_salary)
    low_salary = models.CharField(max_length=20, null=True)
    # 期望工作城市(work_city)
    work_city = models.CharField(max_length=30, null=True)
    # 当前状态(state)
    state = models.CharField(max_length=30, null=True)
    # 可工作时间(available_time)
    available_time = models.CharField(max_length=30, null=True)


class EnterRec(models.Model):    #公司招聘信息表
    name = models.CharField(max_length=30) #公司名
    recruitment = models.CharField(max_length=40) #招募的职业
    pay = models.CharField(max_length=20) #薪资待遇
    area = models.CharField(max_length=20) #工作城市
    experience = models.CharField(max_length=20) #工作经验
    education = models.CharField(max_length=20) #学历
    post = models.CharField(max_length=10) #职位要求（全职，兼职，实习）
    attract = models.TextField(max_length=500) #职业诱惑
    describe = models.TextField(max_length=600) #职位描述
    workplace = models.CharField(max_length=60) #工作地点
    time = models.DateField(auto_now=True) #发布时间



