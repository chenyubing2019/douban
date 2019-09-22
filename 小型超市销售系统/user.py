import pymysql
from  crud import  inquire,add,delete,revise

def user_chart():
    '''
        函数功能：查看用户所有信息
    '''
    try:
        r=inquire('userinfo')
        for i in r:
            uid = i[0]
            uname = i[1]
            sex = i[2]
            Tdata = i[3]
            balance = i[4]
            print("编号:%s,名字:%s,性别:%s,注册日期:%s,余额:%s元"%(uid,uname,sex,Tdata,balance))
    except:
        print("数据库出错")

def user_add():
    '''
        函数功能：添加用户
     '''
    while(True):
        i = int(input("请输入用户id:"))
        n = input("请输入用户名字:")
        s = input("请输入用户性别:")
        t = input("请输入注册日期:")
        b = int(input("请输入余额:"))
        j = (i, n, s, t, b)
        r = add('userinfo',j)
        break

def user_delete():
    '''
        函数功能：删除用户
    '''
    j=input("请输入要删除用户的编号：")
    n= input("请输入要删除用户的编号：")
    delete('userinfo',j,n)

def user_revise():
    '''
        函数功能：修改用户
    '''
    b=int(input("请输入要修改的用户的ID："))
    print("可修改的位置为：编号：uid，名字：uname，性别：sex，注册日期：Tdata，余额：balance")
    j=input("请输入要修改的位置：")
    c=input("请输入要修改的内容:")
    if j != 'balance':
         c='\''+c+'\''
    revise('userinfo',j,c,'uid',b)

