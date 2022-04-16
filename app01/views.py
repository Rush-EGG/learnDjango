from django.shortcuts import render, HttpResponse, redirect
import requests


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
    else:
        # 是POST请求
        # print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")

        if username == 'root' and password == '123':
            # return HttpResponse("登录成功")
            return redirect("https://www.baidu.com")
        else:
            # return HttpResponse("登录失败")
            return render(request, 'login.html', {"error_msg": "用户名或密码错误"})