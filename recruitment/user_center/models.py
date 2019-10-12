from django.db import models

# 账号信息表
class UserInfo(models.Model):
    # 手机号
    phone = models.CharField(max_length=11)
    #密码
    passwd = models.CharField(max_length=15)
    # 姓名
    name = models.CharField(max_length=20, null=True, default="小熊猫")
    # 邮箱
    email = models.CharField(max_length=80, null=True)
    # 用户属性
    priv = models.CharField(max_length=1, default="1")   # 1为个人用户，2为企业用户
    # 账号状态
    state = models.CharField(max_length=1, default="1")  # 1为正常， 2为冻结， 0表示已删除
    # 注册时间reg_time
    reg_time = models.DateField()

    def __str__(self):
        if self.priv == "1":
            return "个人：" + self.name
        elif self.priv == "2":
            return "企业：" + self.name
        return self.name
