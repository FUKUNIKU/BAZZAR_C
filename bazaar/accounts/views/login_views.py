from django.shortcuts import render

# ここから追加
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from ..forms import LoginForm


class LoginViews(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'
    