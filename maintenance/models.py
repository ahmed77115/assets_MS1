from tabnanny import verbose
from django.db import models
from assets.models import Asset
from base.models import BaseModel, UniversityBaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

class MaintenanceTeam(UniversityBaseModel):
    team_name = models.CharField(_("اسم الفريق"),max_length=100)
    class Meta:
        verbose_name='فريق الصيانة'
        verbose_name_plural ='فريق الصيانة'

  


class MaintenanceMember(BaseModel):
    maintenance_team = models.ForeignKey('MaintenanceTeam', on_delete=models.CASCADE)
    team_member = models.ForeignKey('base.User', on_delete=models.CASCADE)

class MaintenanceAsset(UniversityBaseModel):
    asset = models.CharField(_("الأصل"),max_length=100)
    asset = models.ForeignKey('assets.Asset',verbose_name = _("الأصل"),on_delete=models.CASCADE)
    maintenance_team = models.ForeignKey('MaintenanceTeam',verbose_name = _("فريق الصيانة"), on_delete=models.CASCADE)
    maintenance_manager = models.ForeignKey('base.User',verbose_name = _("مدير الصيانة"), on_delete=models.CASCADE)
    class Meta:
        verbose_name='صيانة الأصول'
        verbose_name_plural ='صيانة الأصول'

  

from django.db import models

from django.db import models

class Task(BaseModel):
    STATUS_CHOICES = (
        ('Pending', 'قيد الانتظار'),
        ('In Progress', ' في تقدم'),
        ('Completed', 'جاهز'),
        ('Cancelled', 'ملغي'),
    )
    name = models.CharField(_("الاسم"),max_length=100)
    description = models.TextField(_("الوصف"))
    priority = models.IntegerField(_("الأولويه "))
    assigned_to = models.ForeignKey('base.User',verbose_name = _("تعيين لـ"), on_delete=models.CASCADE)
    status = models.CharField(_("الحالة "),max_length=20, choices=STATUS_CHOICES, default='Pending')
    class Meta:
        verbose_name='المهام'
        verbose_name_plural ='المهام'


class AssetMaintenanceLog(BaseModel):
    MAINTENANCE_TYPE_CHOICES = (
        ('Preventive', 'Preventive'),
        ('Corrective', 'Corrective'),
        ('Predictive', 'Predictive'),
    )

    MAINTENANCE_STATUS_CHOICES = (
        ('Pending', 'قيد الانتظار'),
        ('In Progress', ' في تقدم'),
        ('Completed', 'جاهز'),
        ('Cancelled', 'ملغي'),
    )

    asset_maintenance = models.ForeignKey('MaintenanceAsset',verbose_name = _("أصل"), on_delete=models.CASCADE)
    naming_series = models.CharField(_("الاسم"),max_length=100)
    asset_name = models.CharField(_("اسم الأصل"),max_length=100)
    item_code = models.CharField(_("الغرض"),max_length=100)
    item_name = models.CharField(_("اسم العصر"),max_length=100)
    task = models.ForeignKey('Task',verbose_name = _("المهمه"), on_delete=models.CASCADE)
    maintenance_type = models.CharField(_("نوع الصيانة"),max_length=20, choices=MAINTENANCE_TYPE_CHOICES)
    periodicity = models.CharField(_("دوريه"),max_length=100)
    assign_to_name = models.CharField(_("تعيين"),max_length=100)
    due_date = models.DateField(_("تاريخ"))
    completion_date = models.DateField(_("تاريخ الأنتهاء"),null=True, blank=True)
    maintenance_status = models.CharField(_("حالةالصيانة"),max_length=20, choices=MAINTENANCE_STATUS_CHOICES, default='Pending')
    has_certificate = models.BooleanField(_("لديه شهادة"),default=False)
    certificate_attachment = models.FileField(_("شهادة"),upload_to='certificates/', null=True, blank=True)
    description = models.TextField(_("الوصف"))
    actions_performed = models.TextField(_("الإجراءت المنفذه"))
    amended_from = models.ForeignKey('self',verbose_name = _("تم التعديل"), on_delete=models.SET_NULL, null=True, blank=True)
    task_name = models.CharField(_("اسم المهمه"),max_length=100)
    class Meta:
        verbose_name='سجل الصيانة'
        verbose_name_plural ='سجل الصيانة'


    
from django.db import models

class AssetRepair(UniversityBaseModel):
    REPAIR_STATUS_CHOICES = (
        ('Pending', 'قيد الانتظار'),
        ('In Progress', 'في تقدم '),
        ('Completed', 'جاهز'),
        ('Cancelled', 'ملغي'),
    )

    naming_series = models.CharField(max_length=100)
    failure_date = models.DateField(_("تاريخ الإعطال"))
    completion_date = models.DateField(_("تاريخ أنتهاء الإصلاح"),null=True, blank=True)
    repair_status = models.CharField(_("حالة الإصلاح"),max_length=20, choices=REPAIR_STATUS_CHOICES, default='Pending')
    description = models.TextField(_("الوصف"))
    actions_performed = models.TextField(_("الإجراءات المنفذه"))
    downtime = models.DecimalField(_("مقدار الوقت"),max_digits=10, decimal_places=2)
    repair_cost = models.DecimalField(_("تكلفة الإصلاح"),max_digits=10, decimal_places=2)
    asset = models.ForeignKey('assets.Asset',verbose_name = _("أصل"), on_delete=models.CASCADE)
    asset_name = models.CharField(_("اسم الأصل"),max_length=100)
    class Meta:
        verbose_name=' إصلاح الأصول'
        verbose_name_plural =' إصلاح الأصول'

    # capitalize_repair_cost = models.BooleanField(default=False)
    # cost_center = models.ForeignKey('CostCenter', on_delete=models.SET_NULL, null=True, blank=True)
    # project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True)
    # stock_consumption = models.BooleanField(default=False)
    # total_repair_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # warehouse = models.ForeignKey('Warehouse', on_delete=models.SET_NULL, null=True, blank=True)
    # increase_in_asset_life = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # purchase_invoice = models.ForeignKey('PurchaseInvoice', on_delete=models.SET_NULL, null=True, blank=True)
    # company = models.ForeignKey('Company', on_delete=models.CASCADE)
    # stock_entry = models.ForeignKey('StockEntry', on_delete=models.SET_NULL, null=True, blank=True)

class AssetRepairConsumedItem(BaseModel):
    valuation_rate = models.DecimalField(_(" قيمة العنصر المستهلك"),max_digits=10, decimal_places=2)
    consumed_quantity = models.DecimalField(_("كمية العنصر المستهلك "),max_digits=10, decimal_places=2)
    total_value = models.DecimalField(_("القيمة الإجمالية "),max_digits=10, decimal_places=2)
    serial_no = models.CharField(_(" الرقم التسلسلي"),max_length=100)
    item_code = models.CharField(_(" رمز العنصر"),max_length=100)
    asset_repair = models.ForeignKey('AssetRepair',verbose_name = _("الأصل المستهلك"), on_delete=models.CASCADE)
    class Meta:
        verbose_name='إستهلاك الأصول'
        verbose_name_plural ='إستهلاك الأصول'

