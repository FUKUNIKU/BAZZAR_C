from django.views.generic import TemplateView
from django.views.generic import ListView
from ..models import Reservation,Store,Menu
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# class CompReservationListView(TemplateView):
#     template_name: str = 'comp/bo_reservation_list.html'



class CompReservationListAllView(LoginRequiredMixin,ListView):
    model = Reservation
    #context_object_name = "reservation_list"
    template_name: str = 'comp/bo_reservation_listall.html'

    def get_context_data(self, **kwargs):
        context = super(CompReservationListAllView, self).get_context_data(**kwargs)
        #予約情報を取得

        #StoreテーブルからログインしているユーザーのストアIDを取得
        store = Store.objects.get(bp_id_id = self.request.user.userid)
        store_id = store.store_id
        reservation = Reservation.objects.filter(store_id_id = store_id).order_by('reservation_day','reservation_hour').reverse()
        #reservation = reservation.filter(reservation.values(reservation_day__range=[dt_now, dt_2day]))
        context['reservation'] = reservation
        return context

        #メニュー１～５のメニュー名を取得
        # menu1_id = reservation.values('menu1_id')
        # menu1_name = Menu.objects.filter(id__in = menu1_id)
        # context['menu1_name'] = menu1_name

        # menu2_id = reservation.values('menu2_id')
        # menu2_name = Menu.objects.filter(id__in = menu2_id)
        # context['menu2_name'] = menu2_name

        # menu3_id = reservation.values('menu3_id')
        # menu3_name = Menu.objects.filter(id__in = menu3_id)
        # context['menu3_name'] = menu3_name

        # menu4_id = reservation.values('menu4_id')
        # menu4_name = Menu.objects.filter(id__in = menu4_id)
        # context['menu4_name'] = menu4_name

        # menu5_id = reservation.values('menu5_id')
        # menu5_name = Menu.objects.filter(id__in = menu5_id)
        # context['menu5_name'] = menu5_name
        
        # return context

    # def get_queryset(self):
    #     reservations = Reservation.objects.filter(store_id_id = store_id)
    #     return reservations
    


    # user_store_id = get_store_id()
    # queryset = Reservation.objects.filter(store_id=user_store_id)


