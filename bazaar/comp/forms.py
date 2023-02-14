from django import forms
from django.db import models
import sys
import pathlib
from django.core.mail import EmailMessage
currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir)+"..comp/")
# from comp.models.business_person import Business_person
# from.models.users import User 
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from comp.models import Store
from comp.models import Menu
# from django.contrib.auth.forms.UserCreationForm import clean_password2

# CustomUser = get_user_model()

class LoginCustomUserForm(AuthenticationForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['userid'].widget = forms.TextInput(attrs={'required': 'true', 'placeholder': 'ユーザーID'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'required': 'true', 'placeholder': 'パスワード'})
        self.fields['userid'].widget.attrs['name'] = 'userid'
        self.fields['password'].widget.attrs['name'] = 'password'
        
    class Meta:
        model = CustomUser
        fields = ('userid', 'password')
        labels = {
            'userid': '事業者ID',
            'password': 'パスワード',
        }
        
class RegisterForm(UserCreationForm):

    userid=forms.CharField(label='ユーザーID',min_length=8,max_length=16)
    username=forms.CharField(label='名前',max_length=20)
    mail=forms.EmailField(label='メールアドレス',max_length=40)
    phone = forms.CharField(label='電話番号' ,max_length = 16)
    adress=forms.CharField(label='住所',min_length= 6)


    class Meta:
        model=CustomUser
        
        fields =(CustomUser.USERNAME_FIELD,'username','mail','phone','adress')
        labels= {
            'userid':'ユーザーID',
            'username':'名前',
            'mail':'メールアドレス',
            'phone':'電話番号',
            'adress':'住所',
        }
    
    def form_valid(self, form):
            user = form.save(commit=False)
            user.usertype = 'comp'
            user.save()
        

class StoreForm(forms.ModelForm):
    class Meta:
        model=Store
        exclude = ["bp_id"]


class MenuForm(forms.ModelForm):
    class Meta:
        model= Menu
        exclude = ["store_id"]

class DeleteForm(forms.Form):

    delete_store_id = forms.CharField(label = "店舗ID" , required = True)

def send_email(abc):
    delete_store_id = abc["delete_store_id"]

    message = "削除要請について\nstore_id:{0}".format(delete_store_id)
    from_email = 'admin@example.com'
    to_list = [
        'test@example.com' #宛先
    ]


    message = EmailMessage(body = message, from_email = from_email, to = to_list)
    message.send()
