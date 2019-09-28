from flask import Flask,request,render_template,redirect,Response
app= Flask(__name__)

@app.route("/")
def home():
    is_login= request.cookies.get("is_login")
    return render_template("home.html",is_login=is_login)

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        is_login = request.cookies.get("is_login")
        if is_login:
            rsp = redirect("/")
            return rsp
        return render_template("login.html")
    elif request.method == "POST":
        user_name = request.form.get("user_name")
        user_pwd = request.form.get("user_pwd")
        if user_name == "cyb" and user_pwd == "123456":
            rsp=redirect("/") #登录成跳转到首页
            rsp.set_cookie("is_login","1")
            return rsp
        else:
            return render_template("login_fail.html")

@app.route("/photos")
def photos():
    is_login = request.cookies.get("is_login")
    if is_login:
        return render_template("photos.html")
    else:
        return redirect("/login")


@app.route("/logout")
def logout():
    is_login = request.cookies.get("is_login")
    if is_login:
        rsp = redirect("/")
        rsp.delete_cookie("is_login")
        return rsp
    else:
        return redirect("/login")

@app.route("/login_fail")
def login_fail():
        return  redirect("/login")

if __name__=="__main__":
    app.run(port=80,debug=True)
    # app.run(host="0.0.0.0", port=80, debug=True)