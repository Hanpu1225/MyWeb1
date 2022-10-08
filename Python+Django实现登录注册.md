# 注册与登录界面

## 一、基本配置

### 1、常规配置

1、打开pycharm界面。选择“Create New Project”：

![image-20220929112103545](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929112103545.png)

![image-20220929112422105](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929112422105.png)

2、点击“Create后”进入项目后，界面如下：

![image-20220929112520448](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929112520448.png)

其目录结构为：

![image-20220929152413462](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929152413462.png)

进入setting.py:

①：引入import os

![image-20220929133842141](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929133842141.png)

②：变更当前语言为中文，时区为上海时间![image-20220929134608940](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929134608940.png)

3、编辑Django sever：

①：选择右上角Edit Configureations ：

![image-20220929134932724](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929134932724.png)

②：进入 详情界面，如下：![image-20220929135431921](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929135431921.png)

③：点击运行按钮，

![image-20220929135637362](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929135637362.png)

④：在浏览器输入IP地址与端口号；即可出现：

![image-20220929135812838](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929135812838.png)

### 2、番外篇

**怎么安装Django以及对应版本？**

步骤如下：

①：选择settings：

![image-20220929140646437](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929140646437.png)



②：选择对应香项目的解释器：

![image-20220929140710004](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929140710004.png)

③：点击‘+’：

![image-20220929140931466](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929140931466.png)

④：进入下一级界面：

![image-20220929141204440](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929141204440.png)

## 二、创建及注册APP

### 1、创建APP

在pycharm下方，找到 Terminal按钮，进入终端：

![image-20220929151517664](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929151517664.png)

输入：

```python
python manage.py startapp login
```

界面如下：

![image-20220929151848356](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929151848356.png)

然后按下“enter”按钮，在目录结构中即可出现刚才创建的APP，其名字为login，界面如下：

![image-20220929152321822](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929152321822.png)

### 2、注册APP

在根目录下，找到setting.py。找到INSTALL_APPS,加入’login‘，APP即可注册完成。

![image-20220929152748061](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220929152748061.png)

究其本质来说，所谓的注册APP就是告诉Django我创建了一个APP，名字是login。没有什么多深奥的东西。

## 三、Model数据的设置

### 1、基本操作

model是负责与数据库进行交互的。在前期的话，可能需要去创建模型中的字段，包括字段名、字段类型、字段参数。若复杂一点的话还包括一些关系型的字段，这个其实有点复杂了。

好吧！回到项目中来：

进入‘login/models.py’，我将整个APP应用中的所有模型都存放于此，主要包括姓名、密码、邮箱地址、性别以及创建时间。具体内容如下：

```python
from django.db import models

# Create your models here.
class User(models.Model): #定义”User“类
    gender = (
        ('male',"男"),
        ('female',"女"),
    )

    name = models.CharField(max_length=28,unique=True)
    password = models.CharField(max_length=56)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=28,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  #返回人类友好

    class Meta: #元数据
        ordering = 'c_time'  #按照创建时间排序
        verbose_name = "用户"
        verbose_name_plural ="用户"
```

### 2、数据库后端的设置

因为这个项目中我们直接就用的是sqlite数据库，所以我们不需要去修改settings中关于数据库的配置，其代码如下：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #引擎
        'NAME': BASE_DIR / 'db.sqlite3', #数据库姓名
    }
}

```

### 3、迁移数据

首先打开pythcharm的左下方的Terminal，然后输入python manage.py makemigrations;这之后你得目录机构下回多一个文件，如下图：

![image-20220930093657205](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930093657205.png)

**就其本质而言，其实就是在数据库中创建User模型。**

接着输入python manage.py migrate 进行真正的数据迁移工作，也就是在数据库中创建真实的数据表。

![image-20220930094313112](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930094313112.png)

## 四、启动admin后台

事实上，在实际的开发应用中，admin后台基本不会怎去使用。但是在学习的初级阶段，我还是使用admin进入后台，然后对我的模型数据进行管理。其具体操作如下：

进入‘login/admin.py’：

```python
from django.contrib import admin
from . import models #从当前目录下引入models

admin.site.register(models.User)  #启动admin
# Register your models here.
```

## 五、创建超级管理员

创建超级管理员的目的主要是为了第一次登录系统。其操作较为简单，首先打开pythcharm的左下方的Terminal，然后输入python manage.py createsuperuser，其操作以及结果如下：

![image-20220930094453587](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930094453587.png)

接下来就是要启动我们的服务器进行登录操作，进入admin后台之后，开始新增、删除用户操作。

### 1、启动服务器

在浏览器输入IP地址与端口号，进入我们的登录页面：

![image-20220930095017852](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930095017852.png)

输入我们创建的超级管理员的用户名与密码。接着进入admin后台：

![image-20220930095333957](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930095333957.png)

### 2、增加用户

点击![image-20220930095400898](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930095400898.png)按钮，进入添加用户界面：

![image-20220930095617872](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930095617872.png)

保存成功会天跳转至如下界面：

![image-20220930095742331](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930095742331.png)

### 3、删除用户

![image-20220930100054539](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930100054539.png)

## 六、路由和视图

### 1、配置说明

考虑到项目中要实现的是登录和注册功能，因此我们要创建四个路由，包含四个html文件，他们分别是：

|    url    |     html      |          视图          |
| :-------: | :-----------: | :--------------------: |
|  index/   |  index.html   |  def index(request):   |
|  login/   |  login.html   |  def login(request):   |
| register/ | register.html | def register(request): |
|  logout/  |  logout.html  |  def logout(request):  |

具体的访问策略为：

- 未登录人员，不论是访问index还是login和logout，全部跳转到login界面
- 已登录人员，访问login会自动跳转到index页面
- 已登录人员，不允许直接访问register页面，需先logout
- 登出后，自动跳转到login界面

### 2、创建模板

在login目录下创建文件templates，在此文件下创建login。在login下创建index.html、login.html、register.html、logout.html。分别在其html了中写入对应信息。对应操作界面如下：

![image-20220930102359505](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930102359505.png)

对应的html页面为：以login举例，其他html类似，不再重复：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>
<h1>这仅仅是登录页面而已</h1>
</body>
</html>
```

### 3、创建视图

在login/view.py中定义相应视图。具体的代码如下：

```python
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html',locals())

def login(request):
    pass
    return render(request,'login/login.html',locals())

def register(request):
    pass
    return render(request,'login/register.html',locals())

def logout(request):
    pass
    return redirect('/login/')
```

### 4、配置路由

在根url下进行配置，具体代码为：

![image-20220930103837168](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930103837168.png)

### 5、启动服务器

在浏览器输入[登录](http://127.0.0.1:8000/login/)，进入我们的login页面，即可看到如下界面：

![image-20220930104004575](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20220930104004575.png)

## 七、HTML+CSS+Jquery

截止目前为止，我们已经将基本的界面完成，但是对于实际开发场景来说，这很显然不满足设计开发。那么，接下来我们就要利用html+css+jquery的相关知识进行设计页面。在这之后，我们的前端界面一定会越来越好看。Let‘s go！！！

### 1、HTML

首先，我们改造的是login。进入templates/login/login.html

更新后的代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1,shrink-to-fit=no">
    <title>登录</title>
</head>
<body>
      <div style="margin: 15% 40%;">
          <h1>欢迎登录SDT</h1>
          <form action="/login/" method="post">
              <p>
                  <label for="id_username">用户名:</label>
                  <input type="text" id="id_username" name="username" placeholder="请输入您的用户名" autofocus required/>
              </p>
              <p>
                  <label for="id_possword">密码:</label>
                  <input type="password" id="id_password" name="password" placeholder="请输入您的密码" required/>
              </p>
              <input type="submit" value="登录">
          </form>

      </div>
</body>
</html>
```

在浏览器输入127.0.0.1:8000/login,Django的运行结果为：

![image-20221001102740823](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221001102740823.png)

若只是简单的使用html的话，这个界面依然不是我们理想中的，因为还是比较丑，虽然基本的功能啥的都有了，但是真的很丑。接下来我们就用到了CSS框架中较为知名的Bootstrap 4框架。

### 2、CSS->Bootstrap4

加入Bootstrap4之后我们的界面较之前就会很好看了。代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
    <!--上面这一行必须放在最前面-->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"><!--Bootstrap4-->
    <title>登录</title>
</head>
<body>
      <div class="container">
          <div class="col">
              <form class="form-login" action="/login/" method="post">
                  <h3 class="text-center">欢迎登录</h3>
                  <div class="form-group">
                      <label for="id_username">用户名:</label>
                      <input type="text" name="username" class="form-control" id="id_username" placeholder="请输入您的用户名" autofocus required/>
                  </div>
                  <div class="form-group">
                      <label for="id_password">密码:</label>
                      <input type="password" name="password" id="id_password" class="form-control" placeholder="请输入您的密码" required>
                  </div>
                  <div>
                      <a href="/register/" class="text-success"><ins>新用户注册</ins></a>
                      <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
              </form>
          </div>
      </div>
      <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
      <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
      <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

最终的展示的界面为：

![image-20221001113215882](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221001113215882.png)

### 3、加载静态资源

现在还存在的问题就是，用户名与密码的输入框太长且背景太过于单调。整体的样式也不是我们想要的。因此，还需要进行进一步的优化，那么就加入相应的CSS语言，同时将背景图片也进行加载。

在login目录下创建文件static，在此文件下创建login。在login下创建css、image。其中css文件主要用于存放CSS文件，image主要存放对应的背景照片。新增后的目录结构如下：

![image-20221001151828770](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221001151828770.png)

在login.html文件中，将原有的代码进行修改，修改后的代码为：

```html
{% load static %} //新增
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
    <!--上面这一行必须放在最前面-->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"><!--Bootstrap4-->
    <link href="{% static 'login/css/login.css' %}" rel="stylesheet"> //新增
    <title>登录</title>
</head>
<body>
      <div class="container">
          <div class="col">
              <form class="form-login" action="/login/" method="post">
                  <h3 class="text-center">欢迎登录</h3>
                  <div class="form-group">
                      <label for="id_username">用户名:</label>
                      <input type="text" name="username" class="form-control" id="id_username" placeholder="请输入您的用户名" autofocus required/>
                  </div>
                  <div class="form-group">
                      <label for="id_password">密码:</label>
                      <input type="password" name="password" id="id_password" class="form-control" placeholder="请输入您的密码" required>
                  </div>
                  <div>
                      <a href="/register/" class="text-success"><ins>新用户注册</ins></a>
                      <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
              </form>
          </div>
      </div>
      <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
      <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
      <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

在login.css中加入以下代码：

```css
body {
  height: 100%;
  background-image: url('../image/bg.jpg');
}
.form-login {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-login{
  margin-top:80px;
  font-weight: 400;
}
.form-login .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;

}
.form-login .form-control:focus {
  z-index: 2;
}
.form-login input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-login input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
form a{
  display: inline-block;
  margin-top:25px;
  font-size: 12px;
  line-height: 10px;
}
```

注：照片可自己去找，但是得去进行相应的调整，这里就不赘述了。

### 4、启动服务器

在浏览器输入[登录](http://127.0.0.1:8000/login/)，进入我们的login页面，即可看到如下界面：

![image-20221001154814036](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221001154814036.png)

## 八、登录视图

### 1、登录视图配置

根据我们在路由中的设计，用户通过`login.html`中的表单填写用户名和密码，并以POST的方式发送到服务器的`/login/`地址。服务器通过`login/views.py`中的`login()`视图函数，接收并处理这一请求。视图中具体的login代码为：

```python
def index(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        return redirect('/index/')
    return render(request,'login/index.html',locals())
```

### 2、数据验证

现在存在的问题就是，我们在登录的时候缺少相应的消息提示；举个例子，若密码错误的话，在登录页面就会出现对应的消息提示。接下来，我们就要对这一部门进行完善。Let‘ go！！！

在view中的login中，将原有代码进行修改，具体代码如下：

```python
from django.shortcuts import render
from django.shortcuts import redirect
from . import models #在当前目录下引入models模型

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username,password)
        message = '请仔细检查您的输入！'
        if username.strip() and password: #通过strip函数去除掉账号和密码中的空白
            try:
                user= models.User.objects.get(name=username) #验证模板中的已存在用户与当前登录的用户是否一样
            except:
                message='您的账号不存在!'
                return render(request,'login/login.html',locals()) #若为不同，则继续在此页面进行登录
            if password==user.password:#若密码也正确的话，就跳转至主页
                return redirect('/index/')
            else:
                message = '您的密码输入有误!'
                return render(request, 'login/login.html',locals())
    return render(request,'login/login.html',locals())
```

在这之后，还需要在login.html中修改相应代码，具体如下：

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
    <!--上面这一行必须放在最前面-->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"><!--Bootstrap4-->
    <link href="{% static 'login/css/login.css' %}" rel="stylesheet">
    <title>登录</title>
</head>
<body>
      <div class="logo"></div>
      <div class="container">
          <div class="col">
              <form class="form-login" action="/login/" method="post">
                  {% if message%} #增加了if标签
                      <div class="alert alert-warning">{{ message }}</div>
                  {% endif %}#结束比钱
                  {% csrf_token %}
                  <h3 class="text-center">欢迎登录</h3>
                  <div class="form-group">
                      <label for="id_username">用户名:</label>
                      <input type="text" name="username" class="form-control" id="id_username" placeholder="请输入您的用户名" autofocus required/>
                  </div>
                  <div class="form-group">
                      <label for="id_password">密码:</label>
                      <input type="password" name="password" id="id_password" class="form-control" placeholder="请输入您的密码" required>
                  </div>
                  <div>
                      <a href="/register/" class="text-success"><ins>新用户注册</ins></a>
                      <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
              </form>
          </div>
      </div>
      <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
      <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
      <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

最终的结果如下：

输入错误账号的时候会出现：

![image-20221002140839923](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221002140839923.png)

输入错误的密码会出现：

![image-20221002140809160](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221002140809160.png)

## 九、Django表单

### 1、基础概述

Django中的表单是比较重要的一部分内容。

通常情况下，我们需要自己手动在HTML页面中，编写form标签和其内的其它元素。但这费时费力，而且有可能写得不太恰当，数据验证也比较麻烦。

有鉴于此，Django在内部集成了一个表单模块，专门帮助我们快速处理表单相关的内容。Django的表单模块给我们提供了下面三个主要功能：

- 准备和重构数据用于页面渲染
- 为数据创建HTML表单元素
- 接收和处理用户从表单发送过来的数据

编写Django的form表单，非常类似我们在模型系统里编写一个模型。在模型中，一个字段代表数据表的一列，而form表单中的一个字段代表`<form>`中的一个`<input>`元素。

### 2、结果验证

话不多说进行实操才是王道。首先我们在login中创建forms.py，创建后我们的目录结构如下：

![image-20221002142204237](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221002142204237.png)

在forms表单中，写入相应的代码：

```python
from django import forms #导入forms模块

class UsrForm(forms.Form):
    usrname = forms.CharField(max_length=100,label="用户名",
                              widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入您的账号','autofocus':''}))
    password = forms.CharField(label="密码",max_length=128,
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入您的密码'}))
```

在view.py中修改相应代码：

```python
def login(request):
    if request.method=='POST':
        login_form = forms.UsrForm(request.POST)#从Usr表单中获取信息
        #print(username,password)
        message = '请仔细检查您的输入！'
        if login_form.is_valid(): #若login_Form中的数据是有效的
            username = login_form.cleaned_data('usrname') #从用户输入中获取账号
            password = login_form.cleaned_data('password')#从用户输入中获取密码
        if username.strip() and password: #通过strip函数去除掉账号和密码中的空白
            try:
                user= models.User.objects.get(name=username) #验证模板中的已存在用户与当前登录的用户是否一样
            except:
                message='您的账号不存在!'
                return render(request,'login/login.html',locals()) #若为不同，则继续在此页面进行登录
            if password==user.password:#若密码也正确的话，就跳转至主页
                return redirect('/index/')
            else:
                message = '您的密码输入有误!'
                return render(request, 'login/login.html',locals())
    login_form = forms.UsrForm()
    return render(request,'login/login.html',locals())
```

同时还需要在login.html中修改相应的代码。具体操作如下：

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
    <!--上面这一行必须放在最前面-->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"><!--Bootstrap4-->
    <link href="{% static 'login/css/login.css' %}" rel="stylesheet">
    <title>登录</title>
</head>
<body>
      <div class="logo"></div>
      <div class="container">
          <div class="col">
              <form class="form-login" action="/login/" method="post">
                  {% if message%}
                      <div class="alert alert-warning">{{ message }}</div>
                  {% endif %}
                  {% csrf_token %}
                  <h2 class="text-center" style="font-size: 40px;font-family: 仿宋">欢迎登录</h2>

                  {{ login_form }} //就是这做出了修改

                  <div>
                      <a href="/register/" class="text-success"><ins>新用户注册</ins></a>
                      <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
              </form>
          </div>
      </div>
      <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
      <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
      <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

最终的界面效果为：

![image-20221002143919535](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221002143919535.png)

貌似有点拉胯，但是这个是不影响的，我们要用到表单渲染技术，将其变得更为漂亮、工整。

在login.html进行修改，其代码为：

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
    <!--上面这一行必须放在最前面-->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"><!--Bootstrap4-->
    <link href="{% static 'login/css/login.css' %}" rel="stylesheet">
    <title>登录</title>
</head>
<body>
      <div class="logo"></div>
      <div class="container">
          <div class="col">
              <form class="form-login" action="/login/" method="post">
                  {% if message%}
                      <div class="alert alert-warning">{{ message }}</div>
                  {% endif %}
                  {% csrf_token %}
                  <h2 class="text-center" style="font-size: 40px;font-family: 仿宋">欢迎登录</h2>

                  <div class="form-group">
                      {{ login_form.usrname.label_tag }}
                      {{ login_form.usrname }}
                  </div>

                  <div class="form-group">
                      {{ login_form.password.label_tag }}
                      {{ login_form.password }}
                  </div>

                  <div>
                      <a href="/register/" class="text-success"><ins>新用户注册</ins></a>
                      <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
              </form>
          </div>
      </div>
      <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
      <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
      <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

那么最终的结果为：

![image-20221002145014126](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221002145014126.png)

## 十、session会话

### 1、基础概述

我们知道，HTTP是无状态、无连接的协议，但是只要结合实际场景的话，你显然会对这个说法感到疑惑，因为有很多实际应用中的例子，似乎都表明了HTTP是’有状态’的。比方说，你登录一个网站，并没有输入账号密码就会自动登录，你在购物车中购买的商品，并没有标注你的身份就可以被服务器正确识别，这又是怎么一回事呢？其实做到这些的，不是HTTP，而是另外两个技术，Cookie和Session。

我们登录一个网站输入网址，就相当于为浏览器与服务器开启了一次临时会话，在这次会话中，不可避免的要产生很多数据，但HTTP是无状态的，为了记住这些数据，从而出现了Cookie和Session。其中，Cookie是客户端技术，而Session是服务端技术。因为Cookie保存在客户端，因此Cookie中的信息并不是很安全，我们通常将一些不是很重要的信息保存在Cookie中，而将一些用户的关键性信息保存在Session中。

**当浏览器向服务器发送一个请求时，浏览器会自动生成一个Session和一个Session ID，Session ID用来唯一标注这个Session，然后将该ID发送给浏览器，之后浏览器如果发生第二次请求，会将该Session ID一同发送给服务器，服务器会根据ID找到相应的Session，这样就基本保证了有状态。**

------

### 2、使用session

首先，我们要在view.py中修改login()的视图函数。具体操作如下：

```python
def login(request):
    if request.session.get('is_login','None'): #若当前账户已经登录
        return redirect('/index/') #则直接跳转至主页
    if request.method=='POST':
        login_form = forms.UsrForm(request.POST)#从Usr表单中获取信息
        #print(username,password)
        message = '请仔细检查您的输入！'
        if login_form.is_valid(): #若login_Form中的数据是有效的
            username = login_form.cleaned_data.get('usrname') #从用户输入中获取账号
            password = login_form.cleaned_data.get('password')#从用户输入中获取密码
        if username.strip() and password: #通过strip函数去除掉账号和密码中的空白
            try:
                user= models.User.objects.get(name=username) #验证模板中的已存在用户与当前登录的用户是否一样
            except:
                message='您的账号不存在!'
                return render(request,'login/login.html',locals()) #若为不同，则继续在此页面进行登录
            if password==user.password:#若密码也正确的话，就跳转至主页
                request.session['is_login'] = True #将当前登录状态写入session字典
                request.session['user_id'] = user.id #将当前登录数据写入session字典
                request.session['user_name'] = user.name #将当前登录数据写入session字典
                return redirect('/index/')
            else:
                message = '您的密码输入有误!'
                return render(request, 'login/login.html',locals())
    login_form = forms.UsrForm()
    return render(request,'login/login.html',locals())
```

在logout()也进行相应的修改，具体操作如下：

```python
def logout(request):
    if not request.session.get('is_login','None'): #若当前不是登录状态则直接退出至login
        return redirect('/login/')
    request.session.flush() #否则就退出，同时清除session数据
    return redirect('/login/')
```

### 3、session验证

现在我们有了用户状态，就可以根据用户的登录与否，从而给予其展示不同的界面。我们以index为例进行验证，进入index.html修改代码，具体操作如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
<h1>{{ request.session.user_name }}!  欢迎回来！</h1>
<p>
    <a href="/logout/">登出</a>
</p>
</body>
</html>
```

在视图中也需要修改部分代码，具体操作为：

```python
def index(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    return render(request,'login/index.html',locals())
```

那么，我们的想要的结果就是，我们在浏览器输入：127.0.0.1:8000/index,的时候会自动跳转至login界面。其结果为：

![image-20221003154141610](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221003154141610.png)

## 十一、注册功能

项目做到现在，基本就快大功告成了。我们的目的是完成一个登录注册的功能，但是现在只是完成了登录的功能，并没有实现注册的功能，在前期我们将注册的接口已经写好，现在只是完善。让我们开始吧。

### 1、完善表单

具体的实现过程与登录表单类似，这里不做赘述。

```python
class RegisterForm(forms.Form):

    gender = (
        ('male',"男")
        ('female',"女")
    )


    usrname = forms.CharField(label='用户名',max_length=100,
                              widget=forms.TextInput(attrs={'holderplace':'请填写您的用户名','class':'form-control'}))
    password = forms.CharField(label='密码',max_length=100,
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请填写您的密码'}))
    password1 = forms.CharField(label='确认密码', max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次确认您的密码'}))
    email = forms.EmailField(label='邮箱',max_length=128,
                            widget=forms.EmailInput(attrs={'class':'form-control','holderplace':'请填写您的邮箱账号'}))
    sex = forms.ChoiceField(label="性别",choices=gender)
```

### 2、注册视图配置

也是基本的操作，并没有涉及多深奥的东西，主要是在views.py中的register函数中进行晚上补全，具体的代码操作为：

```python
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
             new_user.password=password
             new_user.email = email
             new_user.sex = sex
             new_user.save()

             time.sleep(2)      
             return redirect('/login/')
         else:
             return render(request, 'login/register.html', locals())
     register_form=forms.RegisterForm()
     return render(request,'login/register.html',locals())
```

------

打开register.html完善其中的代码，话不多说，直接上代码：

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=width-device,initial-scale=1,shrink-to-fit=no">
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link href="{% static 'login/css/register.css' %}" rel = "stylesheet"/>
    <title>注册</title>
</head>

<body>
      <div class="container">
          <div class="col">
              <form class="form-register" method="post" action="/register/">
                  {% if message %}
                      <div class="alert alert-warning">{{ message }}</div>
                  {% endif %}

                 {% csrf_token %}
                 <h3 class="text-center">欢迎注册</h3>
                 <div class="form-group">
                    {{ register_form.usrname.label_tag }}
                    {{ register_form.usrname }}
                 </div>
                 <div class="form-group">
                    {{ register_form.password.label_tag }}
                    {{ register_form.password }}
                 </div>
                 <div class="form-group">
                    {{ register_form.password1.label_tag }}
                    {{ register_form.password1 }}
                 </div>
                 <div class="form-group">
                    {{ register_form.email.label_tag }}
                    {{ register_form.email }}
                 </div>
                 <div class="form-group">
                    {{ register_form.sex.label_tag }}
                    {{ register_form.sex }}
                 </div>
                 <a href="/login/ "><ins>直接登录</ins></a>
                  <button class="btn btn-primary float-right">注册</button>

              </form>
          </div>
      </div>
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
    <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

### 3、结果验证

![image-20221004144852996](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221004144852996.png)

![image-20221004144915345](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221004144915345.png)

若注册成功之后，等待2是则跳转至登录界面：

![image-20221004151905814](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221004151905814.png)

## 十二、密码加密

### 1、基础概述

我们现在通过超级管理员进行登录的时候，账号、密码等信息可以被随便看到，因为我们需要通过加密算法对密码进行加密，从而进一步的保护我们用户的隐私。接下来，我们就开干：

![image-20221004152332904](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221004152332904.png)

其实本质来说，所谓的加密算法的实现并不复杂，只要在view中写一个全局函数，然后在login、register中利用上此函数就好，具体的操作为：

```python
import hashlib #引入哈希库

def HashCode(s,salt="MyWeb"):
    h = hashlib.sha256()
    s+=salt
    h.update(s.encode())
    return h.hexdigest()
```

在login中的代码是：

```html
def login(request):
    if request.session.get('is_login',None): #若当前账户已经登录
        return redirect('/index/') #则直接跳转至主页
    if request.method=='POST':
        login_form = forms.UsrForm(request.POST)#从Usr表单中获取信息
        #print(username,password)
        message = '请仔细检查您的输入！'
        if login_form.is_valid(): #若login_Form中的数据是有效的
            username = login_form.cleaned_data.get('usrname') #从用户输入中获取账号
            password = login_form.cleaned_data.get('password')#从用户输入中获取密码
        #if username.strip() and password: #通过strip函数去除掉账号和密码中的空白
            try:
                user= models.User.objects.get(name=username) #验证模板中的已存在用户与当前登录的用户是否一样
            except:
                message='您的账号不存在!'
                return render(request,'login/login.html',locals()) #若为不同，则继续在此页面进行登录

            if password==HashCode(password):#若密码也正确的话，就跳转至主页
                request.session['is_login'] = True #将当前登录状态写入session字典
                request.session['user_id'] = user.id #将当前登录数据写入session字典
                request.session['user_name'] = user.name #将当前登录数据写入session字典
                return redirect('/index/')
            else:
                message = '您的密码输入有误!'
                return render(request, 'login/login.html',locals())
    login_form = forms.UsrForm()
    return render(request,'login/login.html',locals())

```

在register中的代码为：

```python
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
```

### 2、结果展示

![image-20221004154719724](C:\Users\HanPu\AppData\Roaming\Typora\typora-user-images\image-20221004154719724.png)
