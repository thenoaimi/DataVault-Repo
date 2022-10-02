from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    return render(request, 'login/index.html')

def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        message = 'Examine the content！'
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(name=username)
        except :
            message = 'User does not exist'
            return render(request, 'login/login.html', locals())
        if user.password == password:
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('/index/')
        else:
            message = 'wrong password！'
            return render(request, 'login/login.html', locals())
    else:
        return render(request, 'login/login.html', locals())

    return render(request, 'login/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")