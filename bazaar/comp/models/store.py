from django.db import models
from django.conf import settings
# from .business_person import Business_person
from accounts.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator

#店舗のModel

class Store(models.Model):
    
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
    prefectures = [
        ('北海道', '北海道'),
        ('青森', '青森'),
        ('岩手', '岩手'),
        ('宮城', '宮城'),
        ('秋田', '秋田'),
        ('山形', '山形'),
        ('福島', '福島'),
        ('茨城', '茨城'),
        ('栃木', '栃木'),
        ('群馬', '群馬'),
        ('埼玉', '埼玉'),
        ('千葉', '千葉'),
        ('東京', '東京'),
        ('神奈川', '神奈川'),
        ('新潟', '新潟'),
        ('富山', '富山'),
        ('石川', '石川'),
        ('福井', '福井'),
        ('山梨', '山梨'),
        ('長野', '長野'),
        ('岐阜', '岐阜'),
        ('静岡', '静岡'),
        ('愛知', '愛知'),
        ('三重', '三重'),
        ('滋賀', '滋賀'),
        ('京都', '京都'),
        ('大阪', '大阪'),
        ('兵庫', '兵庫'),
        ('奈良', '奈良'),
        ('和歌山', '和歌山'),
        ('鳥取', '鳥取'),
        ('島根', '島根'),
        ('岡山', '岡山'),
        ('広島', '広島'),
        ('山口', '山口'),
        ('徳島', '徳島'),
        ('香川', '香川'),
        ('愛媛', '愛媛'),
        ('高知', '高知'),
        ('福岡', '福岡'),
        ('佐賀', '佐賀'),
        ('長崎', '長崎'),
        ('熊本', '熊本'),
        ('大分', '大分'),
        ('宮城', '宮城'),
        ('鹿児島', '鹿児島'),
        ('沖縄', '沖縄'),
    ]
    #store_idが主キー
    store_id = models.AutoField(verbose_name='storeid',primary_key=True)
    bp_id=models.ForeignKey(CustomUser,to_field='userid',verbose_name='事業者ID',max_length=16,on_delete=models.PROTECT)
    store_name=models.CharField(verbose_name='店舗名',max_length=30)
    #CustomUserのほうが事業者の住所,Storeのほうが店舗の住所.
    postal_code=models.CharField(verbose_name='郵便番号',max_length=8)
    adress1=models.CharField(verbose_name='住所(xx県)',max_length=20, choices=prefectures)
    adress2=models.CharField(verbose_name='住所(xx市)',max_length=20)
    adress3=models.CharField(verbose_name='住所(xx丁目xx番地)',max_length=20)
    adress4=models.CharField(verbose_name='住所(ビル名など)',max_length=20)
    phone_number=models.CharField(verbose_name='電話番号',max_length=13)
    #seatが店全体の席数。seat_reservationableが時間ごとに予約可能な席数

    seat=models.IntegerField(verbose_name='席数',validators=[MinValueValidator(0)])
    bussiness_hours_start=models.IntegerField(verbose_name='営業開始',choices=hour,default="選択してください")
    bussiness_hours_end=models.IntegerField(verbose_name='営業終了',choices=hour,default=df)
    holiday1=models.CharField(verbose_name="定休日1" ,max_length=4,choices=date,default=cel)
    holiday2=models.CharField(verbose_name="定休日2" ,max_length=4,choices=date,default=none)
    holiday3=models.CharField(verbose_name="定休日3" ,max_length=4,choices=date,default=none)
    photo1=models.ImageField(upload_to="media", verbose_name='写真1',blank=True,null=True)
    photo2=models.ImageField(upload_to="media",verbose_name='写真2',blank=True,null=True)
    photo3=models.ImageField(upload_to="media",verbose_name='写真3',blank=True,null=True)
    photo4=models.ImageField(upload_to="media",verbose_name='写真4',blank=True,null=True)
    photo5=models.ImageField(upload_to="media",verbose_name='写真5',blank=True,null=True)
    photo6=models.ImageField(upload_to="media",verbose_name='写真6',blank=True,null=True)
    photo7=models.ImageField(upload_to="media",verbose_name='写真7',blank=True,null=True)
    photo8=models.ImageField(upload_to="media",verbose_name='写真8',blank=True,null=True)
    photo9=models.ImageField(upload_to="media",verbose_name='写真9',blank=True,null=True)
    photo10=models.ImageField(upload_to="media",verbose_name='写真10',blank=True,null=True)
    about=models.TextField(verbose_name='紹介文',max_length=300)

    def __str__(self):
        return self.store_name
   

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['bp_id'], name='unique_bo')
    #     ]
