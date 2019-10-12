$(function(){
    // 定义一个全局变量can_submit 初始值为false，表不能提交
    var can_submit = false;

    // 提交事件，只有当can_submit返回true才能成功提交
    $("form").submit(function(){
        return can_submit;
    });

    $('input[name="form-password1"]').blur(function(){
        var upass = $(this).val();
        upass = upass.replace(/^\s+|\s+$/gm, '');
        if(upass === ''){
            $("#form-password1").css("border","2px solid red");
            // alert("密码不能为空")
            can_submit = false;
            return;
        }
        if(upass.length < 6 || upass.length > 15){
            $("#form-password1").css("border","2px solid red");
            alert("密码格式错误")
            can_submit = false;
            return;
        }
        else{
            $("#form-password1").css("border","2px solid green");
        }
    });

    $('input[name="form-password2"]').blur(function(){
        var upass2 = $(this).val();
        upass2 = upass2.replace(/^\s+|\s+$/gm, '');

        if(upass2 === ''){
            $("#form-password2").css("border","2px solid red");
            alert("密码不能为空")
            can_submit = false;
            return;
        }

        if(upass2.length < 6 || upass2.length > 15){
            $("#form-password2").css("border","2px solid red");
            alert("密码格式错误")
            can_submit = false;
            return;
        }

        var user_p = $("#form-password1").val()
        if (upass2 != user_p){
            console.log(upass2);
            console.log(user_p);
            $("#form-password2").css("border","2px solid red");
            alert('两次密码不相同')
            can_submit = false;
            return;
        }
        else{
            $("#form-password2").css("border","2px solid green");
            can_submit = true;
        }
    });
});