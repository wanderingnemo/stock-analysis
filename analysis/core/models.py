from django.db import models

# Create your models here.
class ListedCompany(models.Model):
    name = models.CharField(max_length=1024)
    symbol = models.CharField(max_length=100)
    isin = models.CharField(max_length=100, null=True, blank=True)
    

class DailyTradeData(models.Model):
    listed_company = models.ForeignKey(ListedCompany)
    company_symbol = models.CharField(max_length=100)
    traded_date = models.DateField()
    open_value = models.DecimalField(default=0, max_digits=9,
                                     decimal_places=2, null=True)
    high_value = models.DecimalField(default=0, max_digits=9,
                                     decimal_places=2, null=True)
    low_value = models.DecimalField(default=0, max_digits=9,
                                     decimal_places=2, null=True)
    ltp_value = models.DecimalField(default=0, max_digits=9,
                                     decimal_places=2, null=True)
    close_value = models.DecimalField(default=0, max_digits=9,
                                     decimal_places=2, null=True)
    volume = models.DecimalField(default=0, max_digits=16,
                                     decimal_places=2, null=True)
    turn_over= models.DecimalField(default=0, max_digits=16,
                                     decimal_places=2, null=True)
    high_minus_low = models.DecimalField(default=0, max_digits=9,
                                     decimal_places=2, null=True)
    high_minus_open = models.DecimalField(default=0, max_digits=9,
                                     decimal_places=2, null=True)
    close_minus_open = models.DecimalField(default=0, max_digits=9,
                                     decimal_places=2, null=True)