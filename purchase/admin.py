from django.contrib import admin
from.models import *
from django.utils.translation import gettext_lazy as _
  
# Register your models here.
class Supplieradmin(admin.ModelAdmin):
    fieldsets = (
        (_("  بيانات المورد"), {
            "fields": (
                ('name','contact_person',),
                ('email','address',),
                
                )
        }),
     )

    list_display=['name','contact_person','email','address']
admin.site.register(Supplier,Supplieradmin) 
class AssetPurchaseRequestadmin(admin.ModelAdmin):
    fieldsets = (
        (_(" بيانات شراء الأصول"), {
            "fields": (
                ('requester','asset_name',),
                ('quantity','unit_price',),
                ('total_price','status',),
                'date',
                )
        }),
     )

    list_display=['requester','asset_name', 'quantity','unit_price','total_price','status','date'] 
admin.site.register(AssetPurchaseRequest,AssetPurchaseRequestadmin) 
class AssetInvoiceadmin(admin.ModelAdmin):
    fieldsets = (
        (_(" بيانات فاتورة الشراء"), {
            "fields": (
                ('invoice_number','asset_name',),
                ('quantity','unit_price',),
                ('total_price','supplier',),
                'invoice_date',
                )
        }),
     )

    list_display=['invoice_number','asset_name','quantity','unit_price','total_price','supplier','invoice_date']
admin.site.register(AssetInvoice,AssetInvoiceadmin)
class AssetReceiptadmin(admin.ModelAdmin):
     fieldsets = (
        (_(" بيانات استلام الأصول"), {
            "fields": (
                ('receipt_number','asset_name',),
                ('quantity','unit_price',),
                ('total_price','supplier',),
                'receipt_date',
                )
        }),
     )
    
list_display=['receipt_number','asset_name','quantity','unit_price','total_price','supplier','receipt_date'] 
admin.site.register(AssetReceipt,AssetReceiptadmin)       
     
