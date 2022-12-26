from django.db import models
from django.conf import settings
from django.utils import timezone

# наименование типов выпускаемой продукции

class ProductsTypes (models.Model):
     name = models.CharField(max_length=200)  # наименование типов выпускаемой продукции

     def __str__(self):
        return self.name 

# Сырье

class Raw (models.Model):
    num = models.CharField(max_length=200)  # артикул сырья
    name = models.CharField(max_length=200)  # наименование
    layer = models.CharField(max_length=200)  # навзвание слоя на русском

    def __str__(self):
        return self.num +' ' + self.name

# Код ГП
class Sku (models.Model):
    
    num = models.CharField(max_length=200)  # артикул готоваой продукции (ГП)
    name = models.CharField(max_length=200)  # наименование ГП
    raw = models.ManyToManyField(Raw, blank=True, null=True)  # сырье
    weight = models.IntegerField(blank=True, null=True)  # вес
    photo = models.ImageField(blank=True, null=True,
                              upload_to="images/")  # фото
    type = models.ForeignKey(ProductsTypes, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.num + ' ' + self.name

# Изменения в сырье
class Change (models.Model):
    # number = models.CharField(max_length=200)
    raw_current = models.ForeignKey(Raw, blank=True, null=True, on_delete=models.CASCADE, related_name='raw_current')
    raw_new = models.ForeignKey(Raw, blank=True, null=True, on_delete=models.CASCADE, related_name='raw_new')
    # status = models.BooleanField()  # статус
    created_date = models.DateTimeField(default=timezone.now)  # когда была создана заявка

def __str__(self):
      return self.raw_current + 'на' + self.raw_new

def publish(self):
        self.created_date = timezone.now()
        self.save()


# Маршрутная карта

# class Mk (models.Model):
#     name = models.CharField(max_length=200)#номер маршрутной карты
#     raw_id = models.ForeignKey(Raw, blank=True, null=True) # Mk.raw_id.num
#     # raw_id = models.CharField(max_length=200)
#     def __str__(self):
#        return self.name +' '+ self.raw_id

# Соединение кода ГП и МК

# class Sku_Mk(models.Model):
#     sku_id = models.ForeignKey(Sku, blank=True, null= True)
#     mk_id = models.ForeignKey(Mk, blank=True, null=True)

#     def __str__(self):
#        return self.sku_id +' '+ self.mk_id
