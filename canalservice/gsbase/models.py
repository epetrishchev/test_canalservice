from django.db import models


class GoogleSheetModel(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField('Номер заказа')
    price_usd = models.DecimalField(
        'Стоимость,$',
        decimal_places=3,
        max_digits=12
    )
    price_rub = models.DecimalField(
        'Стоимость в руб.',
        decimal_places=3,
        max_digits=12)
    delivery_date = models.DateField('Срок поставки')

    class Meta:
        verbose_name_plural = 'База заказов'
        verbose_name = 'База заказов'
        ordering = ['number']
