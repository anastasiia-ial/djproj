from django.db import models
from django.conf import settings
from django.utils import timezone


class Raw (models.Model):
    num = models.CharField(max_length=200)#артикул сырья
    list = models.CharField(max_length=200)#наименование
    layer = models.CharField(max_length=200)#навзвание слоя на русском

    def __str__(self):
       return self.num +' '+ self.title

# class Sku (models.Model):
#     num = models.CharField( on_delete=models.CASCADE)#артикул готоваой продукции (ГП)
#     title = models.CharField(max_length=200)#наименование ГП

# class Routing (models.Model):
#     code = models.CharField(on_delete=models.CASCADE)#артикул маршрутной карты (МК)
#     sku_num = models.ForeignKey(max_length=3)#ссылка на артикул ГП
    # sku_title = models.CharField(max_length=3)#ссылка на наименование ГП
#     raw_num = models.CharField(max_length=3)#ссылка на артикул сырья
#     raw_title = models.CharField(max_length=3)#ссылка на наименование сырья
   

# class Raw (models.Model):
#     number = models.CharField(max_length=200)#артикул сырья
#     list = models.CharField(max_length=200)#наименование
#     layer = models.CharField(max_length=200)#навзвание слоя на русском

#     def __str__(self):
#        return self.num +' '+ self.title
# class Change (models.Model):
   
#     # id = models.BigAutoField(primary_key=True) #номер изменения 
#     # old_raw = models.ForeignKey(Raw, on_delete=models.CASCADE)#старый артикул сырья
#     # old_raw = models.CharField(max_length=13)#старый артикул сырья
#     new_raw = models.CharField(max_length=13)#новый артикул сырья
#     # title = models.CharField(max_length=200)#наименование
#     # rtitle = models.CharField(max_length=200)#навзвание слоя на русском
#     status = models.BooleanField()#статус
#     created_date = models.DateTimeField(default=timezone.now)#когда была создана заявка

#     # def __str__(self):
#     #     return self.id