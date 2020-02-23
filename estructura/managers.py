from django.db import models


class ProductManager(models.Manager):

    def is_active(self):
        return self.filter(is_active=True)

    def have_stock(self):
        return self.is_active().filter(stock__gte=1)