from os import name
from django.contrib import admin
from django.contrib.admin import AdminSite
from.models import Asset,AssetCategory,Location, MovementAssets
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

# Register your models here.
class CustomAdmin(AdminSite):
    site_header_icon='image/asset'
admin_site=CustomAdmin(name='admin')    

admin.site.site_header='ادارة الأصول'
admin.site.site_title='Assets Managment'
TEXT='أدخل بيانات أنواع الأصول'
class Assetcategoryadmin(admin.ModelAdmin):
     fieldsets = [
        #  (_(" بيانات الأدخال والتحديث"), {
        #     "fields": ('createdat','modifiedat','owner','modifiedby','deletedby','deletedat','deleted'),   
                
        # }),
        (_(" بيانات الفئه"), {
            "fields": ('name','description','category_admin','parent','is_group'),
            'description':'%s'% TEXT,
                
        }),
     ]
     list_display= ['name','category_admin','parent']
 
     list_filter=['name','category_admin','parent']
        

admin.site.register(AssetCategory,Assetcategoryadmin)  
###########################################
TEXT='أدخل بيانات الموقع '
class Locationadmin(admin.ModelAdmin):
    fieldsets = (
        (_(" بيانات الموقع"), {
            "fields": (
                ('name','location_type',),
                ('description','area',),
             ('parent','university',) ,
               'is_group', ),
            'description':'%s'% TEXT,   
        }),
     )  
    list_display=['name','location_type','is_group','area','parent','university']
    #list_editable=['is_group','area']
    search_fields=['name']
    list_filter=['name']



admin.site.register(Location,Locationadmin)
#########################################3
class Assetadmin(admin.ModelAdmin):
    fieldsets = (
        (_(" بيانات الأصل"), {
            'classes': ('collapse' ,),
            "fields": (
                ('barcode','name'),
                ('quantity','status'),
             ('value','activation_date'),
              ('usage_period','creation_date'),
               ('asset_admin','maintenance_required'),
               ('borrow_able',
                )
)        }),
        (_(" الموقع والجامعة "), {
            'classes': ('collapse ' ,),
            "fields": (
                ('location','university',),
               
                )
        }),
        (_(" الفئه والقسم  "), {
            'classes': ('collapse ' ,),
            "fields": (
                ('category','department',),
                )
        }),
        (_(" بيانات إضافيه"), {
            'classes': ('collapse ' ,),
            "fields": (
                ('asset_issued','asset_image',),
        
                )
        }),
     )  

    list_display=['name','quantity','status','value','activation_date','usage_period','creation_date','asset_admin',
    'maintenance_required','borrow_able']
    #list_editable=['quantity','status','value','activation_date','usage_period','creation_date','asset_admin',
    #'maintenance_required','borrow_able']
    list_filter=['name']
    search_fields=['name','quantity','borrow_able','maintenance_required']
    def save_model(self, request, obj, form, change):

        if change:
            obj.modifiedby = request.user
        else:
            obj.owner = request.user
        super().save_model(request, obj, form, change)
        # if not change:
        obj.create_asset_mov()
admin.site.register(Asset,Assetadmin) 
@admin.action(description="تطبيق الجرد")
def make_inventory(modeladmin, request, queryset):
    for obj in queryset:
        obj.create_asset_inventory()
class MovementAssetsadmin(admin.ModelAdmin):
    actions = [make_inventory]
    fieldsets = [
            (_(" بيانات الحركة للأصل"), {
                "fields": [ ('quantity','asset',),
                        'location','employee', 'company'  
                
                ]
            })
    ] 
    list_display=['quantity','count_quantity','asset','location','employee','company',]
    #list_editable=['quantity','asset','location','employee','company',]
    search_fields=['quantity','asset']
    list_filter=['asset',"location","company"]
    list_editable=["count_quantity"]
    list_display_links=[]
    def get_list_display_links(self, request, list_display):
        """
        Return a sequence containing the fields to be displayed as links
        on the changelist. The list_display parameter is the list of fields
        returned by get_list_display().
        """
        return []
admin.site.register(MovementAssets,MovementAssetsadmin)  

        
    
