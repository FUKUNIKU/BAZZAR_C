from django.db import models
#from .business_person import Business_person

from accounts.models import CustomUser
from .store import Store


#メニューのModel

class Menu(models.Model):
   #store_id,menu_name,sizeの合同主キー
   store_id=models.ForeignKey(Store,to_field='store_id',verbose_name='店舗ID',on_delete=models.PROTECT)
   menu_name1=models.CharField(verbose_name='メニュー名',max_length=50)
   size1=models.CharField(verbose_name='サイズ',max_length=3) 
   price1=models.IntegerField(verbose_name='値段')
   photo1=models.ImageField(upload_to="media",verbose_name='写真',blank=True,null=True)
   about1=models.TextField(verbose_name='紹介文',max_length=300)

   menu_name2=models.CharField(verbose_name='メニュー名',max_length=50)
   size2=models.CharField(verbose_name='サイズ',max_length=3) 
   price2=models.IntegerField(verbose_name='値段')
   photo2=models.ImageField(upload_to="media",verbose_name='写真',blank=True,null=True)
   about2=models.TextField(verbose_name='紹介文',max_length=300)

   menu_name3=models.CharField(verbose_name='メニュー名',max_length=50)
   size3=models.CharField(verbose_name='サイズ',max_length=3) 
   price3=models.IntegerField(verbose_name='値段')
   photo3=models.ImageField(upload_to="media",verbose_name='写真',blank=True,null=True)
   about3=models.TextField(verbose_name='紹介文',max_length=300)

   menu_name4=models.CharField(verbose_name='メニュー名',max_length=50)
   size4=models.CharField(verbose_name='サイズ',max_length=3) 
   price4=models.IntegerField(verbose_name='値段')
   photo4=models.ImageField(upload_to="media",verbose_name='写真',blank=True,null=True)
   about4=models.TextField(verbose_name='紹介文',max_length=300)

   def __str__(self):
      return self.menu_name1

