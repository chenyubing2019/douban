from django.db import models

# Create your models here.


# Create your models here.
# 用户信息表
class UserInfor(models.Model):
    # 用户ID
    id = models.AutoField(primary_key=True)
    # 手机号
    phone = models.CharField(max_length=11)
    # 姓名
    name = models.CharField(max_length=20)
    # 头像
    portrait = models.CharField(max_length=200)
    # 生日
    birthday = models.DateField(null=True)
    # 所在地区
    area = models.CharField(max_length=50, null=True)
    # 邮箱
    email = models.CharField(max_length=80)
    # 是否为学生
    student = models.CharField(max_length=4)
    # 参加工作时间
    worktime = models.DateField()
    # 学校
    school = models.CharField(max_length=40)
    # 入学时间
    admdate = models.DateField()
    # 毕业时间
    gradtime = models.DateField()
    # 专业
    prof = models.CharField(max_length=50)
    # 学历
    education = models.CharField(max_length=50)
    # 标签
    label = models.CharField(max_length=60, null=True)
    # 自我描述(selfdes): 150
    selfdes = models.CharField(max_length=150, null=True)
    # 社交主页(shejiao): 如GitHub的url
    shejiao = models.CharField(max_length=200, null=True)
    # 工作类型(type_work): python / java
    type_work = models.CharField(max_length=50)
    # 工作性质(nature_work)：实习/全职
    nature_work = models.CharField(max_length=20)
    # 期望薪资(expecte_salary)
    expecte_salary = models.CharField(max_length=20)
    # 最低薪资(low_salary)
    low_salary = models.CharField(max_length=20)
    # 期望工作城市(work_city)
    work_city = models.CharField(max_length=30)
    # 当前状态(state)
    state = models.CharField(max_length=30)
    # 可工作时间(available_time)
    available_time = models.DateField()
    # 注册时间reg_time
    reg_time = models.DateField()

class Ebterprise (models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30) #职位
    email = models.CharField(max_length=80) #邮箱
    cname = models.CharField(max_length=50) #公司全称
    logo = models.ImageField(upload_to="recruitment/%Y/%m/%d/") #公司logo
    aname = models.CharField(max_length=30) #公司简称
    domain = models.CharField(max_length=30) #行业领域
    scale = models.CharField(max_length=30) #公司规模
    phases = models.CharField(max_length=30) #发展阶段
    welfare = models.CharField(max_length=30) #公司福利