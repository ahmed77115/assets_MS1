


from dis import _format_code_info
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.contrib.auth.models import AbstractUser,UserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from mptt.models import MPTTModel,TreeForeignKey
from .utils import COUNTRIES
from django.utils import timezone
class MyUserManger(UserManager):
    def get_queryset(self,user=None):
        if user:
            if user.is_superuser:
                return super(MyUserManger, self).get_queryset()
            # if user.user_office:
            #     return user.user_office.office_user.all()
            #     # return super(MyUserManger, self).get_queryset().filter(user_office=user.user_office)
            elif user.type_user == '1':
                return super(MyUserManger, self).get_queryset().filter(type_user='1')
        return super(MyUserManger, self).get_queryset()


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
   
    createdat = models.DateField(_("تاريخ الأنشاء"), auto_now=True, auto_now_add=False)
    modifiedat =  models.DateField(_("تاريخ التعديل"), auto_now=True, auto_now_add=False)
    owner = models.ForeignKey('base.User',verbose_name=_("انشائه "),blank=True, null=True, on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_ownership")
    modifiedby =models.ForeignKey('base.User', verbose_name=_("حذفه "), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_modifiedby_set" ,null=True,blank=True)
    deletedby = models.ForeignKey('base.User', verbose_name=_("عدله "), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_deletedby_set" ,null=True,blank=True)
    deletedat  = models.DateField(_("تاريخ الحذف"), auto_now=True, auto_now_add=False)
    deleted = models.BooleanField(_("هل محذوف"),blank=True, null=True)
   # phone = PhoneNumberField(_("رقم التلفون"),blank=True, null=True)
    is_manager = models.BooleanField(_(" هل مدير"),default=False)
    university = models.ForeignKey("base.University",verbose_name=_( "الجامعة" ),on_delete=models.CASCADE,null=True,blank=True)
    objects = MyUserManger()
    bobjects = models.Manager()
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        default_manager_name = 'objects'


    def get_ower_user(self):
        if self.is_superuser:
            return User._default_manager.values_list('id', flat=True)
        elif not self.is_manager:
            return User._default_manager.values_list('id', flat=True).filter(pk=self.pk)
        elif self.type_user == '1':
            return User._default_manager.filter(type_user='1').values_list('id', flat=True)
        else:
            # return objects.filter(content_type=self.content_type,object_id=self.object_id)
            return self.user_office.office_user.values_list('id', flat=True)





class MyBaseManager(models.Manager):
    def get_queryset(self,user=None):
        return super(MyBaseManager, self).get_queryset()

    def get_next_number(self,user=None,field=None):
        
    
            
        if field:

            max_number = self.get_queryset(user).filter().aggregate(models.Max(field)) # {'rating__max': 5}  ,
            print('max_number in manger')
            print(max_number[field+'__max'])
            if max_number[field+'__max']:
                return int(max_number[field+'__max'])+1
            else:
                return 1
        else:
            max_number = self.get_queryset(user).filter().aggregate(models.Max('number')) # {'rating__max': 5}  ,
            print('max_number in manger')
            print(max_number['number__max'])
            if max_number['number__max']:
                return int(max_number['number__max'])+1
            else:
                return 1

class BaseModel(models.Model):
    createdat = models.DateField(_("تاريخ الانشاء"), auto_now=True, auto_now_add=False)
    modifiedat =  models.DateField(_("تاريخ التعديل"), auto_now=True, auto_now_add=False)
    owner = models.ForeignKey(User, verbose_name=_("انشائه "), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_ownership",null=True,blank=True)
    modifiedby =models.ForeignKey(User, verbose_name=_("عدله "), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_modifiedby_set" ,null=True,blank=True)
    deletedby = models.ForeignKey(User, verbose_name=_("حذفه "), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_deletedby_set" ,null=True,blank=True)
    deletedat  = models.DateField(_("تاريخ الحذف"), auto_now=True, auto_now_add=False)
    deleted = models.BooleanField(_("هل حذف"),default=False)
    # objects = models.Manager()
    # yobjects = MyBaseManager()
    objects = MyBaseManager()
    bobjects = models.Manager()

    class Meta:
        default_manager_name = 'objects'
        abstract = True
class BaseMPTTModel(MPTTModel):
    createdat = models.DateField(_("تاريخ الأنشاء"), auto_now=True, auto_now_add=False)
    modifiedat =  models.DateField(_("تاريخ التعديل"), auto_now=True, auto_now_add=False)
    owner = models.ForeignKey(User, verbose_name=_("انشائه"), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_ownership",null=True,blank=True)
    modifiedby =models.ForeignKey(User, verbose_name=_("حذف"), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_modifiedby_set" ,null=True,blank=True)
    deletedby = models.ForeignKey(User, verbose_name=_("عدله"), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_deletedby_set" ,null=True,blank=True)
    deletedat  = models.DateField(_("تاريخ الحذف"), auto_now=True, auto_now_add=False)
    deleted = models.BooleanField(_("هل محذوف"),default=False)
    # objects = models.Manager()
    # yobjects = MyBaseManager()
    objects = MyBaseManager()
    bobjects = models.Manager()

    class Meta:
        default_manager_name = 'objects'
        abstract = True

class Address(BaseModel):
    address_line = models.CharField(_("العنوان"), max_length=255, blank=True, null=True)
    street = models.CharField(_("الشارع"), max_length=55, blank=True, null=True)
    city = models.CharField(_("المدينة"), max_length=255, blank=True, null=True)
    state = models.CharField(_("المنطقة"), max_length=255, blank=True, null=True)
    postcode = models.CharField(
        _("Post/Zip-code"), max_length=64, blank=True, null=True
    )
    country = models.CharField(_("الدولة"),max_length=3, choices=COUNTRIES, blank=True, null=True)
    location = models.CharField(_("الموقع"), max_length=50)
    class Meta:
        verbose_name='العنوان'
        verbose_name_plural = 'العنوان'


    def __str__(self):
        return self.get_complete_address()
        # return self.city if self.city else ""

    def get_complete_address(self):
        address = ""
        if self.address_line:
            address += self.address_line
        if self.street:
            if address:
                address += ", " + self.street
            else:
                address += self.street
        if self.city:
            if address:
                address += ", " + self.city
            else:
                address += self.city
        if self.state:
            if address:
                address += ", " + self.state
            else:
                address += self.state
        if self.postcode:
            if address:
                address += ", " + self.postcode
            else:
                address += self.postcode
        if self.country:
            if address:
                address += ", " + self.get_country_display()
            else:
                address += self.get_country_display()
        return address

    class Meta:
        verbose_name = _("العنوان")
        verbose_name_plural = _("العناوين ")

from django.contrib.contenttypes.fields import GenericRelation

# class UniversityAbstract(BaseModel):
#     office_no = models.CharField(_("رقم المكتب"), max_length=50,unique=True)
#     name =models.CharField(_("اسم المكتب"), max_length=100,unique=True)
#     # location = models.PointField(_("الموقع"),null=True,blank=True)
#     location = models.CharField(_("Location"), max_length=50)
#     Email = models.EmailField(_("الأيميل"), max_length=254)
#     # office_type = models.CharField(_("نوع المكتب"), max_length=50)
#     # area_service = models.CharField(_("منطقة الخدمة"), max_length=50, blank=True, null=True)
#     note = models.TextField(_("ملاحظة"), blank=True, null=True)
#     Stop = models.BooleanField(_("موقف"), blank=True, null=True,default=False)
#     reason = models.CharField(_("السبب"), max_length=200,blank=True, null=True)
#     date_time = models.DateTimeField(_("التاريخ"), auto_now=True, auto_now_add=False)
#     address = models.ForeignKey(Address, verbose_name = _("العنوان"),on_delete=models.CASCADE)
#     # is_active = models.BooleanField(_("نشط"),default=True)
#     class Meta(BaseModel.Meta):
#         abstract = True
#     def __str__(self):
#         return self.name


# class OfficeArea(OfficeAbstract):
#     pass

    

#     class Meta(OfficeAbstract.Meta):
#         verbose_name = _("ادارة منطقة")
#         verbose_name_plural = _("ادارة المناطق")



#     def get_absolute_url(self):
#         return reverse("OfficeArea_detail", kwargs={"pk": self.pk})


# class Office(OfficeAbstract):
#     office_area = models.ForeignKey("base.OfficeArea", verbose_name=_("ادارة المنطقة"), on_delete=models.CASCADE)

    

#     class Meta(OfficeAbstract.Meta):
#         verbose_name = _("مكتب بريد")
#         verbose_name_plural = _("مكاتب البريد")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Office_detail", kwargs={"pk": self.pk})

# class OfficeSereal(models.Manager):

#     def get_next_number(self,office_id):
        
    
            
#         max_number = self.get_queryset().filter(office_No=office_id).aggregate(models.Max('number')) # {'rating__max': 5}  ,
#         print('max_number in manger')
#         print(max_number['number__max'])
#         if max_number['number__max']:
#             return max_number['number__max']+1
#         else:
#             return 1

# class Office_BaseManager(MyBaseManager):

#     def get_queryset(self,user=None):
#         # return super(MyBaseManager, self).get_queryset()
        
#         if user == None:


#             return super(Office_BaseManager, self).get_queryset()
#         elif user:
#             if user.user_office:
#                 if user.content_type.model_class()== Office:
#                     return super(Office_BaseManager, self).get_queryset(user).filter(office_No=user.user_office,owner__pk__in=user.get_ower_user())
#                 elif user.content_type.model_class()== OfficeArea:
#                     return super(Office_BaseManager, self).get_queryset(user).filter(office_No__in=user.user_office.office_set.values_list('id', flat=True))
#                 else:
#                     print("Office_BaseManager user ",user,user.user_office)
#                     return super(Office_BaseManager, self).get_queryset(user).none()
#             elif user.is_superuser:
#                 return super(Office_BaseManager, self).get_queryset(user)
#             elif user.type_user == '1':
#                 return super(Office_BaseManager, self).get_queryset(user)


#         #         user_list = user.get_ower_user()
#         # if user_list == None:
#         #     print("#"*100)
#         #     print("user_list is None")
#         #     print("#"*100)
#         #     return super(Office_BaseManager, self).get_queryset().filter(owner=user)
#         # else:
#         #     return super(Office_BaseManager, self).get_queryset().filter(owner__in=user_list)

    
#     def get_next_number(self,user=None,field=None):
        
    
            
#         if field:

#             max_number = self.get_queryset(user).filter(office_No=user.user_office).aggregate(models.Max(field)) # {'rating__max': 5}  ,
#             print('max_number in manger')
#             print(max_number[field+'__max'])
#             if max_number[field+'__max']:
#                 return int(max_number[field+'__max'])+1

#             else:
#                 return 1
#         else:
#             max_number = self.get_queryset(user).filter(office_No=user.user_office).aggregate(models.Max('number')) # {'rating__max': 5}  ,
#             print('max_number in manger')
#             print(max_number['number__max'])
#             if max_number['number__max']:
#                 return int(max_number['number__max'])+1

#             else:
#                 return 1
    
    
#     def get_next_number_base(self,user=None,field=None):
        
    
            
#         if field:

#             max_number = self.get_queryset().filter().aggregate(models.Max(field)) # {'rating__max': 5}  ,
#             print('max_number in manger')
#             print(max_number[field+'__max'])
#             if max_number[field+'__max']:
#                 return int(max_number[field+'__max'])+1

#             else:
#                 return 1
#         else:
#             max_number = self.get_queryset().filter().aggregate(models.Max('number')) # {'rating__max': 5}  ,
#             print('max_number in manger')
#             print(max_number['number__max'])
#             if max_number['number__max']:
#                 return int(max_number['number__max'])+1

#             else:
#                 return 1




# class Office_BaseManagerInput(MyBaseManager):

#     def get_queryset(self,user=None):
#         # return super(MyBaseManager, self).get_queryset()
        
#         if user == None:
#             print("Office_BaseManagerInput user None")
#             print("Office_BaseManagerInput user None")
#             print("Office_BaseManagerInput user None")

#             return super(Office_BaseManagerInput, self).get_queryset()
#         elif user:
#             if user.user_office:
#                 if user.content_type.model_class()== Office:
#                     print("Office_BaseManagerInput user Office ",user,user.user_office)
                   
#                     return super(Office_BaseManagerInput, self).get_queryset(user).filter(office_No=user.user_office)
#                 elif user.content_type.model_class()== OfficeArea:
#                     return super(Office_BaseManagerInput, self).get_queryset(user).filter(office_No__in=user.user_office.office_set.values_list('id', flat=True))
#                 else:
#                     print("Office_BaseManagerInput user ",user,user.user_office)
#                     return super(Office_BaseManagerInput, self).get_queryset(user).none()
#             elif user.is_superuser:
#                 return super(Office_BaseManagerInput, self).get_queryset(user)
#             elif user.type_user == '1':
#                 return super(Office_BaseManagerInput, self).get_queryset(user)


#         #         user_list = user.get_ower_user()
#         # if user_list == None:
#         #     print("#"*100)
#         #     print("user_list is None")
#         #     print("#"*100)
#         #     return super(Office_BaseManager, self).get_queryset().filter(owner=user)
#         # else:
#         #     return super(Office_BaseManager, self).get_queryset().filter(owner__in=user_list)

    
#     def get_next_number(self,user=None,field=None):
        
    
            
#         if field:

#             max_number = self.get_queryset(user).filter(office_No=user.user_office).aggregate(models.Max(field)) # {'rating__max': 5}  ,
#             print('max_number in manger')
#             print(max_number[field+'__max'])
#             if max_number[field+'__max']:
#                 return int(max_number[field+'__max'])+1

#             else:
#                 return 1
#         else:
#             max_number = self.get_queryset(user).filter(office_No=user.user_office).aggregate(models.Max('number')) # {'rating__max': 5}  ,
#             print('max_number in manger')
#             print(max_number['number__max'])
#             if max_number['number__max']:
#                 return int(max_number['number__max'])+1

#             else:
#                 return 1
    
    
#     def get_next_number_base(self,user=None,field=None):
        
    
            
#         if field:

#             max_number = self.get_queryset(user).filter().aggregate(models.Max(field)) # {'rating__max': 5}  ,
#             print('max_number in manger')
#             print(max_number[field+'__max'])
#             if max_number[field+'__max']:
#                 return int(max_number[field+'__max'])+1

#             else:
#                 return 1
#         else:
#             max_number = self.get_queryset(user).filter().aggregate(models.Max('number')) # {'rating__max': 5}  ,
#             print('max_number in manger')
#             print(max_number['number__max'])
#             if max_number['number__max']:
#                 return int(max_number['number__max'])+1

#             else:
#                 return 1


   # الجامعة
class University(BaseMPTTModel):
    type=(
        ('Especiall','خاصة'),
        ('governmental','حكوميه')
       )
    name = models.CharField(_("الاسم"),max_length=100,null=False,blank=False)
    phone_number = models.CharField(_("رقم التلفون"),max_length=20,null=False,blank=False)
    address = models.CharField(_("العنوان"),max_length=100,null=False,blank=False)
    type = models.CharField(_("النوع"),max_length=50,choices=type)
    establishment_date = models.DateField(_("تاريخ التأسيس"),null=True,blank=True)
    parent= TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='children')
    is_group = models.BooleanField(_("مجموعة"),default=False)
    # departments = models.IntegerField()
    # students_count = models.IntegerField()
    # academic_members_count = models.IntegerField()
    class Meta:
        verbose_name='الجامعة'
        verbose_name_plural ='الجامغة'
    def __str__(self):
        return self.name    

    class MPTTMeta:
       order_insertion_by = ['name']



class UniversityBaseModel(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """
    university = models.ForeignKey(University, verbose_name=_("الجامعة"), on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_ownership")
    
    # objects = Office_BaseManager()
    # objects1 = Office_BaseManagerInput()
    class Meta:
        # default_manager_name = 'objects1'
        default_manager_name = 'objects'
        # base_manager_name = 'objects'
        abstract = True


class Department(UniversityBaseModel):
    name = models.CharField(_("الاسم"),max_length=255,null=False,blank=False,)
    description = models.TextField(_("الوصف"))
    # university = models.ForeignKey('University', on_delete=models.SET_NULL, null=True)
    # location = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='الاقسام'
        verbose_name_plural='الاقسام'





# class TruckDriver(Person):
#     license_number = models.CharField(_("license number"), max_length=50)
#     issuer = models.CharField(_("Issuer"), max_length=50)
#     release_date = models.DateField(_("Release Date"), auto_now=False, auto_now_add=False)
#     expiry_date = models.DateField(_("Expiry date"), auto_now=False, auto_now_add=False)
#     # shipping_license_number = models.ForeignKey("app.Model", verbose_name=_("Shipping license number"), on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = _("TruckDriver")
#         verbose_name_plural = _("TruckDrivers")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("TruckDriver_detail", kwargs={"pk": self.pk})

# class OfficeEmployees(Person):
#     office_no = models.ForeignKey(Office, verbose_name=_("Office No "), on_delete=models.CASCADE)
#     job_title = models.CharField(_("Job title"), max_length=50)
#     the_role = models.CharField(_("The role"), max_length=50)

    

#     class Meta:
#         verbose_name = _("OfficeEmployees")
#         verbose_name_plural = _("OfficeEmployees")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("OfficeEmployees_detail", kwargs={"pk": self.pk})


# class ShippingOfficesAgents(Person):
#     agency_symbol = models.CharField(_("Agency symbol"), max_length=50)
#     proxy_code = models.CharField(_("Proxy code"), max_length=50)
#     # insurance = models.ForeignKey("app.Model", verbose_name=_("Insurance"), on_delete=models.CASCADE)
#     warranty_number = models.CharField(_("Warranty number"), max_length=50)
#     license_date = models.DateField(_("License date"), auto_now=False, auto_now_add=False)
#     commercial_registration_no = models.CharField(_("Commercial Registration No"), max_length=50)

    

#     class Meta:
#         verbose_name = _("ShippingOfficesAgents")
#         verbose_name_plural = _("ShippingOfficesAgentss")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("ShippingOfficesAgents_detail", kwargs={"pk": self.pk})


# class ShippingDeliveryAgents(Person):

#     agency_symbol = models.CharField(_("Agency symbol"), max_length=50)
#     license_number = models.CharField(_("license number"), max_length=50)
#     type_of_activity = models.CharField(_("Type of activity"), max_length=50)
#     license_date =  models.DateField(_("License date"), auto_now=False, auto_now_add=False)
#     office_Phone = models.CharField(_("Office Phone"), max_length=50)
#     # address = models.ForeignKey("app.Model", verbose_name=_("Title"), on_delete=models.CASCADE)
#     location = models.CharField(_("Location"), max_length=50)
#     is_he_the_driver = models.BooleanField(_("Is he the driver"))


#     class Meta:
#         verbose_name = _("ShippingDeliveryAgents")
#         verbose_name_plural = _("ShippingDeliveryAgentss")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("ShippingDeliveryAgents_detail", kwargs={"pk": self.pk})







################


# class JonralEntryOperation(models.Model):
#     daily_entry_number = models.ForeignKey(User, verbose_name=_("Daily entry number"), on_delete=models.CASCADE,related_name="u")
#     currency = models.ForeignKey(User, verbose_name=_("the currency"), on_delete=models.CASCADE)
#     Exchange_rate = models.FloatField(_("exchange rate"))
#     total_amount = models.FloatField(_("The total amount"))



#     class Meta:
#         abstract = True
#         verbose_name = _("JonralEntryOperation")
#         verbose_name_plural = _("JonralEntryOperations")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("JonralEntryOperation_detail", kwargs={"pk": self.pk})

# class OperatioParcelDetals(BaseModel):
#     parcel_number = models.ForeignKey(Parcel, verbose_name=_("Parcel number"), on_delete=models.CASCADE)
#     type_parcel = models.CharField(_("The type of parcel"), max_length=50)
#     size_parcel = models.FloatField(_("The size of the parcel"))
#     weight_parcel = models.FloatField(_("Weight of the parcel"))
#     dSescription = models.CharField(_("Description"), max_length=50)
#     Parcel_value = models.FloatField(_("Parcel value"))
#     service_costs = models.FloatField(_("Service costs"))
#     address = models.CharField(_("address"), max_length=50)
#     destination = models.CharField(_("Destination"), max_length=50)
#     sending_date = models.DateTimeField(_("Sending Date"), auto_now=False, auto_now_add=False)
#     date_arrival = models.DateTimeField(_("date of arrival"), auto_now=False, auto_now_add=False)
#     exchange_code = models.CharField(_("Exchange code"), max_length=50)
#     note = models.CharField(_("Note"), max_length=50)



#     class Meta:
#         verbose_name = _("OperatioParcelDetals")
#         verbose_name_plural = _("OperatioParcelDetalss")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("OperatioParcelDetals_detail", kwargs={"pk": self.pk})

# class Delvry(Person):
#     trade_name = models.CharField(_("Trade Name"), max_length=50)
#     address = models.CharField(_("address"), max_length=50)
#     phone = models.CharField(_("Phone"), max_length=50)
#     truck_data = models.DateField(_("Truck data"), auto_now=False, auto_now_add=False)
#     service_type = models.CharField(_("service type"), max_length=50)
#     work_area = models.CharField(_("Work area"), max_length=50)
#     set_working_lines = models.ForeignKey(User, verbose_name=_("A set of working lines"), on_delete=models.CASCADE,related_name="p")
#     account_number = models.ForeignKey(User, verbose_name=_("account number"), on_delete=models.CASCADE)



#     class Meta:
#         verbose_name = _("Delvry")
#         verbose_name_plural = _("Delvrys")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Delvry_detail", kwargs={"pk": self.pk})

# class Store(OfficeBaseModel):
#     Store_number = models.CharField(_("Store number"), max_length=50)
#     name_store = models.CharField(_("The name of the store"), max_length=50)
#     location = models.CharField(_("Location"), max_length=50)
#     account_number = models.ForeignKey(User, verbose_name=_("account number"), on_delete=models.CASCADE,related_name="r")
#     employee_name = models.ForeignKey(User, verbose_name=_("Employee Name"), on_delete=models.CASCADE)
#     Store_capacity = models.FloatField(_("Store capacity"))
#     Store_type = models.CharField(_("Store type"), max_length=50)



#     class Meta:
#         verbose_name = _("Store")
#         verbose_name_plural = _("Stores")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Store_detail", kwargs={"pk": self.pk})

# class Account(BaseModel):
#     account_name = models.CharField(_("Account name"), max_length=50)
#     account_number = models.CharField(_("account number"), max_length=50)
#     nature_account = models.CharField(_("The nature of the account"), max_length=50)
#     accountt_type = models.CharField(_("account type"), max_length=50)
#     parent =models.ForeignKey("base.Account", verbose_name=_("Parent"), on_delete=models.CASCADE)
#     anlaysis_account = models.CharField(_("Anlyasis Account"), max_length=50)



#     class Meta:
#         verbose_name = _("Account")
#         verbose_name_plural = _("Accounts")

#     def __str__(self):
#         return self.account_name

#     def get_absolute_url(self):
#         return reverse("Account_detail", kwargs={"pk": self.pk})

# class Truck(models.Model):
#     truck_number = models.CharField(_("Truck number"), max_length=50)
#     truck_type = models.CharField(_("Truck type"), max_length=50)
#     owner_name = models.ForeignKey(User, verbose_name=_("the owner's name"), on_delete=models.CASCADE)
#     driver_name = models.ForeignKey(User, verbose_name=_("The driver's name"), on_delete=models.CASCADE, related_name="h")
#     potty_number = models.CharField(_("Potty number"), max_length=50)
#     truck_load = models.CharField(_("Truck load"), max_length=50)
#     service_type = models.CharField(_("service type"), max_length=50)



#     class Meta:
#         verbose_name = _("Truck")
#         verbose_name_plural = _("Trucks")

#     def __str__(self):
#         return self.truck_number

#     def get_absolute_url(self):
#         return reverse("Truck_detail", kwargs={"pk": self.pk})

# class Address(models.Model):
#     address = models.CharField(_("address"), max_length=50)
#     space = models.CharField(_("space"), max_length=50)
#     zip_code = models.CharField(_("Zip code"), max_length=50)
#     area_name = models.CharField(_("Area name"), max_length=50)




#     class Meta:
#         verbose_name = _("Address")
#         verbose_name_plural = _("Addresss")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Address_detail", kwargs={"pk": self.pk})


# from django.contrib.gis.db import models

# class WorldBorder(models.Model):
#     # Regular Django fields corresponding to the attributes in the
#     # world borders shapefile.
#     name = models.CharField(max_length=50)
#     area = models.IntegerField()
#     pop2005 = models.IntegerField('Population 2005')
#     fips = models.CharField('FIPS Code', max_length=2, null=True)
#     iso2 = models.CharField('2 Digit ISO', max_length=2)
#     iso3 = models.CharField('3 Digit ISO', max_length=3)
#     un = models.IntegerField('United Nations Code')
#     region = models.IntegerField('Region Code')
#     subregion = models.IntegerField('Sub-Region Code')
#     lon = models.FloatField()
#     lat = models.FloatField()

#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     mpoly = models.MultiPolygonField()

#     # Returns the string representation of the model.
#     def __str__(self):
#         return self.name