from django.db import models
from user_center.models import UserInfo

# 职位表
class WorkTable(models.Model):
    name = models.CharField(max_length=20)      # 职位名
    total = models.CharField(max_length=20)     # 总分类
    next = models.CharField(max_length=20)      # 次分类
    
    def __str__(self):
        return self.name

# 个人资料表
class PersonInfo(models.Model):
    # 手机号,unique=True 唯一属性，个人信息，为UserInfo表的外键
    # phone = models.ForeignKey(UserInfo, to_field="phone", on_delete=models.CASCADE)
    # phone = models.CharField(max_length=11, null=True)
    
    # ------------------账号资料------------------
    # 手机号
    phone = models.CharField(max_length=11)
    
    # # 密码
    # password = models.CharField(max_length=16)
    
    # # 邮箱
    # email = models.CharField(max_length=80, null=True)
    
    
    # ------------------基本资料------------------
    # 姓名
    name = models.CharField(max_length=10, default="小熊猫")
    
    # 年龄
    age = models.CharField(max_length=3, default=0)

    # 性别
    sex = models.CharField(max_length=20, default=1)    # 1为男 2为女
    
    # 学校
    school = models.CharField(max_length=40, null=True)
    
    # 专业
    prof = models.CharField(max_length=50, null=True)
    
    # 学历
    education = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.phone

# 公司资料表
class CompanyInfo(models.Model):

    # 手机号
    phone = models.CharField(max_length=11)

    # 公司名
    name = models.CharField(max_length=32)

    # 公司地址
    address = models.CharField(max_length=60)

    # 营业执照号码
    business_id = models.CharField(max_length=32)

    # 经济性质
    group = models.CharField(max_length=32)

    # 法人代表
    legal_person = models.CharField(max_length=10)

    # 注册资金
    reg_fund = models.CharField(max_length=15)

    # 人员规模
    staff_scale = models.CharField(max_length=10)

    # 成立时间
    establishd_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

# 公司招聘表
class PostJob(models.Model):

    # 公司手机号
    phone = models.CharField(max_length=11)

    # 公司名
    name = models.CharField(max_length=32)

    # 招募的职业   
    recruitment = models.CharField(max_length=40)

    # 薪资待遇
    pay = models.CharField(max_length=20)          

    # 工作城市 
    area = models.CharField(max_length=20)          

    # 工作经验
    experience = models.CharField(max_length=20)    

    # 学历
    education = models.CharField(max_length=20)     

    # 职位要求
    post = models.CharField(max_length=10)              # 全职，兼职，实习

    # 职业诱惑
    attract = models.TextField(max_length=500)      

    # 职位描述
    describe = models.TextField(max_length=600)     

    # 工作地点
    workplace = models.CharField(max_length=60)     

    # 发布时间
    time = models.DateField(auto_now=True)          
    def __str__(self):
        return self.name

# 个人简历表
class ResumeInfo(models.Model):
    # 所在地区
    area = models.CharField(max_length=50, null=True)
    
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






