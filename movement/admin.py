from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _
# Register your models here.
###########################################
class MovementAdminOperation(admin.ModelAdmin):
    fieldsets = (
        (_(" بيانات الموقع"), {
            "fields": (
            "quantity",
            "asset",
            "source_location",
            "target_location",
            "from_employee",
            "to_employee",
            "from_company",
            "to_company",
            "status",
            "transaction_date",
            "type_movement",
            "purpose",
            "reference_name",
            "university",
                )
        }),
     )  
    list_display=[ "quantity", "asset", "source_location","target_location","from_employee","to_employee",
            "from_company",
            "to_company",
            "status",
            "transaction_date",
            "type_movement",
            "purpose",
            "reference_name",]
    search_fields=['quantity','asset','source_location','type_movement']
    list_filter=['asset']
    def save_model(self, request, obj, form, change):

        if change:
            obj.modifiedby = request.user
        else:
            obj.owner = request.user
        super().save_model(request, obj, form, change)
        # if not change:
        obj.create_asset_mov()
admin.site.register(Movement,MovementAdminOperation)
class MovementTypadmin(admin.ModelAdmin):
    fieldsets = (
        (_("بيانات نوع الحركة "), {
            "fields": (
                ('name','type',),
                 ('source_location','target_location',),
                )
        }),
     )
    list_display=['name','type','source_location','target_location']
admin.site.register(MovementType,MovementTypadmin) 

class StockDetailsinlines(admin.TabularInline):
     model=StockDetails
     extra=1
     fieldsets = (
        (_("بيانات  تفاصيل الجرد "), {
            "fields": 
                ('asset','barcode','status',),    
        }),
        (_("  المواقع "), {
            "fields": ('location','recipient','new_location','new_recipient'),          
        }),
        (_("  الكميات "), {
            "fields": ('quantity','actual_quantity'),          
        }),
                
     )
list_display = ('asset','location', 'quantity', 'new_location', 'status','actual_quantit')
search_fields = ('asset__name', 'location__name', 'new_location__name','actual_quantit_name')
list_filter = ('status',)
class Maindataadmin(admin.ModelAdmin):
     fieldsets = (
        (_("بيانات الجرد الرئيسية    "), {
            "fields": 
                ('year','period','University','lnventory_methods'),    
        }),
     )
     inlines=[StockDetailsinlines] 
admin.site.register(maindata,Maindataadmin)    


