from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
import time
import hashlib

def HashCode(s,salt="MyWeb"):
    h = hashlib.sha256()
    s+=salt
    h.update(s.encode())
    return h.hexdigest()

# Create your views here.
def login(request):
    if request.session.get('is_login',None): #若当前账户已经登录
        return redirect('/index/') #则直接跳转至主页
    if request.method=='POST':
        login_form = forms.UsrForm(request.POST)#从Usr表单中获取信息
        #print(username,password)
        message = '请仔细检查您的输入！'
        if login_form.is_valid(): #若login_Form中的数据是有效的
            username = login_form.cleaned_data.get('usrname') #从用户输入中获取账号
            password_new = login_form.cleaned_data.get('password')#从用户输入中获取密码
        #if username.strip() and password: #通过strip函数去除掉账号和密码中的空白
            try:
                user= models.User.objects.get(name=username) #验证模板中的已存在用户与当前登录的用户是否一样
            except:
                message='您的账号不存在!'
                return render(request,'login/login.html',locals()) #若为不同，则继续在此页面进行登录

            if user.password==HashCode(password_new):#若密码也正确的话，就跳转至主页
                request.session['is_login'] = True #将当前登录状态写入session字典
                request.session['user_id'] = user.id #将当前登录数据写入session字典
                request.session['user_name'] = user.name #将当前登录数据写入session字典
                return redirect('/index/')
            else:
                message = '您的密码输入有误!'
                return render(request, 'login/login.html',locals())
    login_form = forms.UsrForm()
    return render(request,'login/login.html',locals())

def index(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    return render(request,'login/index.html',locals())

def register(request):
     if request.session.get('is_login',None): #若当前已经登录
         return redirect('/index/') #则直接跳转至登录页面
     if request.method=='POST': #若请求的方法为post
         register_form = forms.RegisterForm(request.POST) #把注册表单的数据引过来
         message = "请仔细检查填写内容"
         if register_form.is_valid(): #若注册表单的数据是有效的
             usrname = register_form.cleaned_data.get('usrname')
             password = register_form.cleaned_data.get('password')
             password1 = register_form.cleaned_data.get('password1')
             email = register_form.cleaned_data.get('email')
             sex = register_form.cleaned_data.get('sex')

             if password != password1:
                 message = '您两次密码输入不同'
                 return render(request,'login/register.html',locals())
             else:
                 same_user = models.User.objects.filter(name=usrname)
                 if same_user:
                     message = '您填写的账号已被注册'
                 same_emai1= models.User.objects.filter(email=email)
                 if same_emai1:
                   message = '您填写的邮箱已注册'
                   return render(request, 'login/register.html', locals())
             new_user = models.User()
             new_user.name = usrname
             new_user.password=HashCode(password)
             new_user.email = email
             new_user.sex = sex
             new_user.save()

             message = '成功注册'
             time.sleep(3)

             return redirect('/login/')
         else:
             return render(request, 'login/register.html', locals())
     register_form=forms.RegisterForm()
     return render(request,'login/register.html',locals())

def logout(request):
    if not request.session.get('is_login',None): #若当前没有登录则直接退出至login
        return redirect('/login/')
    request.session.flush() #否则就退出，同时清除session数据
    return redirect('/login/')