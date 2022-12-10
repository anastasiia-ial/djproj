from django.db import models
from django.conf import settings
from django.utils import timezone


# class Raw (models.Model):
#     id = models.CharField(max_length=200, primary_key= True)
#     num = models.CharField(max_length=200)#артикул сырья 
#     name = models.CharField(max_length=200)#наименование
#     layer = models.CharField(max_length=200)#навзвание слоя на русском

    # def __str__(self):
    #    return self.num +' '+ self.title

# class Sku (models.Model):
#     num = models.CharField(max_length=200,primary_key=True)#артикул готоваой продукции (ГП)
#     name = models.CharField(max_length=200)#наименование ГП

# class MK (models.Model):
#     code = models.CharField(max_length=200,primary_key=True)#артикул маршрутной карты (МК)
#     name = models.CharField(max_length=200)#наименование
#     raw_num = models.ForeignKey(Raw, on_delete=models.CASCADE)#ссылка на артикул сырья
   
# class Sku_MK (models.Model):
# #     id = models.BigAutoField(primary_key=True) #номер изменения 
#     sku_num = models.ForeignKey(Sku, on_delete=models.CASCADE)
#     mk_code= models.ForeignKey(MK, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(default=timezone.now)#когда была создана

# class Change (models.Model):
#     id = models.BigAutoField(primary_key=True) #номер изменения 
#     # old_raw = models.ForeignKey(Raw, on_delete=models.CASCADE)#старый артикул сырья
#     # old_raw = models.CharField(max_length=13)#старый артикул сырья
#     new_raw = models.CharField(max_length=13)#новый артикул сырья
#     # title = models.CharField(max_length=200)#наименование
#     # rtitle = models.CharField(max_length=200)#навзвание слоя на русском
#     status = models.TextChoices('Выполнено', 'Невыполнено')#статус
#     created_date = models.DateTimeField(default=timezone.now)#когда была создана заявка

    # def __str__(self):
    #     return self.id