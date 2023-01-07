from django.contrib import admin
from .models import *
# from .models import Sku
# from .models import Change

@admin.register(Raw,Change,ProductsTypes)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Sku)
class PersonAdmin(admin.ModelAdmin):
    filter_horizontal = ['raw']
