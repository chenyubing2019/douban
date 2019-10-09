from django.shortcuts import render
from django.http import HttpResponse
# from .models import PositionTable, PersonInfor    # 从models中导入用户表
# from .models import EnterRec    # 导入招聘表
from . import models
import json

# 获取数据库数据
def HQ(total,list):
    technology = []  # 技术列表
    a = 0
    for x in list:
        b = "j%d" % a
        b = models.PositionTable.objects.filter(total=total, next=x)
        b.names = x
        technology.append(b)
        a += 1
    return technology   # 返回对象列表

# 添加
def add():
    models.PositionTable.objects.all().delete()  # 删除所有数据
    # 技术
    s = ["JAVA", "C++", "PHP", "数据挖掘", "搜索算法", "精准推荐", "C", "C#", "全栈工程师", ".NET", "Hadoop", "Python", "Delphi", "VB",
         "Rudy", "Node.js", "Go", "ASP", "Shell", "区块链", "后端开发其他"]
    s1 = ["HTML5", "Android", "iOS", "WP", "移动开发其他"]
    s2 = ["web前端", "Flash", "html5", "JavaScript", "U3D", "COCOS2D-X", "前端开发其他"]
    s3 = ["深度学习", "机器学习", "图像处理", "图像识别", "语言识别", "机器视觉", "算法工程师", "自然语言处理"]
    s4 = ["测试工程师", "自动化测试", "功能测试", "性能测试", "测试开发", "游戏测试", "白盒测试", "灰盒测试", "黑盒测试", "手机测试", "硬件测试", "测试经理", "测试经理", "测试其他"]
    s5 = ["运维工程师", "运维开发工程师", "网络工程师", "系统工程师", "IT支持", "IDC", "CDN", "F5系统管理员", "病毒分析", "WEB安全", "网络安全", "系统安全", "运维经理",
          "运维其它"]
    s6 = ["MySQL", "SQLServer", "Oracle", "DB2", "MongoDB", "ETL", "Hive", "数据仓库", "DBA其他"]
    s7 = ["技术经理", "技术总监", "架构师", "CTO", "运维总监", "技术合伙人", "项目总监", "测试总监", "安全专家", "高端技术职位其他"]
    s8 = ["项目经理", "项目经理"]
    s9 = ["硬件", "嵌入式", "自动化", "单片机", "电路设计", "驱动开发", "系统集成", "FPGA开发", "DSP开发", "ARM开发", "PCB工艺", "模具设计", "热传导", "材料工程师",
          "精益工程师", "射频工程师", "硬件开发其他"]
    s10 = ["实施工程师", "售前工程师", "售后工程师", "BI工程师", "企业软件其他"]
    # 产品
    s11 = ["产品经理", "网页产品经理", "移动产品经理", "产品助理", "数据产品经理", "电商产品经理", "游戏策划", "产品实习生"]
    s12 = ["网页产品设计师", "无线产品设计师"]
    s13 = ["产品部经理", "产品总监", "游戏制作"]
    # 设计
    s14 = ["视觉设计师", "网页设计师", "Flash设计师", "APP设计师", "UI设计师", "平面设计师", "美术设计师(2D/3D)", "广告设计师", "多媒体设计师", "原画师", "游戏特效",
           "游戏界面设计师", "游戏场景", "游戏角色", "游戏动作"]
    s15 = ["交互设计师", "无线交互设计师", "网页交互设计师", "硬件交互设计师"]
    s16 = ["数据分析师", "用户研究员", "游戏数值策划"]
    s17 = ["设计经理/主管", "设计总监", "视觉设计经理/主管", "视觉设计总监", "交互设计经理/主管", "交互设计总监", "用户研究经理/主管", "用户研究总监"]
    # 运营
    s18 = ["用户运营", "产品运营", "数据运营", "内容运营", "活动运营", "商家运营", "品类运营", "游戏运营", "网络推广", "运营专员", "网店运营", "新媒体运营", "海外运营",
           "运营经理"]
    s19 = ["副主编", "内容编辑", "文案策划", "记者"]
    s20 = ["售前咨询", "售后客服", "淘宝客服", "客服经理"]
    s21 = ["主编", "运营总监", "COO", "客服总监"]
    # 市场
    s22 = ["市场营销", "市场策划", "市场顾问", "商务渠道", "商业数据分析", "活动策划", "网络营销", "海外市场", "商务专员"]
    s23 = ["政府关系", "品牌公关", "广告协调", "媒介投放", "媒介合作", "媒介顾问"]
    s24 = ["广告创意", "广告制作", "广告文案", "广告投放", "广告定价", "广告专员", "品牌合作", "品牌策划", "品牌专员", "美术指导"]
    s25 = ["市场推广", "渠道推广", "SEO", "SEM"]
    s26 = ["策划经理", "媒介经理", "市场总监", "公关总监", "媒介总监", "创意总监"]
    # 销售
    s27 = ["销售专员", "销售顾问", "销售经理", "客户代表", "客户经理", "商务拓展", "渠道销售", "代理商销售", "电话销售", "广告销售", "信用卡销售", "保险销售", "销售工程师",
           "商务渠道", "其他销售"]
    s28 = ["销售总监", "商务总监", "区域总监", "城市经理", "团队经理", "销售VP", "商务主管", "其他销售管理职位"]
    # 职能
    s29 = ["人力资源", "招聘", "HRBP", "人事/HR", "培训经理", "薪资福利经理", "绩效考核经理", "员工关系"]
    s30 = ["助理", "前台", "行政", "总助", "文秘"]
    s31 = ["会计", "出纳", "财务", "结算", "税务", "审计", "风控"]
    s32 = ["法务", "律师", "专利"]
    s33 = ["行政总监/经理", "财务总监/经理", "HRD/HRM", "CFO", "CEO"]
    # 游戏
    s34 = ["H5游戏开发", "小游戏开发", "游戏后端开发", "C++游戏开发", "FLASH", "COCOS2D-X", "U3D", "游戏测试"]
    s35 = ["游戏制作人", "游戏产品经理", "游戏项目经理", "游戏策划", "剧情设计", "游戏文案"]
    s36 = ["游戏动画", "游戏原画", "游戏界面", "游戏场景", "游戏角色", "游戏动作", "游戏动效", "游戏美工"]
    s37 = ["游戏运营", "游戏编辑", "游戏推广", "手游推广", "页游推广"]
    s38 = ["游戏主播", "游戏陪练", "游戏体验", "电竞主持", "电竞讲师"]
    a = ["后端开发", "移动开发", "前端开发", "人工智能", "测试", "运维", "DBA", "高端职位", "项目管理", "硬件开发", "企业软件", "产品经理", "产品设计师", "高端职位",
         "视觉设计", "交互设计", "用户研究", "高端职位", "运营", "编辑", "客服", "高端职位", "市场/营销", "媒介/公关", "品牌/广告", "渠道/推广", "高端职位", "销售",
         "销售管理", "人力资源", "行政", "财务", "法务", "高端职位", "技术开发", "产品策划", "设计", "运营/推广", "其他"]
    b = ["技术", "产品", "设计", "运营", "市场", "销售", "职能", "游戏"]
    p = 0
    k = [s, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24,
         s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38]

    for l in k:
        for i in l:
            if p <= 10:
                stu1 = models.PositionTable(name=i, total=b[0], next=a[p])
                stu1.save()
            elif 10 < p <= 13:
                stu1 = models.PositionTable(name=i, total=b[1], next=a[p])
                stu1.save()
            elif 13 < p <= 17:
                stu1 = models.PositionTable(name=i, total=b[2], next=a[p])
                stu1.save()
            elif 17 < p <= 21:
                stu1 = models.PositionTable(name=i, total=b[3], next=a[p])
                stu1.save()
            elif 21 < p <= 26:
                stu1 = models.PositionTable(name=i, total=b[4], next=a[p])
                stu1.save()
            elif 26 < p <= 28:
                stu1 = models.PositionTable(name=i, total=b[5], next=a[p])
                stu1.save()
            elif 28 < p <= 33:
                stu1 = models.PositionTable(name=i, total=b[6], next=a[p])
                stu1.save()
            elif 33 < p <= 38:
                stu1 = models.PositionTable(name=i, total=b[7], next=a[p])
                stu1.save()
        p += 1
        pass

# 获取职位数据
def index(request):
    # 技术
    # add()
    total = "技术"
    next = ["后端开发", "移动开发", "前端开发", "人工智能", "测试", "运维", "DBA", "项目管理", "硬件开发", "企业软件"]
    technology = HQ(total, next) 
    # 产品
    product_total = "产品"
    product_list = ["产品经理", "产品设计师", "高端职位"]
    product = HQ(product_total, product_list)
    # 设计
    design_total = "设计"
    design_list = ["视觉设计", "交互设计", "用户研究", "高端职位"]
    design = HQ(design_total, design_list)
    # 运营
    operating_total = "运营"
    operating_list = ["运营", "编辑", "客服", "高端职位"]
    operating = HQ(operating_total, operating_list)
    # 市场
    market_total = "市场"
    market_list = ["市场/营销", "媒介/公关", "品牌/广告", "渠道/推广", "高端职位"]
    market = HQ(market_total, market_list)
    # 销售
    sales_total = "销售"
    sales_list = ["销售", "销售管理"]
    sales = HQ(sales_total, sales_list)
    # 职能
    function_total = "职能"
    function_list = ["人力资源", "行政", "财务", "法务", "高端职位"]
    function = HQ(function_total, function_list)
    # 游戏
    game_total = "游戏"
    game_list = ["技术开发", "产品策划", "设计", "运营/推广", "运营/推广"]
    game = HQ(game_total, game_list)

    # 招聘信息
    recruitment = models.EnterRec.objects.all()[:10]


    dict = {"technology": technology, "product": product, "design": design, "operating": operating, "market": market, "sales": sales, "function": function, "game": game, "recruitment":recruitment}
    return render(request, "main/index.html", dict)

# 个人资料添加
def  Person_Infor(request):
    if request.method == "GET":
        return render(request, "main/resume.html")
    elif request.method == "POST":
        phone = request.POST.get("phone")    # 手机号
        name = request.POST.get("name")      # 姓名
        sex = request.POST.get("sex")
        birthday = request.POST.get("birthday")      # 生日
        area = request.POST.get("area")              # 所在地区
        email = request.POST.get("email")            # 邮箱
        student = request.POST.get("student")        # 是否为学生
        worktime = request.POST.get("worktime")      # 参加工作时间
        school = request.POST.get("school")          # 学校
        admdate = request.POST.get("admdate")        # 入学时间
        gradtime = request.POST.get("gradtime")      # 毕业时间
        prof = request.POST.get("prof")              # 专业
        education = request.POST.get("education")    # 学历
        selfdes = request.POST.get("selfdes")                 # 自我描述(selfdes): 150
        shejiao = request.POST.get("shejiao")                 # 社交主页(shejiao): 如GitHub的url
        type_work = request.POST.get("type_work")             # 工作类型(type_work): python / java
        nature_work = request.POST.get("nature_work")         # 工作性质(nature_work)：实习/全职
        expecte_salary = request.POST.get("expecte_salary")   # 期望薪资(expecte_salary)
        low_salary = request.POST.get("low_salary")           # 最低薪资(low_salary)
        work_city = request.POST.get("work_city")             # 期望工作城市(work_city)
        state = request.POST.get("state")                     # 当前状态(state)
        available_time = request.POST.get("available_time")   # 可工作时间(available_time)
        print(phone,type(phone))
        info = [name, sex, worktime, phone, birthday, area, email, student, school, admdate, gradtime, prof, education, selfdes, shejiao, type_work, nature_work, expecte_salary, low_salary, work_city, state, available_time]
        for x in info:
            print(x)
            if x == "":
                return HttpResponse("数据不能有空值，请填写数据")
        p = models.PersonInfor(name=name, phone=phone, worktime=worktime, sex=sex, birthday=birthday, area=area, email=email, student=student, school=school, admdate=admdate, gradtime=gradtime, prof=prof, education=education, selfdes=selfdes, shejiao=shejiao, type_work=type_work, nature_work=nature_work, expecte_salary=expecte_salary, low_salary=low_salary, work_city=work_city, state=state, available_time=available_time)
        p.save()
        return HttpResponse("录入成功")













