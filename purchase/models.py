from django.db import models
# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel, UniversityBaseModel
class Supplier(BaseModel):
    name = models.CharField(_("الاسم"),max_length=100)
    contact_person = models.CharField(_("الشخص المتصل به"),max_length=100)
    email = models.EmailField(_("الإيميل"),)
    phone_number = models.CharField(_("رقم الهاتف"),max_length=20)
    address = models.TextField(_("العنوان"))
    class Meta:
        verbose_name=' المورد'
        verbose_name_plural =' المورد'
class AssetPurchaseRequest(UniversityBaseModel):
    STATUS_CHOICES = (
        ('Pending', 'قيد الانتظار'),
        ('Approved', 'موافق عليه'),
        ('Rejected', 'مرفوض'),
    )
    requester = models.ForeignKey('base.user',verbose_name='المطلب', on_delete=models.CASCADE)
    asset_name = models.CharField(_("اسم الأصل"),max_length=100)
    description = models.TextField(_("الوصف"))
    quantity = models.PositiveIntegerField(_("الكمية"))
    unit_price = models.DecimalField(_("سعر الوحدة"),max_digits=10, decimal_places=2)
    total_price = models.DecimalField(_("السعر الإجمالي"),max_digits=12, decimal_places=2)
    status = models.CharField(_("الحالة"),max_length=20, choices=STATUS_CHOICES, default='Pending')
    date = models.DateTimeField(_("التاريخ"))
    class Meta:
        verbose_name=' طلب شراء الأصول'
        verbose_name_plural =' طلب شراء الأصول'
    
from django.db import models

class AssetInvoice(UniversityBaseModel):
    invoice_number = models.CharField(_(" رقم الفاتورة"),max_length=100)
    asset_name = models.CharField(_(" اسم الأصل"),max_length=100)
    quantity = models.PositiveIntegerField(_(" الكمية"))
    unit_price = models.DecimalField(_(" سعر الوحدة"),max_digits=10, decimal_places=2)
    total_price = models.DecimalField(_(" السعر الإجمالي"),max_digits=12, decimal_places=2)
    supplier = models.ForeignKey('Supplier',verbose_name='المورد', on_delete=models.CASCADE)
    invoice_date = models.DateField(_(" تاريخ الفاتورة"))
    class Meta:
        verbose_name='   فاتورةشراء الأصول'
        verbose_name_plural =' فاتورة شراء الأصول '

class AssetReceipt(UniversityBaseModel):
    receipt_number = models.CharField(_(" رقم الاستلام"),max_length=100)
    asset_name = models.CharField(_(" اسم الأصل"),max_length=100)
    quantity = models.PositiveIntegerField(_(" الكمية"))
    unit_price = models.DecimalField(_(" سعر الوحدة"),max_digits=10, decimal_places=2)
    total_price = models.DecimalField(_(" السعر الإجمالي"),max_digits=12, decimal_places=2)
    supplier = models.ForeignKey('Supplier',verbose_name='المورد', on_delete=models.CASCADE)
    receipt_date = models.DateField(_("  تاريخ الاستلام"))
    class Meta:
        verbose_name='استلام الأصول'
        verbose_name_plural ='استلام'
