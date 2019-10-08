from flask import Flask, request, render_template,flash
from crud import inquire,delete,revise,add
app = Flask(__name__)
app.secret_key = 'cyb'

@app.route("/")
def home_pape():
    return render_template("home_pape.html")

@app.route("/user" ,methods=["GET"])
def user():
    table = request.args.get("table")
    users = inquire(table)
    return render_template("user.html",users=users,table=table)

@app.route("/del")
def user_del():
    id = request.args.get("id")
    table = request.args.get("table")
    delete(table, id)
    users = inquire(table)
    flash(u"删除成功")
    return render_template("user.html", users=users, table=table)


@app.route("/upd" ,methods=["GET", "POST"] )
def upd():
    if request.method == "GET":
        id = request.args.get("id")
        table = request.args.get("table")
        return render_template("amend.html", id=id,table=table)
    elif request.method == "POST":
        table = request.form.get("table")
        print(table)
        id = request.form.get("id")
        print(id)
        s = request.form.get("s")
        print(s)
        n = request.form.get("n")
        print(n)
        if s != "balance":
            n = "\""+n+"\""
        revise(table,s,n,id)
        users = inquire(table)
        flash(u"修改成功")
        return render_template("user.html",users=users,table=table)


@app.route("/add2",methods=["GET","POST"])
def add2():
    if request.method == "GET":
        table = request.args.get("table")
        return render_template("add2.html",table=table)
    elif request.method == "POST":
        table = request.form.get("table")
        id = request.form.get("id")
        name = request.form.get("name")
        sex = request.form.get("sex")
        tdata = request.form.get("tdata")  #注册日期
        balance = request.form.get("balance")  #余额
        phone = request.form.get("phone") #手机号
        site = request.form.get("site") #地点
        cname = request.form.get("cname") #商品名
        if table == "userinfo":
            j = (int(id),name,sex,tdata,int(balance))
            add(table, j)
        if table == "supplier":
            j = (int(id), name, sex, phone, site, cname)
            add(table, j)
        users = inquire(table)
        flash(u"添加成功")
        return render_template("user.html", users=users, table=table)


if __name__ == "__main__":
    app.run(port=80,debug=True)