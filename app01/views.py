from django.shortcuts import render, HttpResponse, redirect
import requests
from app01.models import Department, UserInfo


# Create your views here.

# 视图函数，写函数


def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    # 在render的内部，会找到user_list.html这个文件
    # 优先会去项目的根目录，也就是manage.py所在目录的templates文件夹下找
    # 如果找不到，那么会根据app的注册顺序，逐一在每个app下的templates文件夹中找
    # 并将这个页面返回给用户
    return render(request, "user_list.html")


def user_add(request):
    return render(request, 'user_add.html')


def tpl(request):
    name = "喷喷"
    roles = ["管理员", "CEO", "保安"]
    user_info = {"name": "卢小喷", "salary": "100包狗粮", "role": "CTO"}
    data_list = [
        {"name": "郑筝", "salary": "100w", "role": "CEO"},
        {"name": "马麻", "salary": "1000", "role": "保安"},
        {"name": "王魍", "salary": "1", "role": "临时工"}
    ]

    return render(request,
                  'tpl.html',
                  {"n1": name,
                   "n2": roles,
                   "n3": user_info,
                   "n4": data_list})


def news(req):
    # 用爬虫去获取联通的新闻
    # 向地址http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/04/news发请求

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/04/news", headers=headers)
    data_list = res.json()
    # print(data_list)

    return render(req, 'news.html', {"news_list": data_list})


def reANDres(request):
    # request是一个对象，封装了用户发送的所有的数据

    # 获取请求的方式 GET/POST
    print(request.method)

    # request.GET能得到用户在url上面传送一些值
    # /?n1=123&n2=456
    # GET请求是放在明面上的
    print(request.GET)

    # 用户在在请求体中提交的数据通过.POST来得到
    # POST请求是偷偷传过来的，表面看不到
    print(request.POST)

    # 【响应】HttpResponse("返回内容")能将该函数内部的字符串返回给请求者
    # return HttpResponse("返回内容")

    # 【响应】通过读取HTML的内容，再加上渲染，并将一些占位符等替换为字符串，返还给请求者
    # return render(request, 'reandres.html', {"title": "来啦"})

    # 【响应】让浏览器重定向到其他的页面
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    # 是POST请求
    # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")

    if username == 'root' and password == '123':
        # return HttpResponse("登录成功")
        return redirect("https://www.baidu.com")

    # return HttpResponse("登录失败")
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})


def orm(request):
    # 测试orm添加数据
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="运营部")

    # UserInfo.objects.create(name="tt", password="123", age=23, size=5)

    # 测试orm删除数据
    # UserInfo.objects.filter(id=2).delete()
    # UserInfo.objects.filter(id=3).delete()
    # Department.objects.all().delete()

    # 测试orm获取数据
    # 筛选得到的数据是一个列表，列表里面是一行行的数据->[行， 行]
    # 是QuerySet类型
    # 而每一行都是一个对象，里面封装了所有列和对应的字段
    data_list = UserInfo.objects.all()
    # print(data_list)
    for obj in data_list:
        print(obj.id, obj.name, obj.password, obj.age)

    # 如果知道拿到的只有一行数据，或者只要第一行数据
    # 可以使用.first()方法
    row_obj = UserInfo.objects.filter(id=1).first()
    print(row_obj.name)

    # 更新数据
    # UserInfo.objects.all().update(password=999)

    return HttpResponse("成功")


def info_list(request):
    # 获取数据库中所有的用户信息
    data_list = UserInfo.objects.all()
    # print(data_list)

    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")

    # 获取用户提交的post请求
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    size = request.POST.get("size")

    # 添加到数据库
    UserInfo.objects.create(name=user, password=pwd, age=age, size=size)

    return redirect("/info/list/")


def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")
