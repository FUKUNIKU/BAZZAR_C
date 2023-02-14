from django import forms
import sys
import pathlib
from django.core.mail import EmailMessage
currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir)+"..comp/")
# from comp.models.business_person import Business_person
# from.models.users import User
from accounts.models import CustomUser
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from comp.models import Kuchikomi
from comp.models import Reservation
from bootstrap_datepicker_plus.widgets import DatePickerInput

class LoginBusiness_personForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('userid', 'password')
        labels = {
            'userid': 'ユーザーID',
            'password': 'パスワード',
        }
        widgets = {
            'userid': forms.TextInput,
            'password': forms.TextInput,
        }



class RegisterForm(UserCreationForm):
    userid=forms.CharField(label='ユーザーID',min_length=8,max_length=16)
    password1=forms.CharField(label='パスワード',min_length=8,max_length=16,widget=forms.PasswordInput)
    password2=forms.CharField(label='パスワード(再入力)',min_length=8,max_length=16,widget=forms.PasswordInput)
    username=forms.CharField(label='名前',max_length=20)
    mail=forms.EmailField(label='メールアドレス',max_length=40)
    phone = forms.CharField(label='電話番号' ,max_length = 16)

    class Meta:
        model=CustomUser
        fields =(CustomUser.USERNAME_FIELD,'username','mail','phone')
        labels= {
            'userid':'ユーザーID',
            'username':'名前',
            'mail':'メールアドレス',
            'phone':'電話番号',
        }

        
        

class SaveForm(forms.Form):
    
    userid=forms.CharField(label='ユーザーID',min_length=8,max_length=16)
    password=forms.CharField(label='パスワード',min_length=8,max_length=16,widget=forms.PasswordInput)
    confirm_password=forms.CharField(label='パスワード(再入力)',min_length=8,max_length=16,widget=forms.PasswordInput)

    # username=forms.CharField(label='名前',max_length=20)
    # mail=forms.EmailField(label='メールアドレス',max_length=40)
    # phone = forms.CharField(label='電話番号' ,max_length = 16)  

    
class KutikomiForm(forms.ModelForm):
    class Meta:
        model = Kuchikomi
        fields = ('store_id','user_id','score','impression',)

        exclude = ["store_id",'user_id']

class ReservationForm(forms.ModelForm):
   
    class Meta:
        model= Reservation
        exclude = ["user_id","menu5","store_id","reservation_day","reservation_hour"]

        
class ReservationLoginForm(forms.ModelForm):
   
    class Meta:
        model= Reservation
        exclude = ["store_id","user_id","reservation_name","reservation_phone","reservation_mail","menu1","menu2","menu3","menu4","menu5"]
      


def send_email(abc):
    res_day = abc["reservation_day"]
    res_hour = abc["reservation_hour"]
    res_name = abc["reservation_name"]
    res_mail = abc["reservation_mail"]
    res_phone = abc["reservation_phone"]
    res_nop = abc["nop"]
    day=str(res_day)
    hour=str(res_hour)
    name=str(res_name)
    mail=str(res_mail)
    phone=str(res_phone)
    nop=str(res_nop)
    message = "予約内容:{0}\n予約日:{1}\n時間:{1}\nお名前:{1}\nメールアドレス:{2}\n電話番号:{3}\n予約可能席数:{3}".format(day,hour,name,mail,phone,nop)
    from_email = 'admin@example.com'
    to_list = [
        'test@example.com' #宛先
    ]
    cc_list = [
        res_mail #共有したいメールアドレス
    ]

    message = EmailMessage(body = message, from_email = from_email, to = to_list, cc = cc_list)
    message.send()

