from django.db import models
# from user.models.users import User
# from .business_person import Business_person
from .memu import Menu
from accounts.models import CustomUser
from .store import Store
from django.utils import timezone
from bootstrap_datepicker_plus.widgets import DatePickerInput
#予約のModel

class Reservation(models.Model):
   #store_id,user_id,timeの合同主キー
   mon="mon"
   tue="tue"
   wed="wed"
   thr="thr"
   fri="fri"
   sat="sat"
   sun="sun"
   cel="祝日"
   none="なし"
   date=[
      ('月曜日','月曜日'),
      ('火曜日','火曜日'),
      ('水曜日','水曜日'),
      ('木曜日','木曜日'),
      ('金曜日','金曜日'),
      ('土曜日','土曜日'),
      ('日曜日','日曜日'),
      ('祝日','祝日'),
      ('なし','なし')
    ]
   df="選択してください"
   hour=[
      (1,1),
      (2,2),
      (3,3),
      (4,4),
      (5,5),
      (6,6),
      (7,7),
      (8,8),
      (9,9),
      (10,10),
      (11,11),
      (12,12),
      (13,13),
      (14,14),
      (15,15),
      (16,16),
      (17,17),
      (18,18),
      (19,19),
      (20,20),
      (21,21),
      (22,22),
      (23,23),
      (24,24),
    ]
   minute=[
      ("00分","00分"),
      ("15分","15分"),
      ("30分","30分"),
      ("45分","45分"),
    ]
   store_id=models.ForeignKey(Store,to_field='store_id',verbose_name='店舗ID',on_delete=models.PROTECT) 
   user_id=models.ForeignKey(CustomUser,to_field='userid',verbose_name='ユーザーID',max_length=16,on_delete=models.PROTECT,null=True,blank=True)
   menu1=models.IntegerField(verbose_name='数量')
   menu2=models.IntegerField(verbose_name='数量')
   menu3=models.IntegerField(verbose_name='数量')
   menu4=models.IntegerField(verbose_name='数量')
   reservation_name=models.CharField(verbose_name='予約者名',max_length=20,null=True,blank=True)
   reservation_mail=models.EmailField(verbose_name='予約者メールアドレス',max_length=40,null=True,blank=True)
   reservation_day=models.CharField(verbose_name='予約希望日',max_length=20)
   reservation_phone=models.CharField(verbose_name='予約者電話番号',max_length=11,null=True,blank=True)
   reservation_hour=models.IntegerField(verbose_name='予約時間')
   nop=models.IntegerField(verbose_name='予約人数')

   def __str__(self):
                                                                      
     st= str(self.reservation_hour) + str(self.reservation_name)
     return st
