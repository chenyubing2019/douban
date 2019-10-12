$(function(){
    // 定义一个全局变量can_submit 初始值为false，表不能提交
    var can_submit = false;

    // 提交事件，只有当can_submit返回true才能成功提交
    $("form").submit(function(){
        return can_submit;
    });
    // blur()方法的作用：添加函数到blur事件，当<input>字段失去焦点时发生blur事件
    $('input[name="form-phone"]').blur(function(){
        // 获取user_name的值
        var form_phone = $("#form-phone").val();
        // 去除用户名的空格
        form_phone = form_phone.replace(/^\s+|\s+$/gm, '');
        // 如果用户名为空
        if(form_phone === ''){
            $("#form-phone").css("border", "2px solid red");
            // 并且将can_submit设置为false
            can_submit = false;
            return;
        }
        if (! /1\d{10}/.test(form_phone)) {
            $("#form-phone").css("border", "2px solid red");
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
                    $("#form-phone").css("border", "2px solid green");

                    $("#btn").click(function(){
                        console.log("开始发送验证码");
                        // 通过Ajax将手机号发送给服务器后端程序
                        $.ajax({
                            url: "/user_center/send_yzm",
                            data: {"phone": form_phone},
                            success: function(data){
                                if (data["err"] === 0) {
                                    console.log("成功接收");
                                    // 成功
                                    var s = 60;
                                    $("#btn").prop("disabled", true);
                                    $("#btn").html(s + "S");
                                    var timer = window.setInterval(function() {
                                        --s;
                                        if (s === 0) {
                                            window.clearInterval(timer);
                                            $("#btn").html("重新获取");
                                            $("#btn").prop("disabled", false);
                                            return;
                                        }
                                        $("#btn").html(s + "S");
                                    }, 1000);
                                } else {
                                    // 失败
                                    alert("发送短信验证码失败，" + data["desc"]);
                                }
                            },
                            error: function(){
                                alert("发送请求失败，请检查网络连接！");
                            }
                        });
                    });
                }
                else {
                    // 手机号已注册，则显示红色
                    $("#form-phone").css("border", "2px solid red");
                    alert("手机号已注册")
                    can_submit = false;
                    return;
                }
            },
            error: function () {console.log("返回出错");}
        });
    });

    // 校验验证码
    $('input[name="form-verify_code"]').blur(function(){
        var verify_code = $(this).val();
        console.log("开始校验验证码",verify_code);
        if (! /\d{6}/.test(verify_code)){
            $("#form-verify_code").css("border", "2px solid red");
            alert("验证码格式错误")
            can_submit = false;
            return;
        }else {
            $("#form-verify_code").css("border", "2px solid green");
            can_submit = true;
        }
    });
});