create table employee(      #员工
		eid  INT UNSIGNED AUTO_INCREMENT,
		ename  VARCHAR(255) not null,
		sex 	char(4)  not null,
		birthday DATE  not null,  #出生日期
		duty VARCHAR(20) not null, #职务
		phone CHAR(11) not null,  #手机号
		PRIMARY key(eid)
);
insert into employee VALUES (1001, '张三', '男', '1996-3-20',' 收银员', '18971515416');
insert into employee VALUES (1002, '李四', '女', '1997-5-11', '组长', '18971515635');
insert into employee VALUES (1003, '王五', '男', '1989-6-20', '经理', '18971515534');


create table userinfo(      #用户
		uid  INT UNSIGNED AUTO_INCREMENT,
		uname  VARCHAR(255) not null,
		sex 	char(4)  not null,
		Tdata DATE  not null,     #注册日期
		balance int	not null, #余额
		PRIMARY key(uid)
);
insert into userinfo VALUES (1001, '赵6', '女', '2015-6-20', 300);
insert into userinfo VALUES (1002, '小明', '男', '2016-1-10', 100);
insert into userinfo VALUES (1003, '小强', '男', '2016-9-15', 1000);

  
create table supplier(    #供应商
		sid  INT UNSIGNED AUTO_INCREMENT,
		sname  VARCHAR(255) not null,
		sex 	char(4)  not null,
		phone CHAR(11) not null,
		site  VARCHAR(255) not null,    #地点
		cname VARCHAR(255) not null, #商品名
		PRIMARY key(sid)
);
insert into supplier VALUES (1001, '小红', '女', '18971515511', '湖北','方便面');
insert into supplier VALUES (1002, '王明', '男', '18971515615', '深圳','1L矿泉水');
insert into supplier VALUES (1003, '张强', '男', '18971515599', '上海','牛肉干');


create table commodity(    #商品
		cid  INT UNSIGNED AUTO_INCREMENT,
		cname  VARCHAR(255) not null,
		price  int not null,  #价格
		amount int  not null,       #数量
		unit   VARCHAR(4) not null,  #计量单位
		dom  DATE   not null,   #生产日期
		sname  VARCHAR(255) not null,   #供应商
		PRIMARY key(cid)
);
insert into commodity VALUES (1001, '方便面', 1, 50, '袋','2019-6-3','小红');
insert into commodity VALUES (1002,'1L矿泉水', 6, 30, '瓶','2019-9-1','王明');
insert into commodity VALUES (1003, '牛肉干',10, 60, '袋','2019-7-20','张强');