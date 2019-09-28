import socket
import json
import hashlib
import os


def get_file_md5(file_path):
    m = hashlib.md5()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(1024)
            if len(data) == 0:
                break
            m.update(data)
    return m.hexdigest().upper()

def enter():     #登录信息
    user_name=input("请输入用户名：")
    user_password=hashlib.md5(input("请输入密码：").encode()).hexdigest().upper()  #密码 md5
    data=json.dumps({"op":1,"args":{"uname":user_name,"passwd":user_password}})
    user_message = str(len(data)).ljust(15," ")+data  #用户信息加json数据
    return user_message.encode()

def register():     #注册信息
    user_name=input("请输入用户名：")
    user_password=hashlib.md5(input("请输入密码：").encode()).hexdigest().upper()  #密码 md5
    user_phone=input("请输入手机号:")
    user_email=input("请输入邮箱:")
    data=json.dumps({"op":2,"args":{"uname":user_name,"passwd":user_password,"phone":user_phone,"email":user_email}})
    user_message = str(len(data)).ljust(15," ")+data  #用户信息加json数据
    return user_message.encode()

def verify(): #用户名校验信息
    user_name = input("请输入用户名：")
    data = json.dumps({"op": 3, "args": {"uname": user_name}})
    user_message = str(len(data)).ljust(15, " ") + data  # 用户信息加json数据
    return user_message.encode()

def main():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("192.168.10.156", 9999))
        i=int(input("欢迎使用\n1.登录并下载\n2.注册用户\n3.用户校验\n4.退出\n请选择:"))
        if i == 1: #登录
            sock.send(enter())
            file_size = sock.recv(15).decode().rstrip()
            file_json = json.loads(sock.recv(int(file_size)))
            if file_json['error_code'] == 0:   #登录成功 下载文件
                while True:
                    file_path = sock.recv(300).decode().rstrip()  # 路径
                    print(file_path)
                    if len(file_path) == 0:
                        break
                    file_size = sock.recv(15).decode().rstrip()  # 文件大小
                    if len(file_size) == 0:
                        break
                    file_size = int(file_size)

                    file_md5 = sock.recv(32).decode()
                    if len(file_md5) == 0:
                        break
                    # 如果为空文件夹
                    if file_size == -1:
                        print("\n成功接收空文件夹 %s" % file_path)
                        os.makedirs(file_path, exist_ok=True)
                        continue
                    file_name = os.path.basename(file_path)  # 文件名字
                    #if file_path[-4:]!=".zip":
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # 创建文件夹

                    f = open(file_path, "wb")  # 在指定路径创建文件
                    copy_size = 0
                    while copy_size < file_size:
                        data = sock.recv(file_size - copy_size)  # 防粘包
                        if data == 0:
                            break
                        f.write(data)
                        copy_size += len(data)
                    f.close()

                    recv_file_md5 = get_file_md5(file_path)
                    if recv_file_md5 == file_md5:  # md5值对比查看是否传输错误
                        print("成功接收", file_name)
                    else:
                        print("文件%s接收失败" % file_path)
                sock.close()
            if file_json['error_code'] == 1:    #登录响应
                print("登录失败 返回主界面")
        if i == 2: #注册
            sock.send(register())
            file_size = sock.recv(15).decode().rstrip()
            file_json = json.loads(sock.recv(int(file_size)))
            if file_json['error_code'] ==0:
                print("注册成功 返回主界面")
            if file_json['error_code'] ==1:
                print("注册失败 返回主界面")
        if i== 3:    #用户校验
            sock.send(verify())
            file_size = sock.recv(15).decode().rstrip()
            file_json = json.loads(sock.recv(int(file_size)))
            if file_json['error_code'] == 0:
                print("用户不存在 返回主界面")
            if file_json['error_code'] == 1:
                print("用户已存在 返回主界面")
        if i == 4:   #退出
            sock.close()
            print("欢迎下次使用")
            break
        if  i > 4 or i < 1:
            print("请选择有效选项")

if __name__ == '__main__':
    main()