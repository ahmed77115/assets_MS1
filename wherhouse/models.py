from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel,UniversityBaseModel,University,User,Address,MyBaseManager
from phonenumber_field.modelfields import PhoneNumberField
from base.utils import CURRENCY_CODES
from customer.models import Partner


# Create your models here.

class AbstractStore(UniversityBaseModel):

    name = models.CharField(_("الأسم"), max_length=50)
    number = models.CharField(_("الرقم"), max_length=10)
    store_type = models.CharField(_("نوع المخزن"), max_length=50)
    length = models.FloatField(_("طول"),blank=True, null=True)
    wideth = models.FloatField(_("العرض"),blank=True, null=True)
    height = models.FloatField(_("الارتفاع"),blank=True, null=True)

    class Meta(UniversityBaseModel.Meta):
        # unique
        abstract = True
        verbose_name = _("AbstractStore")
        verbose_name_plural = _("AbstractStores")
        unique_together = [['name','office_No'],['number','office_No'],]

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Warehouse_detail", kwargs={"pk": self.pk})



class Store(AbstractStore):

    # office_no = models.ForeignKey("app.Model", verbose_name=_("University No"), on_delete=models.CASCADE)
    # warehouse_employee = models.ForeignKey(User, verbose_name=_("Warehouse employee number"), on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name=_("العنوان"), on_delete=models.CASCADE,blank=True, null=True)
    location = models.CharField(_("الموقع"), max_length=50,blank=True, null=True)
    phone = PhoneNumberField(_("الهاتف"),blank=True, null=True)

    

    class Meta(UniversityBaseModel.Meta):
        default_manager_name = 'objects1'

        verbose_name = _("مخزن")
        verbose_name_plural = _("مخازن")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("OfficeStores_detail", kwargs={"pk": self.pk})


class WarehouseShelves(BaseModel):

    store = models.ForeignKey(Store, verbose_name=_("Store number"), on_delete=models.CASCADE)
    number = models.CharField(_("Rack number"), max_length=10,unique=True)
    shelf_location = models.CharField(_("Shelf location"), max_length=50,blank=True, null=True)
    highest = models.FloatField(_("The highest"),blank=True, null=True)
    rack_type = models.CharField(_("Rack type"), max_length=50,blank=True, null=True)
    shelf_space = models.FloatField(_("Shelf space"),blank=True, null=True)
    length = models.FloatField(_("Length"),blank=True, null=True)
    wideth = models.FloatField(_("wideth"),blank=True, null=True)
    height = models.FloatField(_("Height"),blank=True, null=True)
    stop = models.BooleanField(_("Stop"),default=False)
    reson = models.CharField(_("Reson"), max_length=250,blank=True, null=True)
    

    class Meta:
        verbose_name = _("WarehouseShelves")
        verbose_name_plural = _("WarehouseShelvess")

    def __str__(self):
        return str(self.store,self.rack_number)

    def get_absolute_url(self):
        return reverse("WarehouseShelves_detail", kwargs={"pk": self.pk})

#    # class Truckstores(Store,BaseModel):
    #     truck_number = models.ForeignKey(TruckData, verbose_name=_("Truck Number"), on_delete=models.CASCADE)

    #     class Meta:
    #         verbose_name = _("Truckstores")
    #         verbose_name_plural = _("Truckstoress")

    #     def __str__(self):
    #         return self.name

    #     def get_absolute_url(self):
    #         return reverse("Truckstores_detail", kwargs={"pk": self.pk})



class ParcelProperties(BaseModel):
    """Model definition for ParcelProperties."""

    # TODO: Define fields here
    name = models.CharField(_("الأسم"), max_length=50,unique=True)
    description = models.CharField(_("الوصف"), max_length=250, blank=True, null=True)

    class Meta(BaseModel.Meta):
        """Meta definition for ParcelProperties."""

        verbose_name = 'خصائص الطرد'
        verbose_name_plural = 'خصائص الطرود'

    def __str__(self):
        """Unicode representation of ParcelProperties."""
        return self.name

class Units(BaseModel):

    name = models.CharField(_("الأسم"), max_length=50,unique=True)
    number = models.CharField(_("الرقم"), max_length=10,unique=True)
        

    class Meta(BaseModel.Meta):
        verbose_name = _("وحدة")
        verbose_name_plural = _("الوحدات ")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("PackageUnits_detail", kwargs={"pk": self.pk})

class Category(BaseModel):

    number = models.CharField(_("رقم الفئة"), max_length=10,unique=True)
    name = models.CharField(_("اسم الفئة"), max_length=50,unique=True)
    unit = models.ForeignKey(Units, verbose_name=_("الوحدة"), on_delete=models.CASCADE)
    from_qty = models.IntegerField(_("من الكمية"),null=True, blank=True)
    to_qty = models.IntegerField(_("الى الكمية"),null=True, blank=True)
    from_length = models.FloatField(_("من الطول"), default=1.0,null=True, blank=True)
    from_width = models.FloatField(_("من العرض"), default=1.0,null=True, blank=True)
    from_height = models.FloatField(_("من الأرتفاع"), default=1.0,null=True, blank=True)    
    from_weight = models.FloatField(_("من الوزن"), default=1.0,null=True, blank=True)
    to_length = models.FloatField(_("الى الطول"), default=1.0,null=True, blank=True)
    to_width = models.FloatField(_("الى العرض"), default=1.0,null=True, blank=True)
    to_height = models.FloatField(_("الى الأرتفاع"), default=1.0,null=True, blank=True)    
    to_weight = models.FloatField(_("الى الوزن"), default=1.0,null=True, blank=True)
    # tolerance_ratio = models.FloatField(_("معدل الزيادة"), blank=True,null=True)
    # extra_increase_volume = models.FloatField(_("قيمة الزيادة"), blank=True,null=True)
 
    class Meta(BaseModel.Meta):
        verbose_name = _("فئة طرد")
        verbose_name_plural = _("فئات الطرد")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

class ParcelType(BaseModel):

    name = models.CharField(_("الأسم"), max_length=50,unique=True)
    number = models.CharField(_("الرقم"), max_length=10,unique=True)
    description = models.TextField(_("الوصف"),null=True, blank=True)
    properties = models.ManyToManyField(ParcelProperties, verbose_name=_("خصائص الطرد"))
    category = models.ManyToManyField(Category, verbose_name=_("فئات الطرد"))

    class Meta(BaseModel.Meta):
        verbose_name = _("نوع الطرد")
        verbose_name_plural = _("انواع الطرود")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("ParcelType_detail", kwargs={"pk": self.pk})

class ParcelCategoryPricing(BaseModel):
    """Model definition for ParcelCategoryPricing."""

    # TODO: Define fields here
    parcel_type = models.ForeignKey(ParcelType, verbose_name=_("نوع الطرد"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=_("الفئة"), on_delete=models.CASCADE)
    date = models.DateTimeField(_("التاريخ"), auto_now_add=True)
    amount = models.FloatField(_("المبلغ"))
    currency = models.CharField(_("العملة"), max_length=50,choices=CURRENCY_CODES)
    exchange_rate = models.CharField(_("سعر الصرف"), max_length=50)
    price_extra_volume = models.FloatField(_("السعر للزيادة في الحجم"))
    enabled = models.BooleanField(_(" غير مفعل"),default=False)
    from_date = models.DateField(_("من تاريخ"))
    to_date = models.DateField(_("الى تاريخ"))


    class Meta(BaseModel.Meta):
        """Meta definition for ParcelCategoryPricing."""

        verbose_name = 'سعر فئة الطرد'
        verbose_name_plural = 'اسعار فئة الطرود'
        get_latest_by = ['date']

    def __str__(self):
        """Unicode representation of ParcelCategoryPricing."""
        return str(self.parcel_type) + " -" + str(self.category)

class TypesExpenses(BaseModel):
    """Model definition for TypesExpenses."""

    # TODO: Define fields here
    name = models.CharField(_("الأسم"), max_length=50,unique=True)
    description = models.TextField(_("الوصف"), null=True, blank=True)
    one_time = models.BooleanField(_("مرة واحدة"), default=True,help_text=_("This option is selected if the bank only downloads one time during the life of the parcel"))
    type_value =models.CharField(_("نوع القيمة"), max_length=50, choices=[("value",_("قيمة")),("rate",_("نسبة"))]) 
    rate_value = models.FloatField(_("النسبة"), null=True, blank=True)

    class Meta(BaseModel.Meta):
        """Meta definition for TypesExpenses."""

        verbose_name = 'نوع المصروف'
        verbose_name_plural = 'انواع المصاريف'

    def __str__(self):
        """Unicode representation of TypesExpenses."""
        return self.name

  

    # def get_absolute_url(self):
    #     """Return absolute url for TypesExpenses."""
    #     return ('')

    # TODO: Define custom methods here


# from shipping.models import SendParcel,ShippingTraffic,PathParcel,StoreMovement

# starting_point
# destination
# service_at_detailed_path
class ParcelQuerySet(models.QuerySet):
    def parcel_for_trips(self,trips_id):
        from shipping_office.models import Trips
        trips_obj =Trips.objects.get(pk = trips_id)
        pp = trips_obj.get_parcel_avalibel()
        print("{"*100)
        print(pp)

        # return self.filter(role='A')

class ParcelManger(MyBaseManager):

    def get_queryset(self):
        return super(ParcelManger, self).get_queryset()

    def parcel_for_trips(self,trips_id):
        from shipping_office.models import Trips
        trips_obj =Trips.objects.get(pk = trips_id)
        pp = trips_obj.get_parcel_avalibel()
        parcel_id = []
        for p in pp:
            parcel_id.append(p['parcel'])
        return self.get_queryset().filter(pk__in= parcel_id)
       

class Parcel(BaseModel):
    # SendParcel = models.ForeignKey(SendParcel, verbose_name=_("بوليصية الشحن"), on_delete=models.CASCADE)
    number = models.CharField(_("رقم الطرد"), max_length=10,unique=True)
    # code = models.CharField(_("كود الشحن"), max_length=10,unique=True)
    parcel_type = models.ForeignKey(ParcelType, verbose_name=_("نوع الطرد"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=_("الفئة"), on_delete=models.CASCADE)
    # qty  = models.IntegerField(_("qty"),default=1)    
    # status_parcel = models.CharField(_("Status of the parcel"), max_length=50)
    # data sender
    sender = models.ForeignKey(Partner, verbose_name=_("اسم المرسل"), on_delete=models.CASCADE,related_name="senders_set")
    sender_address = models.ForeignKey(Address, verbose_name=_("العنوان"), on_delete=models.CASCADE ,related_name="sender_address_set")
    sender_phone = models.CharField(_("رقم الهاتف"), max_length=50)
    # data recipient
    reciver = models.ForeignKey(Partner, verbose_name=_("اسم المستلم"), on_delete=models.CASCADE,related_name="recevers_set")
    reciver_address = models.ForeignKey(Address, verbose_name=_("العنوان"), on_delete=models.CASCADE ,related_name="recever_address_set")
    reciver_phone = models.CharField(_("الهاتف"), max_length=50)
    delivery_note = models.TextField(_("ملاحظة عند التسليم"),blank=True, null=True)
    source = models.ForeignKey(University, verbose_name=_("مصدر الطرد"), on_delete=models.CASCADE, related_name="source_set",blank=True)
    destination = models.ForeignKey(University, verbose_name=_("وجهة الطرد"), on_delete=models.CASCADE,related_name="destination_set",blank=True)
    cost = models.FloatField(_("تكلفة الطرد"),null=True,blank=True)
    # date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    delivery_time = models.DateTimeField(_("وقت وتاريخ التسليم"), auto_now=False, auto_now_add=False)
    # actual_track_number = models.CharField(_("Actual track number"), max_length=50)
    weight = models.FloatField(_("الوزن"))
    length = models.FloatField(_("الطول"), default=1.0,null=True, blank=True)
    width = models.FloatField(_("العرض"), default=1.0,null=True, blank=True)
    height = models.FloatField(_("الأرتفاع"), default=1.0,null=True, blank=True)    
    # address_parcel = models.ForeignKey("app.Model", verbose_name=_("address parcel"), on_delete=models.CASCADE)
    # type_parcel = models.ForeignKey("app.Model", verbose_name=_("Type Parcel"), on_delete=models.CASCADE)
    # note = models.TextField(_("Note"))
    shipping_charges = models.FloatField(_("سعر الشحن"),default=0)
    # total_burden = models.FloatField(_("Total burden"))
    total_expenses = models.FloatField(_("اجمالي المصاريف"),default=0)
    # encode_encodings = models.ForeignKey("app.Model", verbose_name=_("Encode encodings"), on_delete=models.CASCADE)
    # objects = MyBaseManager()
    obj_trips = ParcelManger()

    def __str__(self):
        return self.number
    
    class Meta(BaseModel.Meta):
        verbose_name = ' الطرد'
        verbose_name_plural = ' الطرود'
        # default_manager_name = 'objects'

# obj, created = Person.objects.update_or_create(
#     first_name='John', last_name='Lennon',
#     defaults={'first_name': 'Bob'},)
    def is_served(self):
        ii = self.pathparcel_set.filter(status__in=['1','2','3',])
        if ii:
            return False
        else:
            return True    
    
    def get_current_path(self):
        try:
            if self.is_served():
                return False
            else:
                return self.pathparcel_set.filter(status__in=['1','2','3',]).earliest()
        except  DoesNotExist as e:
            return False
    def get_next_status_path(self):
        if self.has_next():
            return '1'
        else:
            return '4'

    def has_next(self):
        cr = self.get_current_path()
        if cr:
            nx = self.pathparcel_set.filter(sequence=cr.sequence + 1)
            if nx:
                return True
        else:
            return False
    
    def get_next_path(self):
        if self.has_next():
            return self.pathparcel_set.get(sequence=self.get_current_path().sequence + 1)
        else:
            return None

    
    def migrate_to_stor(self):
        self.storemovement_set.all().delete()

        StoreMovement.objects.create(
            # store = self.SendParcel.store ,
            status_parcel ='w_shipment'   ,
            parcel = self  ,
            destination = self.pathparcel_set.earliest('pk').rode.to_office ,
            current_track = self.pathparcel_set.earliest('pk')  ,
            # office_No = self.SendParcel.office_No,
            owner = self.SendParcel.owner,

        )
    def migrate_to_ShippingTraffic(self):
        max_number = ShippingTraffic.bobjects.aggregate(models.Max('number')) # {'rating__max': 5}  ,
        print('max_number')
        print(self.SendParcel.shipping_traffic.all().count())
        max_num = 1
        if max_number['number__max']:
            max_num = max_number['number__max']+1

        if self.SendParcel.shipping_traffic.all().count() == 0:
            created = ShippingTraffic.objects.create(
                    number = max_num,
                    movement_type =  "send" ,
                    # content_type =   ,
                    # operation_number =   ,
                    content_object = self.SendParcel  ,
                    status_parcel ='w_shipment',
                    office =  self.source ,
                    customer = self.sender  ,
                    parcel = self  ,
                    # driver =   ,
                    store = self.SendParcel.store  ,
                    state_store = 'incom'  ,
                    owner = self.owner,

            )
        else:
            obj_sh_t = self.SendParcel.shipping_traffic.all()[0]
            ShippingTraffic.objects.filter(pk=obj_sh_t.id).update(
                    # number = max_num,
                    movement_type =  "send" ,
                    # content_type =   ,
                    # operation_number =   ,
                    # content_object = self.SendParcel  ,
                    status_parcel ='w_shipment',
                    office =  self.source ,
                    customer = self.sender  ,
                    parcel = self  ,
                    # driver =   ,
                    store = self.SendParcel.store  ,
                    state_store = 'incom'  ,
                    modifiedby = self.modifiedby,
            )
    #     pass



    # def save_path_parcel(self):
    #     self.pathparcel_set.all().delete()
    #     path_parcel, path_list= RodeOffice.rod.get_path((self.source.id),(self.destination.id))

    #     price = ParcelCategoryPricing.objects.filter(parcel_type=self.parcel_type,category=self.category).latest()
    #     data = []
    #     total = 0
        
    #     i=0
    #     for rod in path_parcel:
    #         ss="1"
    #         if i ==0:
    #             ss="2"
    #         PathParcel.objects.create(
    #             rode=rod,
    #             parcel=self,
    #             operation_number=self.SendParcel,
    #             currency=self.SendParcel.currency,
    #             amount=rod.distanse * price.amount,
    #             status = ss,
    #             start = University.objects.get(pk=int(path_list[i])),
    #             sequence=int(i+1),
    #             owner = self.owner,
    #         )
    #         i +=1
    #         # d = {}
    #         # d['rode']=rod.id
    #         # d['currency'] = price.currency
    #         # d['amount']= rod.distanse * price.amount
    #         # total +=rod.distanse * price.amount
    #         # data.append(d)
    #         # print(d)
    
    # # pass



class ParcelExpenses(BaseModel):
    """Model definition for ParcelExpenses."""

    # TODO: Define fields here
    parcel = models.ForeignKey(Parcel, verbose_name=_("الطرد"), on_delete=models.CASCADE)
    expenses = models.ForeignKey(TypesExpenses, verbose_name=_("المصروف"), on_delete=models.CASCADE)
    currency = models.CharField(_("العملة"), max_length=50,choices=CURRENCY_CODES)
    amount = models.FloatField(_("المبلغ"))
    status = models.CharField(_("الحالة"), max_length=50, null = True, blank=True)
    # SendParcel = models.ForeignKey(SendParcel, verbose_name=_("بوليصية الشحن"), on_delete=models.CASCADE)
    
    class Meta(BaseModel.Meta):
        """Meta definition for ParcelExpenses."""

        verbose_name = 'مصروف الطرد'
        verbose_name_plural = 'مصاريف الطرود'

    # def __str__(self):
    #     """Unicode representation of ParcelExpenses."""
    #     return self.parcel.number + self.expenses.name



    # def get_absolute_url(self):
    #     """Return absolute url for ParcelExpenses."""
    #     return ('')

    # TODO: Define custom methods here


