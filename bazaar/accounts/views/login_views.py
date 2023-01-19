from django.shortcuts import render

# ここから追加
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from ..forms import LoginForm

# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class LoginViews(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


#ログイン
# def Login(request):
#     # POST
#     if request.method == 'POST':
#         # フォーム入力のユーザーID・パスワード取得
#         ID = request.POST.get('userid')
#         Pass = request.POST.get('password')

#         # Djangoの認証機能
#         user = authenticate(userid=ID, password=Pass)

#         # ユーザー認証
#         if user:
#             #ユーザーアクティベート判定
#             if user.is_active:
#                 # ログイン
#                 login(request,user)
#                 # ホームページ遷移
#                 return HttpResponseRedirect(reverse('test'))
#             else:
#                 # アカウント利用不可
#                 return HttpResponse("アカウントが有効ではありません")
#         # ユーザー認証失敗
#         else:
#             return HttpResponse("ログインIDまたはパスワードが間違っています")
#     # GET
#     else:
#         return render(request, 'accounts/login.html')



    
