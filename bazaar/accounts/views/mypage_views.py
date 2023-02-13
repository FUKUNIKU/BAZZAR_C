from django.views.generic import TemplateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from comp.models import Store,Menu
from accounts.models import CustomUser


#ログインしていることが条件
class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/mypage.html"
    model = Store,Menu,CustomUser


    def get_context_data(self, **kwargs):
        context = super(MypageView,self).get_context_data(**kwargs)


        if CustomUser.objects.filter(userid = self.request.user.userid):
            customuserid = CustomUser.objects.get(userid = self.request.user.userid)
            registration_store = Store.objects.filter(bp_id_id = customuserid.userid)
            context['registration_store'] = registration_store
        elif Store.objects.filter(bp_id_id = customuserid.userid):
            storeid = Store.objects.get(bp_id_id = customuserid.userid)
            registration_menu = Menu.objects.filter(store_id_id = storeid.store_id)
            context['registration_menu'] = registration_menu
        else:
            context['usertype'] = self.request.user.usertype


        return context
