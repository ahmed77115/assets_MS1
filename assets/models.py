from tkinter import S
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel,TreeForeignKey
from base.models import BaseMPTTModel, BaseModel, Department, University
# Create your models here.
# أنواع الأصـــــــــــــــول
class AssetCategory(BaseMPTTModel):
    name = models.CharField(_("الاسم"),max_length=100,null=False,blank=False)
    description = models.CharField(_("الوصف"),max_length=100,null=False,blank=False)
    category_admin = models.CharField(_("مسؤول الأصول "),max_length=100,null=False,blank=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_group = models.BooleanField(_("مجموعة"),default=False)
    class Meta:
        verbose_name='فئات الأصول'
        verbose_name_plural = 'فئات الأصول'
    def __str__(self):
     return self.name        

class Location(BaseMPTTModel):
    MOVEMENT_TYPE=(
        ('1','داخلي'),
        ('2','عملاء'),
        ('3','نقل'),
        ('4','تالف \خساره'),
        ('5','موردين'),
        ('6','صيانه'),
        ('7','الافتتاحي'),
    
    )
    name = models.CharField(_("الاسم"),max_length=100,null=False,blank=False)
    location_type = models.CharField(_("نوع الموقع"),choices=MOVEMENT_TYPE,max_length=100,null=False,blank=False,help_text='هذا يكون أختيار نوع الموقع ')
    description = models.CharField(_("الوصف"),max_length=100,null=False,blank=False)
    is_group = models.BooleanField(_("مجموعة"),default=False)
    area = models.CharField(_("المساحة "),max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    university = models.ForeignKey('base.University',verbose_name = _("الجامعة"), on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name='المواقع'
        verbose_name_plural = 'المواقع'
    def __str__(self):
        return self.name    
#الأقســـــــــــــــــــام


# الأصـــــــــــــــــــــول
class Asset(models.Model):
    status=(
        ('1','فعال'),
        ('2','غير فعال'),
        ('3','موقف'),
        ('4','مستبعد')
    )
    barcode = models.IntegerField(_("رقم الباركود"),null=True,blank=True)
    name = models.CharField(_("الاسم"),max_length=100,null=True,blank=True)
    quantity = models.IntegerField(_("الكمية"))
    status = models.CharField(_("الحالة"),max_length=100,choices=status)
    value = models.DecimalField(_("القيمة"),max_digits=10, decimal_places=2)
    activation_date = models.DateField(_("تاريخ التفعيل"),null=True,blank=True)
    usage_period = models.DateField(_("فترة الأستخدام"),null=True,blank=True)
    creation_date = models.DateField(_("تاريخ الاضافة"),null=True,blank=True)
    asset_admin = models.CharField(_("مسؤول الأصل"),max_length=100,null=True,blank=True)
    maintenance_required = models.BooleanField(_("الصيانة مطلوبة"))
    borrow_able = models.BooleanField(_("جاهزللأعارة"))
    location = models.ForeignKey(Location,verbose_name = _("الموقع"), on_delete=models.CASCADE)
    university = models.ForeignKey(University,verbose_name = _("الجامعة"), on_delete=models.CASCADE)
    category = models.ForeignKey(AssetCategory,verbose_name = _("نوع الأصل"), on_delete=models.CASCADE)
    department = models.ForeignKey(Department,verbose_name = _("القسم"), on_delete=models.CASCADE)
    asset_issued = models.BooleanField(default=False)
    employee = models.ForeignKey('customer.Partner',verbose_name = _("الموظف"), on_delete=models.SET_NULL, null=True, blank=True)
    asset_image = models.ImageField(_("الصورة"),default="default.jpeg", upload_to = 'images/')
    class Meta:
        verbose_name='الأصول'
        verbose_name_plural ='الأصول'
    def __str__(self):
        return self.name
    
    def create_asset_mov(self):
        from movement.models import Movement
        if Movement.objects.filter(asset=self).exists():
            return
        from datetime import date
        from movement.models import Movement,MovementType
        Movement.objects.create(
            purpose="اضافة اصل",
            transaction_date=date.today() ,
            reference_name="001",
            asset=self,
            source_location=Location.objects.filter(location_type='7').first(),
            target_location=self.location,
            from_employee=None,
            to_employee=self.employee,
            from_company=self.university,
            to_company=self.university,
            university=self.university,
            type_movement=MovementType.objects.filter(type='1').first(),
            quantity=self.quantity,
            status='',
        )
        obj1,created =MovementAssets.objects.get_or_create(
      defaults={
            "asset": self ,
            "location": Location.objects.filter(location_type='7').first() ,
            "employee": self.employee ,
            "company": self.university ,
            },
            quantity = -self.quantity ,
            status = self.status , 
        )
        if not created:
            obj1.location = Location.objects.filter(location_type='7').first()
            obj1.employee = self.employee
            obj1.company = self.university
            obj1.quantity = -self.quantity
            obj1.status = self.status
            obj1.save()
        obj2,created=MovementAssets.objects.get_or_create(
            defaults={
            "asset": self ,
            "location": self.location ,
            "employee": self.employee ,
            "company": self.university ,
            },
            quantity =self.quantity ,
            status = self.status , 
        )
        if not created:
            obj2.location = self.location
            obj2.employee = self.employee
            obj2.company = self.university
            obj2.quantity = self.quantity
            obj2.status = self.status
            obj2.save()
        
class MovementAssets(BaseModel):
    quantity = models.IntegerField(_("الكمية"))
    count_quantity = models.IntegerField(_("الكمية المحسوبة"),null=True,blank=True)
    asset = models.ForeignKey('Asset',verbose_name = _("الأصل"), on_delete=models.CASCADE)
    location = models.ForeignKey('Location',verbose_name = _("الموقع"),null=True,blank=True, on_delete=models.CASCADE, related_name='movement_lines_as_source_mov')
    employee = models.ForeignKey('customer.Partner',verbose_name = _("العميل"), on_delete=models.SET_NULL, null=True, blank=True, related_name='movement_lines_as_from_employee_mov')
    company = models.ForeignKey('base.University',verbose_name = _("الجامعة"), on_delete=models.CASCADE,null=True, blank=True, related_name='movement_lines_as_from_company_mov')
    statusch=(
        ('in','in'),
        ('out','out'),
        ('non','in')
    )
    status = models.CharField(_("الحالة"),max_length=100,choices=statusch)
    class Meta:
        verbose_name='حركة الأصل'
        verbose_name_plural = 'حركة الأصل'
        
    def create_asset_inventory(self):
        from datetime import date
        from movement.models import Movement,MovementType
        if  self.count_quantity and self.quantity and self.count_quantity-self.quantity >0:
            Movement.objects.create(
            purpose="تسوية الجرد",
            transaction_date=date.today() ,
            reference_name="001",
            asset=self.asset,
            source_location=self.location,
            target_location=Location.objects.filter(location_type='4').first(),
            from_employee=self.employee,
            to_employee=None,
            from_company=self.company,
            to_company=self.company,
            type_movement=MovementType.objects.filter(type='7').first(),
            quantity=self.count_quantity-self.quantity,
            status='',
        )
        elif  self.count_quantity and self.quantity and self.count_quantity-self.quantity <0:
            Movement.objects.create(
            purpose="تسوية الجرد",
            transaction_date=date.today() ,
            reference_name="001",
            asset=self.asset,
            target_location=self.location,
            source_location=Location.objects.filter(location_type='4').first(),
            from_employee=None,
            to_employee=self.employee,
            from_company=self.company,
            to_company=self.company,
            type_movement=MovementType.objects.filter(type='7').first(),
            quantity=abs(self.count_quantity-self.quantity),
            status='',
        )
        elif  self.count_quantity and self.quantity and self.count_quantity-self.quantity ==0:
            self.count_quantity=None
            self.save()
            return
        elif self.count_quantity is None:
            return
       
        obj1,created =MovementAssets.objects.get_or_create(
      defaults={
            "quantity":self.count_quantity-self.quantity ,
            "status":self.status , },
      **{
            "asset": self.asset ,
            "location": Location.objects.filter(location_type='4').first() ,
            "employee": self.employee ,
            "company": self.company ,
            },
        )
        if not created:
            obj1.location = Location.objects.filter(location_type='4').first()
            obj1.employee = self.employee
            obj1.company = self.company
            obj1.quantity = self.count_quantity-self.quantity
            obj1.status = self.status
            obj1.save()

        
        # obj2.location = self.location
        # obj2.employee = self.employee
        # obj2.company = self.university
        self.quantity = self.count_quantity
        self.count_quantity = None
        self.save()
        
        
    def __str__(self):
        return f"كمية:{self.quantity} -أصل:{self.asset} -موقع: {self.location} -موظف:{self.employee} - جامعة:{self.company} - الحالة:{self.status}"