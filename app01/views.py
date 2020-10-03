"""
请求/响应处理逻辑
"""

from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse, render,redirect
from Helper import Tools
from app01.models import Publisher
from DAO import MysqlHelper


def index(request):
    players = MysqlHelper.get_players()
    # orient参数，设置为records时，就是转换为字典的列表
    # print(players.to_dict(orient='records'))
    return render(request, "index.html", {"players": players.to_dict(orient='records')})


def manage(request):
    return render(request, "manage.html")


def login(request):
    # print("-" * 20)
    # print(request, type(request))
    # print(request.method, type(request.method))
    # print("-" * 20)
    if request.method == "POST":
        # print(request.POST["user"])
        # print(request.POST["pwd"])
        user = request.POST["user"]
        pwd = request.POST["pwd"]
        if login_check(user, pwd):
        # if user == "Admin" and pwd == "123456":
        #     return HttpResponse("登录成功")
            return redirect("/index/")
    return render(request, "login.html")


def player_info(request):
    players = MysqlHelper.get_players()
    # orient参数，设置为records时，就是转换为字典的列表
    # print(players.to_dict(orient='records'))
    return render(request, "index.html", {"players": players.to_dict(orient='records')})



def login_check(username, pwd):
    user_info = Tools.get_user_info(username, pwd)
    # print(user_info, username, pwd)
    if user_info is None:
        return False
    if len(user_info) > 0:
        # print(user_info[0][1] , str(pwd))
        if user_info[0][0] == username:
            return True
    return False


def del_player(request):
    p_id = request.GET.get("id")
    MysqlHelper.do_execute("DELETE FROM b_player_basicinfo WHERE id = {};".format(p_id))
    return redirect("/index")


def add_player(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        number = request.POST.get("number")
        nationality = request.POST.get("nationality")
        position = request.POST.get("position")
        Tools.insert_into_b_player_info(name, age, number, position, weight, height, nationality)
        return redirect("/index")
    return render(request, "add_player.html")


def modify_player(request):
    p_id = request.GET.get("id")
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        number = request.POST.get("number")
        nationality = request.POST.get("nationality")
        position = request.POST.get("position")
        Tools.modify_b_player_info(p_id, name, age, number, position, weight, height, nationality)
        return redirect("/index")
    return render(request, "modify_player.html")


def words(request):
    return HttpResponse("字符串")



def second(request):
    return render(request, "second.html")


def do_register(request):
    if request.method == "POST":
        # print(request.POST["user"])
        # print(request.POST["pwd"])
        username = request.POST["user"]
        pwd = request.POST["pwd"]
        if login_check(username, pwd):
            return render(request, "login.html")
        else:
            res = Tools.create_user_info(username, pwd)
            if res == Tools.success:
                return redirect("/second/")
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        # print(request.POST["user"])
        # print(request.POST["pwd"])
        username = request.POST["user"]
        pwd = request.POST["pwd"]
        if login_check(username, pwd):
            return render(request, "register.html")
        else:
            res = Tools.create_user_info(username, pwd)
            if res == Tools.success:
                return redirect("/login/")
    return render(request, "register.html")


def publisher(request):
    publisher_list = Publisher.objects.all()
    print(publisher_list)
    return render(request, "publisher.html", {"publisher": publisher_list})


def add(request):
    # print(request.POST)
    if request.method == "GET":
        return render(request, "add.html")
    a = request.POST["a"]
    b = request.POST["b"]
    if a.isdigit() and b.isdigit():
        a, b = int(a), int(b)
        return HttpResponse(a + b)
    return render(request, "add.html")


def show_one_img(request):
    with open("static/imgs/Starry.jpg", "rb") as f:
        img = f.read()
        return HttpResponse(img, content_type="image/jpg")


def page1(request):
    return render(request, "page1.html")


def team_list(request):
    return render(request, "team_list.html")


def team_info(request):
    name = request.GET.get("name")
    print(request.GET.get("name"))
    return HttpResponse(name)
    # return render(request, "team_info.html")


def get_area(request):
    return HttpResponse("地区")