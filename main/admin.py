from django.contrib import admin
from .models import Raw, Change
# from .models import Sku
# from .models import Routing
from .models import Change

@admin.register(Raw, Change)
class PersonAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Sku)
# admin.site.register(Routing)