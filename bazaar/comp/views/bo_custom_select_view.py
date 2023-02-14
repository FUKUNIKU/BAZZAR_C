from django.views.generic import TemplateView
from comp.models import Store,Menu
from accounts.models import CustomUser

class CustomSelectView(TemplateView):
    template_name="comp/bo_custom_select.html"
    model = Store,Menu,CustomUser


    def get_context_data(self,**kwargs):

        if Store.objects.filter(bp_id_id = self.request.user.userid):
            context = super(CustomSelectView,self).get_context_data(**kwargs)
            customuserid = CustomUser.objects.get(userid = self.request.user.userid)
            registration_store = Store.objects.filter(bp_id_id = customuserid.userid)

            Store.objects.filter(bp_id_id = customuserid.userid)
            storeid = Store.objects.get(bp_id_id = customuserid.userid)
            registration_menu = Menu.objects.filter(store_id_id = storeid.store_id)

            context['registration_store'] = registration_store
            context['registration_menu'] = registration_menu

            return context
