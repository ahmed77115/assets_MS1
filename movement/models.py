from django.db import models
# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel, UniversityBaseModel
class MovementType(BaseModel):
    MOVEMENT_TYPE=(
        ('1','أضافة'),
        ('2','أستعارة'),
        ('3','نقل'),
        ('4','صيانة'),
        ('5','شراء '),
        ('6','بيع'),
    
    )
    name = models.CharField(_("الاسم"),max_length=100)
    type = models.CharField(_("نوع الحركة"),max_length=100,choices=MOVEMENT_TYPE)
    source_location = models.ForeignKey('assets.Location',null=True,blank=True,verbose_name = _("موقع المصدر"), on_delete=models.CASCADE, related_name='movement_lines_as_sourcedef')
    target_location = models.ForeignKey('assets.Location',null=True,blank=True,verbose_name = _("موقع الهدف "), on_delete=models.CASCADE, related_name='movement_lines_as_targetdef')
    class Meta:
        verbose_name=' نوع الحركة'
        verbose_name_plural =' نوع الحركة'
    def __str__(self):
        return str(self.type)  


class Movement(UniversityBaseModel):
    purpose = models.CharField(_("الغرض"),max_length=100)
    transaction_date = models.DateField(_("تاريخ الحركة"),null=True,blank=True)
    reference_name = models.CharField(_("اسم الحركة"),max_length=100)
    asset = models.ForeignKey('assets.Asset',verbose_name = _("الأصل"),on_delete=models.CASCADE)
    source_location = models.ForeignKey('assets.Location',verbose_name = _("موقع المصدر"), on_delete=models.CASCADE, related_name='movement_lines_as_source')
    target_location = models.ForeignKey('assets.Location',verbose_name = _("موقع الهدف "), on_delete=models.CASCADE, related_name='movement_lines_as_target')
    from_employee = models.ForeignKey('customer.Partner',verbose_name = _("من العميل"), on_delete=models.SET_NULL, null=True, blank=True, related_name='movement_lines_as_from_employee')
    to_employee = models.ForeignKey('customer.Partner', verbose_name = _("إلى العميل"),on_delete=models.SET_NULL, null=True, blank=True, related_name='movement_lines_as_to_employee')
    from_company = models.ForeignKey('base.University',verbose_name = _(" الجامعة المرسله"), on_delete=models.CASCADE,null=True, blank=True, related_name='movement_lines_as_from_company')
    to_company = models.ForeignKey('base.University', verbose_name = _("  الجامعة المستلمة"),on_delete=models.CASCADE,null=True, blank=True, related_name='movement_lines_as_to_company')
    type_movement = models.ForeignKey('MovementType', verbose_name = _(" نوع الحركة"),on_delete=models.CASCADE,null=True, blank=True, related_name='movement_lines_as_to_company')
    
    statusch=(
        ('in','in'),
        ('out','out'),
        ('non','in')
    )
    status = models.CharField(_("الحالة"),max_length=100,choices=statusch)
    quantity = models.IntegerField(_("الكمية"))
    class Meta:
        verbose_name=' الحركة'
        verbose_name_plural =' الحركة'
    # def __str__(self):
    #     return self.asset  
        
    def create_asset_mov(self):
        from assets.models import MovementAssets

        obj1,created =MovementAssets.objects.get_or_create(
            **{
            "asset": self.asset ,
            "location":self.source_location ,
            "employee": self.from_employee ,
            "company": self.from_company ,
            },
            defaults={"quantity":(-(self.quantity))} ,
            # status = self.status , 
        )
        if not created:
            obj1.location = self.source_location
            obj1.employee = self.from_employee
            obj1.company = self.from_company
            obj1.quantity -= self.quantity
            # obj1.status = self.status
            obj1.save()
        obj2,created=MovementAssets.objects.get_or_create(
            **{
            "asset": self.asset ,
            "location": self.target_location ,
            "employee": self.to_employee ,
            "company": self.to_company ,
            },
            defaults={"quantity":self.quantity}
            # status = self.status , 
        )
        if not created:
            obj2.location = self.target_location
            obj2.employee = self.to_employee
            obj2.company = self.to_company
            obj2.quantity += self.quantity
            obj2.status = self.status
            obj2.save()

class maindata(models.Model):
    LNVENTORY_METHODS=(
        ('1', 'إنزال آلي للأصول'),
        ('2', 'إدخال يدوي للأصول'),
        ('3', 'جرد الأصول غير المجرودة'),
    )
    year=models.IntegerField(_("السنة"))
    period = models.ForeignKey('periods.Period', verbose_name=_("الفترة"), on_delete=models.CASCADE)
    University = models.ForeignKey('base.University',verbose_name = _(" الجامعة "), on_delete=models.CASCADE,null=True, blank=True)
    lnventory_methods=models.CharField(_("طريقة الجرد"),max_length=100,choices=LNVENTORY_METHODS)
    class Meta:
        verbose_name = _(" البيانات الرئيسية")
        verbose_name_plural = _(" جرد الأصول")


class  StockDetails(BaseModel):
    status_choices = (
        ('مفقود', 'مفقود'),
        ('موجود', 'موجود'),
        ('منقول', 'منقول'),
    )
    year=models.ForeignKey('maindata',verbose_name=_("السنة"), on_delete=models.CASCADE)
    barcode = models.IntegerField(_("رقم الباركود"),null=True,blank=True)
    asset = models.ForeignKey('assets.Asset', verbose_name=_("الأصل"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("الكمية"))
    actual_quantity=models.IntegerField(_("كمية الجرد (الفعلية)"))
    status = models.CharField(_("حالة الجرد"), max_length=100, choices=status_choices)
    location = models.ForeignKey('assets.Location', verbose_name=_("الموقع"), on_delete=models.CASCADE,related_name="stockdetails_location")
    recipient=models.CharField(_("المستلم "),max_length=100)
    new_location = models.ForeignKey('assets.Location', verbose_name=_("الموقع الجديد"), on_delete=models.CASCADE,related_name="stockdetails_new_location")
    new_recipient=models.CharField(_("المستلم الجديد"),max_length=100)
    class Meta:
        verbose_name = _(" البيانات التفصيلية")
        verbose_name_plural = _("البيانات التفصيلية  ")
    def __str__(self):
        return f"{self.asset} - {self.period} - {self.location} - {self.date}"

