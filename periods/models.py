from django.db import models
from django.db import models
from base.models import University
##########الرئيسي###########
class Period(models.Model):
    PERIOD_TYPES = [
        ('monthly', 'شهري'),
        ('quarterly', 'ربع سنوي'),
        ('yearly', 'سنوي'),
    ]

    STATUS_CHOICES = [
        ('new', 'جديد'),
        ('active', 'فعال'),
        ('locked', 'مقفل'),
        ('stopped', 'موقف'),
    ]

    name = models.CharField(max_length=255, verbose_name="اسم الفترة")
    period_type = models.CharField(max_length=20, choices=PERIOD_TYPES, verbose_name="نوع الفترة")
    start_date = models.DateField(verbose_name="من تاريخ")
    end_date = models.DateField(verbose_name="إلى تاريخ")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="حالة")
    university = models.ForeignKey(University, verbose_name="الجامعة", on_delete=models.CASCADE)
    class Meta:
        verbose_name='الرئيسي'
        verbose_name_plural = 'الرئيسي'

    def __str__(self):
        return self.name

########## التفصيلي##################
class PeriodDetail(models.Model):
    period = models.ForeignKey(Period, verbose_name="الفترة", on_delete=models.CASCADE)
    period_number = models.IntegerField(verbose_name="رقم الفترة")
    name = models.CharField(max_length=255, verbose_name="اسم الفترة")
    start_date = models.DateField(verbose_name="من تاريخ")
    end_date = models.DateField(verbose_name="إلى تاريخ")
    status = models.CharField(max_length=20, choices=Period.STATUS_CHOICES, default='new', verbose_name="حالة")
    class Meta:
        verbose_name='التفصيلي'
        verbose_name_plural = 'التفصيلي'

    def __str__(self):
        return self.name
