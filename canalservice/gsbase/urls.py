from django.urls import path

from .views import OrderListView


appname = 'gsbase'
urlpatterns = [
    path('', OrderListView.as_view(), name='main')
]
