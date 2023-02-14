from django.views.generic import UpdateView
from ..models.store import Store
from ..forms import StoreForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured

class CompStoreUpdateView(UpdateView):
    model=Store
    fields = ['store_name', 'postal_code', 'adress1', 'adress2','adress3','phone_number',
    'seat','seat','bussiness_hours_start','bussiness_hours_end',
    'holiday1','holiday2','holiday3','photo1','photo2','photo3','photo4','photo5','photo6','photo7','photo8','photo9','photo10']
    template_name='comp/bo_mystore_update.html'


    def get_object(self):
        return Store.objects.get(bp_id=self.request.user) # or request.POST
    def get_success_url(self):
        return reverse_lazy("accounts:mypage")