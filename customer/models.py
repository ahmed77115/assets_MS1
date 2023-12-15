from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from base.utils import COUNTRIES
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Person(BaseModel):
    CUSTOMER_TYPE = [
        ('1',_("An individual")),
        ('2',_("a company")),
        ('3',_("Mail-man")),
        ('4',_("post-man")),
    ]
    M=(('male','ذكر'),
       ('female','أنثى')

    )

    X=(('student', 'طالب'),
        ('employee', 'موظف'),
        ('teacher', 'مدرس'),)
    Y = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    customer_number = models.IntegerField(_("رقم العميل"))
    customer_type = models.CharField(_("نوع العميل"), max_length=50,choices=CUSTOMER_TYPE)
    name = models.CharField(_("الأسم"), max_length=50)
    user_type = models.CharField(_("نوع المستخدم"),max_length=100,choices=X)
    status = models.CharField(_("حالة العميل"),max_length=100, choices=Y)
    gender = models.CharField(_("الجنس"),max_length=100,choices=M)
    #phone_number = models.CharField(_("رقم التلفون"),max_length=100,blank=True, null=True)
    #user_email = models.EmailField(_("الأيميل"), max_length=245 ,blank=True, null=True)
    date_joined = models.DateTimeField(_('تاريخ الربط'), default=timezone.now)
    stop = models.BooleanField(_("موقف"),default=False)
    reason = models.CharField(_("السبب"), max_length=200,blank=True, null=True)
    identity_type = models.CharField(_("نوع الهوية"), max_length=50,blank=True, null=True)
    identification_number = models.IntegerField(_("رقم الهوية"),blank=True, null=True)
    issuer = models.CharField(_("جهة الأصدار"), max_length=50,blank=True, null=True)
    release_date = models.DateField(_("تاريخ الأصدار"), auto_now=False, auto_now_add=False,blank=True, null=True)
    expiry_date = models.DateField(_("تاريخ الأنتهاء"), auto_now=False, auto_now_add=False,blank=True, null=True)
    join_date = models.DateField()
    university = models.ForeignKey('base.University',verbose_name=_("الجامعة"), on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey('base.Department',verbose_name=_("القسم"), on_delete=models.CASCADE)
    user =models.ForeignKey('base.User', verbose_name=_("المستخدم"), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_partner_linked" ,null=True,blank=True)

    class Meta:
        abstract = True
        verbose_name = ' بيانات العميل'
        verbose_name_plural = ' بيانات العملاء'
    
    def __str__(self):
        return self.name

class Partner(Person):
    pass

class PartnerAddress(BaseModel):
    partner = models.ForeignKey(Partner, verbose_name=_("العميل"), on_delete=models.CASCADE)
   # address = models.ForeignKey("base.Address", verbose_name=_("العنوان"), on_delete=models.CASCADE)
    type_address = models.CharField(_("نوع العنوان"), max_length=50)
    # phone = models.CharField(_("phone"), max_length=50)
    note = models.CharField(_("ملاحظة"), max_length=50,  blank=True, null=True)
    class Meta:
     verbose_name = ' عنوان العميل'
    verbose_name_plural = 'عنوان العميل' 
    
    

    def __str__(self):
        return str(self.partner)