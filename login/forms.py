from django import forms #导入forms模块

class UsrForm(forms.Form):
    usrname = forms.CharField(max_length=100,label="用户名",
                              widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入您的账号','autofocus':''}))
    password = forms.CharField(label="密码",max_length=128,
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入您的密码'}))



class RegisterForm(forms.Form):

    gender = (
        ('male',"男"),
        ('female',"女"),
    )


    usrname = forms.CharField(label='用户名',max_length=100,
                              widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请填写您的用户名'}))
    password = forms.CharField(label='密码',max_length=100,
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请填写您的密码'}))
    password1 = forms.CharField(label='确认密码', max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次确认您的密码'}))
    email = forms.EmailField(label='邮箱',max_length=128,
                            widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'请填写您的邮箱账号'}))
    sex = forms.ChoiceField(label="性别",choices=gender)
