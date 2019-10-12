$(function(){
    // 定义一个全局变量can_submit 初始值为false，表不能提交
    var can_submit = false;
    var a = 0;
    var b = 0
    // 提交事件，只有当can_submit返回true才能成功提交
    $("form").submit(function(){
        return can_submit;
    });
    // blur()方法的作用：添加函数到blur事件，当<input>字段失去焦点时发生blur事件
    $('input[name="form-username"]').blur(function(){
        // 获取user_name的值
        var form_phone = $("#form-username").val();
        // 去除用户名的空格
        form_phone = form_phone.replace(/^\s+|\s+$/gm, '');
        // 如果用户名为空
        if(form_phone === ''){
            $("#form-username").css("border", "2px solid red");
            // 并且将can_submit设置为false
            can_submit = false;
            return;
        }
        if (! /1\d{10}/.test(form_phone)) {
            $("#form-username").css("border", "2px solid red");
            can_submit = false;
            return;
        }
        // 通过AJAX发送请求给服务器以校验用户名是否已经存在
        $.ajax({
            type: "GET",
            contentType: "application/json; charset=UTF-8",
            dataType: "json",
            url: "/user_center/check_phone",
            data: "phone=" + form_phone,
            timeout: 1000,
            success: function(data){
                console.log(data);
                // 如果不存在该手机号则返回{"err": 0}
                if (data["err"] === 0) {
                    $("#form-username").css("border", "2px solid red");
                    alert("该用户未注册");
                    return;
                }
                if (data["err"] === 1)   {
                    // 手机号已注册，则显示绿色
                    $("#form-username").css("border", "2px solid green");
                    a = 1;

                }
            },
            error: function () {console.log("返回出错");}
        });
    });

    $('input[name="form-password"]').blur(function(){
        var upass = $(this).val();
        upass = upass.replace(/^\s+|\s+$/gm, '');
        if(upass === ''){
            $("#form-password").css("border","2px solid red");
            can_submit = false;
            return;
        }
        if(upass.length < 6 || upass.length > 15){
            $("#form-password").css("border","2px solid red");
            alert("密码格式错误")
            can_submit = false;
            return;
        }
        else{
            $("#form-password").css("border","2px solid green");
            b = 1
        }
        if (a == 1 && b ==1){can_submit = true;}
    });
});