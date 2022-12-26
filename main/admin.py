from django.contrib import admin
from .models import *
# from .models import Sku
# from .models import Change

@admin.register(Raw,Change,Sku,ProductsTypes)
class PersonAdmin(admin.ModelAdmin):
    pass

