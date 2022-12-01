from django.urls import path
from .views.login_views import LoginViews
from .views.password_reset_views import PasswordReset
from .views.password_reset_send_views import PasswordResetDone
from .views.password_reset_confim_views import PasswordResetConfirm
from .views.password_reset_complete_views import PasswordResetComplete

app_name ='accounts'

urlpatterns =[
    path('', LoginViews.as_view(), name='login'),#ログインページ
    #path('logout/', views.Logout.as_view(), name='logout'),#ログアウトページ
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),#パスワードリセットページ
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),#パスワードリセット用のメールを送信しましたページ
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),#新パスワード入力用ページ
    path('password_reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),#パスワード更新完了ページ
]
      