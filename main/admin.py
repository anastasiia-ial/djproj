from django.contrib import admin
from .models import Raw, Sku, Change
# from .models import Sku
# from .models import Change

@admin.register(Raw, Sku, Change)
class PersonAdmin(admin.ModelAdmin):
    pass

