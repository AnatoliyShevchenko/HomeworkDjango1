from django.shortcuts import (render, HttpResponse,)
from django.http.request import HttpRequest
import math

# Create your views here.
base = [{
    'name': 'Brick',
    'last_name' : 'Brickkk',
    'login' : 'Brick92',
    'password': 'qwerty123'
}]

def home_work_reg(request):
    return HttpResponse("""
        <form action="/check-reg/" method="post">
            <input type="text" name="name" id="name" placeholder="Введите ваше имя">
            <input type="text" name="last_name" id="last_name" placeholder="Введите вашу фамилию">
            <input type="text" name="login" id="login" placeholder="Придумайте логин">
            <input type="password" name="password" id="password" placeholder="Придумайте пароль">
            <input type="password" name="ppassword" id="ppassword" placeholder="Подтвердите пароль">
            <input type="submit" value="enter">
        </form>
    """)

def check_reg(request: HttpRequest):
    global base
    name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    login = request.POST.get('login')
    password = request.POST.get('password')
    ppassword = request.POST.get('ppassword')
    go_on = 0 # 0 = логин занят, 1 = пароли не совпадают, 2 = ок
    temp = {}
    keys = ['name', 'last_name', 'login', 'password']
    values = [name, last_name, login, password]
    for i in base:
        if login == i['login']:
            go_on = 0
        elif password != ppassword: 
            go_on = 1
        else:
            go_on = 2
    if go_on == 2:
        temp = dict(zip(keys, values))
        base.append(temp)
        return HttpResponse('<h1>Вы успешно зарегистрировались, перейдите на страницу авторизации</h1>\
            <a href="/home-work-autorization"><button>GO</button></a>')
    elif go_on == 1:
        return HttpResponse('<h1 style="color: red;">Пароли не совпадают</h1>\
            <a href="/home-work-reg"><button>GO BACK</button></a>')
    else:
        return HttpResponse('<h1 style="color: red;">Логин занят</h1>\
            <a href="/home-work-reg"><button>GO BACK</button></a>')

def home_work_autorization(request):
    return HttpResponse("""
        <form action="/check-autorization/" method="post">
            <input type="text" name="login" id="login" placeholder="Введите логин">
            <input type="password" name="password" id="password" placeholder="Введите пароль">
            <input type="submit" value="enter">
        </form>
    """)

def check_autorization(request: HttpRequest):
    global base
    login = request.POST.get('login')
    password = request.POST.get('password')
    go_on = 0 # 0 = логин не зарегистрирован, 1 = неправильный пароль, 2 = ок
    for i in base:
        if login != i['login']:
            go_on = 0
        elif login == i['login'] and password != i['password']:
            go_on = 1
        elif login == i['login'] and password == i['password']:
            go_on = 2
            name = i['name']
            last_name = i['last_name']
    if go_on == 0:
        return HttpResponse('<h1 style="color: red;">Данный логин не зарегистрирован, перейдите на страницу регистрации</h1>\
            <a href="/home-work-reg"><button>GO</button></a>')
    elif go_on == 1:
        return HttpResponse('<h1 style="color: red;">Неправильный пароль</h1>\
            <a href="/home-work-autorization"><button>GO BACK</button></a>')
    else:
        return HttpResponse(f'<h1 style="color: yellowgreen;">{name}</h1>\
            <h1 style="color: blue;">{last_name}</h1>')

def don_t(request):
    global base
    return HttpResponse(base)