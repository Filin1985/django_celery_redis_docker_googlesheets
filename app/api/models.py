from pycbrf.toolbox import ExchangeRates
from django.db import models

# Create your models here.


class Order(models.Model):
    id_num = models.IntegerField(blank=False, null=False, unique=True)
    order_num = models.CharField(
        blank=False, null=False, max_length=7)
    price_dol = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)
    price_rub = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)
    get_data = models.DateField(blank=False, null=False)
    

    