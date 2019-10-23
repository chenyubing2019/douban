from flask import Flask,request,render_template
from lxml import etree
import  requests , re
app = Flask(__name__)

@app.route("/",methods=["GET"])
def app2():
    if request.method == "GET":
        c = a()
        html = etree.HTML(c.text)
        #新片榜
        name1 = html.xpath('//div[@class=""]//a/@title')  # 中文名
        name2 = html.xpath('//div[@class=""]//a/span/text()')  # 翻译名
        synopsis = html.xpath('//div[@class=""]//p/text()')  # 简介
        picture = html.xpath('//div[@class=""]//a/img/@src')  # 图片网络地址
        connect = html.xpath('//div[@class=""]//a[@class="nbg"]/@href')  # 电影链接
        grade = html.xpath('//div[@class="star clearfix"]//span[@class="rating_nums"]/text()')  # 评分
        grade_amount = html.xpath('//div[@class="star clearfix"]//span[@class="pl"]/text()')  # 评分人数
        #一周口碑榜
        c1 = re.findall("                    (.+?)\n                </a>",c.text)[0:10]  #电影名字
        c2 = html.xpath('//div[@class="name"]//a/@href')  # 电影连接
        c3 = html.xpath('//span[@class="box_chart_num color-gray"]/text()')[0]  # 更新时间
        c4 = html.xpath('//div[@class="no"]/text()')[0:9]  # 序号
        nuw = list(zip(name1,name2,synopsis,picture,connect,grade,grade_amount))
        nuw2 =list(zip(c1,c2,c4))
        return render_template("douban.html",nuw=nuw,nuw2=nuw2,c3=c3)

def a():
    c = requests.get("https://movie.douban.com/chart")
    c.raise_for_status()  # 如果状态不是200，则引发异常
    c.encoding = c.apparent_encoding
    return c

if __name__ == "__main__":
    app.run(port=8000 ,debug=True)