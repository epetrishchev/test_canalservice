from typing import Optional
from django.shortcuts import render
from django.views.generic import ListView
from .services.worker import сompletely_update_db
from .models import GoogleSheetModel


class OrderListView(ListView):
    """
    OrderListView Представление главной страницы приложения
    в виде списка заказов. 
    """
    context_object_name: Optional[str] = 'order_list'
    model = GoogleSheetModel
    template: str = 'gsbase/main.html'

    def get(self, request):
        orders = self.model.objects.all()
        worker_test = 'Работает' if сompletely_update_db(
            self.model) else 'Не работает'
        context = {
            'orders': orders,
            'worker': worker_test,
        }
        return render(request, self.template, context)
