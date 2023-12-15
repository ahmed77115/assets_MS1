
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *
# Register your models here.
class PeriodDetailInline(admin.TabularInline): 
    model=PeriodDetail
    extra = 1
    fieldsets = [
        (_(" تفاصيل الفترة "), {
             "fields": ('period','period_number','name','start_date','end_date','status'),
            
                
        }),
     ]
TEXT='أدخل بيانات  الفترات'
class PeriodAdmin(admin.ModelAdmin):
    fieldsets = [
        (_(" بيانات الفترة "), {
            "fields": ('name', 'period_type', 'start_date', 'end_date', 'status', 'university'),
             'description':'%s'% TEXT,
            
                
        }),
     ]

    list_display = ('name', 'period_type', 'start_date', 'end_date', 'status', 'university')
    search_fields = ('name', 'period_type', 'status')
    list_filter = ('period_type', 'status', 'university')
    inlines = [PeriodDetailInline]

admin.site.register(Period, PeriodAdmin)

#admin.site.register(Period)



