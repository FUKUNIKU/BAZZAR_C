from django.views.generic import TemplateView
from django.views.generic import ListView
from ..models import Reservation,Store,Menu
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from  datetime import date,datetime,timedelta
# class CompReservationListView(TemplateView):
#     template_name: str = 'comp/bo_reservation_list.html'



class CompReservationListView(LoginRequiredMixin,ListView):
    model = Reservation
    #context_object_name = "reservation_list"
    template_name: str = 'comp/bo_reservation_list.html'

    def get_context_data(self, **kwargs):
        context = super(CompReservationListView, self).get_context_data(**kwargs)
        #予約情報を取得
        #現在の日付を取得
        dt_now = datetime.now()
        #2日後の日付を取得
        dt_2day = dt_now + timedelta(days=2)
        #StoreテーブルからログインしているユーザーのストアIDを取得
        store = Store.objects.get(bp_id_id = self.request.user.userid)
        store_id = store.store_id

        #メニュー名を取得
        menu = Menu.objects.get(store_id_id = store_id)
        menu1 = menu.menu_name1
        menu2 = menu.menu_name2
        menu3 = menu.menu_name3
        menu4 = menu.menu_name4
        context['menu1']=menu1
        context['menu2']=menu2
        context['menu3']=menu3
        context['menu4']=menu4


        #予約を取得
        reservation = Reservation.objects.filter(reservation_day__range=[dt_now, dt_2day])
        reservation = reservation.filter(store_id_id = store_id).order_by('reservation_day','reservation_hour')
        context['reservation'] = reservation

        return context

    # def get_queryset(self):
    #     reservations = Reservation.objects.filter(store_id_id = store_id)
    #     return reservations
    


