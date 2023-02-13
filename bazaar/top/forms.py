from django import forms
from django.core.mail import EmailMessage
from django.shortcuts import render


# def clean_Inquiry_email(value):
#     if '@' not in value:
#         raise forms.ValidationError('@を含んだメールアドレスにしてください')
#     return value

class InquiryForm(forms.Form):

    # Inquiry = forms.CharField(label = "お問い合わせ内容" , required = True ,widget = forms.Textarea)
    # Inquiry_name = forms.CharField(label = "お名前" , required = True , max_length = 20, widget = forms.TextInput)
    # Inquiry_email = forms.EmailField(label = "メールアドレス" ,validators=[clean_Inquiry_email], required = True , max_length = 50, widget = forms.TextInput,)

    inquiry = forms.CharField(label = "お問い合わせ内容" , required = True ,widget = forms.Textarea)
    inquiry_name = forms.CharField(label = "お名前" , required = True , max_length = 20, widget = forms.TextInput)
    inquiry_email = forms.EmailField(label = "メールアドレス" , required = True , max_length = 50, widget = forms.TextInput)

    def clean_Inquiry_email(self):
        inquiry_email = self.cleaned_data['inquiry_email']
        if '@' not in inquiry_email:
            raise forms.ValidationError('@を含んだメールアドレスにしてください')
        return inquiry_email


def send_email(abc):
    inquiry = abc["inquiry"]
    inquiry_name = abc["inquiry_name"]
    inquiry_email = abc["inquiry_email"]

    message = "お問い合わせ内容:{0}\nお名前:{1}\nメールアドレス:{2}".format(inquiry,inquiry_name,inquiry_email)
    from_email = 'admin@example.com'
    to_list = [
        'test@example.com' #宛先
    ]
    cc_list = [
        inquiry_email #共有したいメールアドレス
    ]

    message = EmailMessage(body = message, from_email = from_email, to = to_list, cc = cc_list)
    message.send()

