from django.contrib import admin
from .models import GoogleSheetModel


class GoogleSheetModelAdmin(admin.ModelAdmin):
    list_display = ['number', 'price_usd', 'price_rub', 'delivery_date']
    list_display_links = ['number', ]
    search_fields = ['number', 'delivery_date']


admin.site.register(GoogleSheetModel, GoogleSheetModelAdmin)
