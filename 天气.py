import socket
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

sock = socket.socket()
sock.connect(("www.tianqi.com",80))
req="GET /wuhan//mingtian/?qd=tq15 HTTP/1.1\r\nConnection: close\r\nHost: www.tianqi.com\r\n\r\n"
sock.send(req.encode())
data = b''
while True:
    tmp = sock.recv(1024)
    if tmp:
        data += tmp
    else:
        break

data = data.decode(errors="ignore")
sock.close()
news_title = re.search("汉(.+?)】", data).group(1)
site = re.search("<h2>(.+?)</h2>",data).group(1)  #地点
time = re.search("week\">(.+?)</dd>",data).group(1) #时间
weather = re.findall("<b>(.+?)</b>",data,re.M)[0:5]
r =["地点："+site,"时间："+time,"天气："+weather[0]+"℃  "]
news_content = '\n'.join(r+weather[1:5])
with open(news_title + ".txt", "w") as f:
    for i in news_content:
        f.write(i)

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "taolang25@foxmail.com"  # 用户名
#mail_pass = "wsrgdocjcxsxbiej"  # 口令
mail_pass = "vcnpthnckxosjebf"

sender = 'taolang25@foxmail.com'
receivers = ['459012403@qq.com', 'chenyubing@chenyubing.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText(news_content, 'plain', 'utf-8')
message['From'] = Header("dj", 'utf-8')
message['To'] = Header("张三", 'utf-8')

subject = news_title
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host)  # SMTP over SSL 默认端口号为465
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件", e)