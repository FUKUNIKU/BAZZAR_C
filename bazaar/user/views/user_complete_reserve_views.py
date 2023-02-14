from django.views.generic import FormView,CreateView,TemplateView,ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ..forms import ReservationForm
from comp.models import Store,Reservation,Menu
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render

from django.core.exceptions import ValidationError


class UserCheckReserveView(FormView):
     template_name="user/user_check_reserve.html"
     form_class = ReservationForm
     def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        r_store=self.kwargs.get('pk')
        store=Store.objects.get(store_id=r_store)
        menu=Menu.objects.get(store_id=r_store)
        menuname1=menu.menu_name1
        menuname2=menu.menu_name2
        menuname3=menu.menu_name3
        menuname4=menu.menu_name4
        ctx['store']=store
        ctx['menu_1']=menuname1
        ctx['menu_2']=menuname2
        ctx['menu_3']=menuname3
        ctx['menu_4']=menuname4
        ctx['reservation_name']=self.request.POST('reservation_name')
        ctx['reservation_day']=self.request.POST('reservation_day')
        ctx['reservation_hour']=self.request.POST('reservation_hour')
        return render(request=self.request,template_name="user/user_check_reserve.html",context={'form':ctx})



class UserCompleteReserveView(TemplateView):
    template_name="user/user_complete_reserve.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        r_store=self.kwargs.get('pk')
        store=Store.objects.get(store_id=r_store)
        menu=Menu.objects.get(store_id=r_store)
        menuname1=menu.menu_name1
        menuname2=menu.menu_name2
        menuname3=menu.menu_name3
        menuname4=menu.menu_name4
        ctx['store']=store
        ctx['menu_1']=menuname1
        ctx['menu_2']=menuname2
        ctx['menu_3']=menuname3
        ctx['menu_4']=menuname4
        ctx['reservation_name']=self.request.POST('reservation_name')
        ctx['reservation_day']=self.request.POST('reservation_day')
        ctx['reservation_hour']=self.request.POST('reservation_hour')
        return ctx