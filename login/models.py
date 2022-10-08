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
        ordering = ["c_time"]  #按照创建时间排序
        verbose_name = "用户"
        verbose_name_plural ="用户"
