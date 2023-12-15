from django.contrib import admin
from.models import *
from django.utils.translation import gettext_lazy as _

# Register your models here.
class MaintenanceTeamadmin(admin.ModelAdmin):
     fieldsets = (
        (_(" بيانات فريق الصيانة"), {
            "fields": (
                ('team_name','university',),
                
                )
        }),
     )
    
     list_display=['team_name','university']
admin.site.register(MaintenanceTeam,MaintenanceTeamadmin)

class MaintenanceAssetadmin(admin.ModelAdmin):
    fieldsets = (
        (_(" بيانات  صيانة الأصول"), {
            "fields": (
                ('asset','maintenance_team',),
                 ('maintenance_manager','university',),
                
                )
        }),
     )
    list_display=['asset','maintenance_team','maintenance_manager','university']
admin.site.register(MaintenanceAsset,MaintenanceAssetadmin)
class taskadmin(admin.ModelAdmin):
    fieldsets = (
        (_(" بيانات  المهام"), {
            "fields": (
                ('name','priority',),
                 ('assigned_to','status',),
                
                )
        }),
     )
    list_display=['name','priority','assigned_to','status']
admin.site.register(Task,taskadmin)
class AssetMaintenanceLogadmin(admin.ModelAdmin):
    fieldsets = (
        (_(" بيانات  سجل الصيانة"), {
            "fields": (
                ('asset_maintenance','naming_series',),
                 ('asset_name','item_code',),
                  ('item_name','task',),
                   ('maintenance_type','periodicity',),
                    'maintenance_status',
                
                )
        }),
     )
    list_display=['asset_maintenance','naming_series','asset_name','item_code','item_name','task','maintenance_type','periodicity','maintenance_status']
admin.site.register(AssetMaintenanceLog,AssetMaintenanceLogadmin)  
class AssetRepairadmin(admin.ModelAdmin):
     fieldsets = (
        (_(" بيانات  أصلاح الأصول "), {
            "fields": (
                ('naming_series','failure_date',),
                 ('completion_date','repair_status',),
                  ('actions_performed','downtime',),
                   ('repair_cost','asset',),
                    'asset_name',
                
                )
        }),
     )
     list_display=['naming_series','failure_date','completion_date','repair_status','actions_performed','downtime','repair_cost','asset','asset_name']
admin.site.register(AssetRepair,AssetRepairadmin)
class AssetRepairConsumedItemadmin(admin.ModelAdmin):
    fieldsets = (
        (_(" بيانات   استهلاك الأصول "), {
            "fields": (
                ('valuation_rate','consumed_quantity',),
                 ('total_value','serial_no',),
                  ('item_code','asset_repair',),
                   
                
                )
        }),
     )
    
    
    list_display=['valuation_rate','consumed_quantity','total_value','serial_no','item_code','asset_repair']
admin.site.register(AssetRepairConsumedItem,AssetRepairConsumedItemadmin)    
