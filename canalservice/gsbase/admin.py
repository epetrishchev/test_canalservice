from django.contrib import admin
from .models import GoogleSheetModel


class GoogleSheetModelAdmin(admin.ModelAdmin):
    list_display = ['order', 'price_usd', 'price_rub', 'delivery_date']
    list_display_links = ['order', ]
    search_fields = ['order', 'delivery_date']


admin.site.register(GoogleSheetModel, GoogleSheetModelAdmin)
