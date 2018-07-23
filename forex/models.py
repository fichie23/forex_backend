from django.db import models


class Currency(models.Model):
    base = models.CharField(max_length=3)
    target = models.CharField(max_length=3)

    class Meta:
        unique_together = ('base', 'target',)


class ExchangeRateHistory(models.Model):

    currency = models.ForeignKey(Currency)
    date = models.DateField()
    rate = models.FloatField(default=1.0)
