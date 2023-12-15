from django.core.exceptions import (
    FieldDoesNotExist, FieldError, PermissionDenied, ValidationError,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib import admin



# from django.contrib.gis import admin as admin_gis
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
from .models import *
from django.contrib import messages
import json
from django import forms
from django.urls import reverse
from django.utils.html import format_html
# from easy_maps.models import Address as aaa
from django.contrib.admin import AdminSite
from .admins.user_admin import *
class Inlinedeprament(admin.TabularInline):
    model=Department
    extra=1
    fieldsets = (
        (_(" معلومات القسم"), {
            "fields": (
                ('name','university',),
                ('description',),
                
                )
        }),
     )
    list_display=['name','university','description'] 

class universityadmin(admin.ModelAdmin):
     fieldsets = (
        (_(" معلومات الجامعة"), {
            "fields": (
                ('name','phone_number',),
                ('address','type',),
                  ('establishment_date','is_group',),
                
                )
        }),
     )
     list_display=['name','phone_number','address','type','establishment_date','is_group']
     inlines=[Inlinedeprament]
admin.site.register(University,universityadmin)    
   

   


    
# admin.site.register(Department,depramentadmin)     
# class Addressadmin(admin.ModelAdmin):
    #list_display=['address_line','address_line','city','country','location']
# admin.site.register(Address,Addressadmin)
  


class EventAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"


event_admin_site = EventAdminSite(name='event_admin')


# General Administration

# District administration
class DistrictAdmin(AdminSite):
    site_header = "District administration"
    site_title = "District administration Portal"
    index_title = "Welcome to District administration Portal"

    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view
        *at least one* page in the admin site.
        """
        ii = request.user.is_active and request.user.is_staff
        if not request.user.is_anonymous:
            if request.user.type_user != '1':
                return request.user.content_type.model_class() == OfficeArea and ii
            elif request.user.is_superuser:
                return request.user.is_active and request.user.is_staff
            else:
                return False


        else:
            return request.user.is_active and request.user.is_staff



branch = DistrictAdmin(name='branch_admin')


# Management of service offices
class ServiceAdmin(AdminSite):
    site_header = "Management of service offices"
    site_title = "Management of service offices Portal"
    index_title = "Welcome to Management of service offices Portal"

    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view
        *at least one* page in the admin site.
        """
        ii = request.user.is_active and request.user.is_staff
        if not request.user.is_anonymous:
            if request.user.type_user != '1':
                return request.user.content_type.model_class() == Office and ii
            elif request.user.is_superuser:
                return request.user.is_active and request.user.is_staff
            else:
                return False


        else:
            return request.user.is_active and request.user.is_staff


office = ServiceAdmin(name='servic_admin')


# Managing freight offices
class FreightAdmin(AdminSite):
    site_header = _("Managing freight offices")
    site_title = "Managing freight offices Portal"
    index_title = "Welcome to Managing freight offices portal"


freight_admin_site = EventAdminSite(name='freight_admin')
###############################
# from easy_maps.widgets import AddressWithMapWidget

# from .models import Firm

# class FirmAdmin(admin_gis.GeoModelAdmin):
#     class form(forms.ModelForm):
#         class Meta:
#             widgets = {
#                 'address': AddressWithMapWidget({'class': 'vTextField'})
#             }

# admin.site.register(Firm, FirmAdmin)

# event_admin_site.register(aaa)


# event_admin_site.register(Event)
# event_admin_site.register(EventHero)
# event_admin_site.register(EventVillain)


class BaseModelAdmin(admin.ModelAdmin):
    # list_display = ('',)
    exclude = ('createdat', 'modifiedat', 'owner', 'modifiedby', 'deletedby', 'deletedat', 'deleted')
    view_on_site = False

    def save_model(self, request, obj, form, change):
        # print(request.__dict__)
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.owner = request.user
            instance.save()
        formset.save_m2m()

    def get_queryset(self, request):
        """
        Return a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        # print("#"*80)
        # print("in get_queryset")
        # print(type(self.model._default_manager))
        # print((request.user.get_ower_user()))
        # print("#"*80)
        try:
            qs = self.model._default_manager.get_queryset(user=request.user)
            print(qs)
        except Exception as e:
            print("exceptions")
            print(str(e))
        # qs = self.model.yobjects.get_queryset(request.user)
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def get_field_queryset(self, db, db_field, request):
        """
        If the ModelAdmin specifies ordering, the queryset should respect that
        ordering.  Otherwise don't specify the queryset, let the field decide
        (return None in that case).
        """
        related_admin = self.admin_site._registry.get(db_field.remote_field.model)
        if related_admin is not None:
            ordering = related_admin.get_ordering(request)
            if ordering is not None and ordering != ():
                print("#" * 111)
                print("in get_field_queryset with related_admin", db_field, db_field.name)

                return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db).order_by(
                    *ordering)
        print("#" * 88)
        print("in get_field_queryset ", db_field, db_field.name, request.user)
                        
        if not db_field.remote_field.model == ContentType:
            return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db)
        return db_field.remote_field.model._default_manager.get_queryset().using(db)
        return None

    def get_changeform_initial_data(self, request):
        print("hjhjhjhj")
        initial = dict(request.GET.items())
        for k in initial:
            try:
                f = self.model._meta.get_field(k)
            except FieldDoesNotExist:
                continue
            # We have to special-case M2Ms as a list of comma-separated PKs.
            if isinstance(f, models.ManyToManyField):
                initial[k] = initial[k].split(",")
        try:
            f = self.model._meta.get_field('office_No')
            initial['office_No'] = request.user.user_office
        except FieldDoesNotExist:
            pass
        try:
            f = self.model._meta.get_field('office')
            initial['office'] = request.user.user_office
        except FieldDoesNotExist:
            pass
        try:
            f = self.model._meta.get_field('office_area')
            initial['office_area'] = request.user.user_office
        except FieldDoesNotExist:
            pass

        try:
            f = self.model._meta.get_field('office_no')
            initial['office_no'] = self.model._default_manager.get_next_number(request.user,field='office_no')
        except FieldDoesNotExist:
            pass

        try:
            f = self.model._meta.get_field('number')
            initial['number'] = self.model._default_manager.get_next_number(request.user)
        except FieldDoesNotExist:
            pass
        try:
            f = self.model._meta.get_field('sereal')
            initial['sereal'] = self.model._default_manager.get_next_number_base(request.user, field='sereal')
        except FieldDoesNotExist:
            pass
        try:
            f = self.model._meta.get_field('date')
            initial['date'] = timezone.now()
        except FieldDoesNotExist:
            pass
        try:
            f = self.model._meta.get_field('date_time')
            initial['date_time'] = timezone.now()
        except FieldDoesNotExist:
            pass

        return initial


class OfficeBaseModelAdmin(BaseModelAdmin):
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(MyModelAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['my_field_name'].initial = 'abcd'
    #     return form
    # def get_changeform_initial_data(self, request):
    #     return {'name': 'custom_initial_value'}

    def get_field_queryset(self, db, db_field, request):
        """
        If the ModelAdmin specifies ordering, the queryset should respect that
        ordering.  Otherwise don't specify the queryset, let the field decide
        (return None in that case).
        """
        if db_field.name == 'office_No':
            if request.user.user_office:
                if request.user.content_type.model_class() == Office:
                    return db_field.remote_field.model._default_manager.get_queryset(request.user).filter(
                        pk=request.user.user_office.pk).using(db)
        elif db_field.name == 'driver':
            print("kkkkkkkkkkkkkkkkkkkkk")
            if request.user.user_office:
                print("kkkkkkkkkkkkkkkkkkkkk")
                if request.user.content_type.model_class() == Office:
                    print("kkkkkkkkkkkkkkkkkkkkk",
                          db_field.remote_field.model.bobjects.get_queryset().filter().using(db))
                    return db_field.remote_field.model.bobjects.get_queryset().filter(type_user='4').using(db)
        return super().get_field_queryset(db, db_field, request=request)
        # related_admin = self.admin_site._registry.get(db_field.remote_field.model)
        # if related_admin is not None:
        #     ordering = related_admin.get_ordering(request)
        #     if ordering is not None and ordering != ():
        #         print("#"*111)
        #         print("in get_field_queryset with related_admin",db_field)

        #         return db_field.remote_field.model._default_manager.using(db).order_by(*ordering)
        # print("#"*111)
        # print("in get_field_queryset ",db_field)
        # return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db)
        # return None


class OfficeDriverModelAdmin(BaseModelAdmin):
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(MyModelAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['my_field_name'].initial = 'abcd'
    #     return form
    # def get_changeform_initial_data(self, request):
    #     return {'name': 'custom_initial_value'}

    # def get_changeform_initial_data(self, request):
    #     print("hjhjhjhj")
    #     return {
    #         'office': request.user.user_office,
    #         'number':self.model._default_manager.get_next_number(request.user),
    #         # 'sereal':self.model._default_manager.get_next_number_base(request.user,field='sereal'),
    #     }

    def get_field_queryset(self, db, db_field, request):
        """
        If the ModelAdmin specifies ordering, the queryset should respect that
        ordering.  Otherwise don't specify the queryset, let the field decide
        (return None in that case).
        """
        if db_field.name == 'office':
            if request.user.user_office:
                if request.user.content_type.model_class() == OfficeTransport:
                    return db_field.remote_field.model._default_manager.get_queryset(request.user).filter(
                        pk=request.user.user_office.pk).using(db)
        return super().get_field_queryset(db, db_field, request=request)
        # related_admin = self.admin_site._registry.get(db_field.remote_field.model)
        # if related_admin is not None:
        #     ordering = related_admin.get_ordering(request)
        #     if ordering is not None and ordering != ():
        #         print("#"*111)
        #         print("in get_field_queryset with related_admin",db_field)

        #         return db_field.remote_field.model._default_manager.using(db).order_by(*ordering)
        # print("#"*111)
        # print("in get_field_queryset ",db_field)
        # return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db)
        # return None


class BaseModelAdminOSM(BaseModelAdmin):
    # list_display = ('',)
    pass
    # exclude = ('createdat', 'modifiedat', 'owner', 'modifiedby', 'deletedby', 'deletedat', 'deleted')
    # view_on_site = False

    # def save_model(self, request, obj, form, change):
    #     # print(request.__dict__)
    #     obj.owner = request.user
    #     super().save_model(request, obj, form, change)

    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     for obj in formset.deleted_objects:
    #         obj.delete()
    #     for instance in instances:
    #         instance.owner = request.user
    #         instance.save()
    #     formset.save_m2m()

    # def get_queryset(self, request):
    #     """
    #     Return a QuerySet of all model instances that can be edited by the
    #     admin site. This is used by changelist_view.
    #     """
    #     # print("#"*80)
    #     # print("in get_queryset")
    #     # print(type(self.model._default_manager))
    #     # print((request.user.get_ower_user()))
    #     # print("#"*80)
    #     try:
    #         qs = self.model._default_manager.get_queryset(user=request.user)
    #         print(qs)
    #     except Exception as e:
    #         print("exceptions")
    #         print(str(e))
    #     # qs = self.model.yobjects.get_queryset(request.user)
    #     # TODO: this should be handled by some parameter to the ChangeList.
    #     ordering = self.get_ordering(request)
    #     if ordering:
    #         qs = qs.order_by(*ordering)
    #     return qs

    # def get_field_queryset(self, db, db_field, request):
    #     """
    #     If the ModelAdmin specifies ordering, the queryset should respect that
    #     ordering.  Otherwise don't specify the queryset, let the field decide
    #     (return None in that case).
    #     """
    #     related_admin = self.admin_site._registry.get(db_field.remote_field.model)
    #     if related_admin is not None:
    #         ordering = related_admin.get_ordering(request)
    #         if ordering is not None and ordering != ():
    #             print("#" * 111)
    #             print("in get_field_queryset with related_admin", db_field, db_field.name)

    #             return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db).order_by(
    #                 *ordering)
    #     print("#" * 88)
    #     print("in get_field_queryset ", db_field, db_field.name, request.user)
                        
    #     if not db_field.remote_field.model == ContentType:
    #         return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db)
    #     return db_field.remote_field.model._default_manager.get_queryset().using(db)
    #     return None

    # def get_changeform_initial_data(self, request):
    #     print("hjhjhjhj")
    #     initial = dict(request.GET.items())
    #     for k in initial:
    #         try:
    #             f = self.model._meta.get_field(k)
    #         except FieldDoesNotExist:
    #             continue
    #         # We have to special-case M2Ms as a list of comma-separated PKs.
    #         if isinstance(f, models.ManyToManyField):
    #             initial[k] = initial[k].split(",")
    #     try:
    #         f = self.model._meta.get_field('office_No')
    #         initial['office_No'] = request.user.user_office
    #     except FieldDoesNotExist:
    #         pass
    #     try:
    #         f = self.model._meta.get_field('office')
    #         initial['office'] = request.user.user_office
    #     except FieldDoesNotExist:
    #         pass
    #     try:
    #         f = self.model._meta.get_field('office_area')
    #         initial['office_area'] = request.user.user_office
    #     except FieldDoesNotExist:
    #         pass

    #     try:
    #         f = self.model._meta.get_field('office_no')
    #         initial['office_no'] = self.model._default_manager.get_next_number(request.user,field='office_no')
    #     except FieldDoesNotExist:
    #         pass

    #     try:
    #         f = self.model._meta.get_field('number')
    #         initial['number'] = self.model._default_manager.get_next_number(request.user)
    #     except FieldDoesNotExist:
    #         pass
    #     try:
    #         f = self.model._meta.get_field('sereal')
    #         initial['sereal'] = self.model._default_manager.get_next_number_base(request.user, field='sereal')
    #     except FieldDoesNotExist:
    #         pass
    #     try:
    #         f = self.model._meta.get_field('date')
    #         initial['date'] = django.utils.timezone.now()
    #     except FieldDoesNotExist:
    #         pass
    #     try:
    #         f = self.model._meta.get_field('date_time')
    #         initial['date_time'] = timezone.now()
    #     except FieldDoesNotExist:
    #         pass

    #     return initial


class BaseStackedInline(admin.StackedInline):
    '''Stacked Inline View for BaseStacked'''
    view_on_site = False

    exclude = ('createdat', 'modifiedat', 'owner', 'modifiedby', 'deletedby', 'deletedat', 'deleted')

    def get_queryset(self, request):
        """
        Return a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        print("#" * 80)
        print("in get_queryset")
        print(type(self.model._default_manager))
        print((request.user.get_ower_user()))
        print("#" * 80)
        qs = self.model._default_manager.get_queryset(user=request.user)
        # qs = self.model.yobjects.get_queryset(request.user)
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def get_field_queryset(self, db, db_field, request):
        """
        If the ModelAdmin specifies ordering, the queryset should respect that
        ordering.  Otherwise don't specify the queryset, let the field decide
        (return None in that case).
        """
        related_admin = self.admin_site._registry.get(db_field.remote_field.model)
        if related_admin is not None:
            ordering = related_admin.get_ordering(request)
            if ordering is not None and ordering != ():
                print("#" * 111)
                print("in get_field_queryset with related_admin", db_field)

                return db_field.remote_field.model._default_manager.using(db).order_by(*ordering)
        print("#" * 111)
        print("in get_field_queryset ", db_field)
        return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db)
        return None

    # def get_changeform_initial_data(self, request):
    #     return {
    #         # 'office_No': request.user.user_office,
    #         'number':self.model._default_manager.get_next_number(request.user),
    #         'sereal':self.model._default_manager.get_next_number(request.user,field='sereal'),
    #     }


class BaseTabularInline(admin.TabularInline):
    '''Stacked Inline View for BaseStacked'''
    exclude = ('createdat', 'modifiedat', 'owner', 'modifiedby', 'deletedby', 'deletedat', 'deleted')

    def get_queryset(self, request):
        """
        Return a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        print("#" * 80)
        print("in get_queryset")
        print(type(self.model._default_manager))
        print((request.user.get_ower_user()))
        print("#" * 80)
        qs = self.model._default_manager.get_queryset(user=request.user)
        # qs = self.model.yobjects.get_queryset(request.user)
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def get_field_queryset(self, db, db_field, request):
        """
        If the ModelAdmin specifies ordering, the queryset should respect that
        ordering.  Otherwise don't specify the queryset, let the field decide
        (return None in that case).
        """
        related_admin = self.admin_site._registry.get(db_field.remote_field.model)
        if related_admin is not None:
            ordering = related_admin.get_ordering(request)
            if ordering is not None and ordering != ():
                print("#" * 111)
                print("in get_field_queryset with related_admin", db_field)

                return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db).order_by(
                    *ordering)
        print("#" * 111)
        print("in get_field_queryset ", db_field)
        return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db)

    # def get_changeform_initial_data(self, request):
    #     return {
    #         # 'office_No': request.user.user_office,
    #         'number':self.model._default_manager.get_next_number(request.user),
    #         'sereal':self.model._default_manager.get_next_number(request.user,field='sereal'),
    #     }


class OfficeAreaAdmin(BaseModelAdminOSM):
    search_fields = ('office_no', 'name')
    autocomplete_fields = ('address',)
    date_hierarchy ='date_time'
    fieldsets = (
        (None, {
            "fields": (
                ('office_no','name',),
                # 'date_time',
                ('Email','address',),
                'location',
                'note',)
        }),
        (_('Advanced options'),{
            'classes': ('collapse ' ,),
            "fields": (
                'Stop','reason',            ),
        }),
    )
    
    list_display = ('office_no','name','Stop',)
from base.general.admin import general_admin
# general_admin.register(OfficeArea, OfficeAreaAdmin)

# from delivery_agents.admin import DelivryDriverOfficeInline



# search_fields = ('country')
# autocomplete_fields = ('country',)
# list_display = ('',)
from .utils import COUNTRIES
from dal import autocomplete


class CountryAutocompleteFromList(autocomplete.Select2ListView):
    def get_result_label(self, obj):


        return format_html("{} - {}", obj.name, obj.description)

    def get_list(self):
        return COUNTRIES
    # def autocomplete_results(self, results):
    #     """Return list of strings that match the autocomplete query."""
    #     print("#"*100)
    #     print(results)
    #     print("#"*100)
    #     print(self.__dict__)
    #     print("#"*100)
    #     return [x for x in results if self.q in x[0] or self.q in x[1]]


# data = [line.strip() for line in open("C:\corpus\TermList.txt", 'r')]
# texts = [[word.lower() for word in text.split()] for text in data]

def get_choice_list():
    return [x for x in COUNTRIES]


# class CountryForm(forms.ModelForm):
#     country = autocomplete.Select2ListChoiceField(
#         choice_list=COUNTRIES,
#         widget=autocomplete.ListSelect2(url='country_list_autocomplete')
#     )
#     class Meta:
#         model = Address
#         fields = '__all__'
class AddressAdmin(admin.ModelAdmin):
    list_display=('address_line', 'street', 'city', 'state', 'postcode', 'country',)
admin.register(Address, AddressAdmin)
class AddressAdmin(BaseModelAdminOSM):
    # form = CountryForm
    search_fields = ('address_line', 'street', 'city', 'state', 'postcode', 'country',)


general_admin.register(Address, AddressAdmin)
branch.register(Address, AddressAdmin)

office.register(Address, AddressAdmin)
from base.base_delivry import delivry_admin
delivry_admin.register(Address, AddressAdmin)
#office.register(User, UserAdmin)

# admin.site.register(Name, NameAdmin)


# admin.site.register(User)
# admin.site.register(Address)
class StatewAdmin(admin.ModelAdmin):
    list_display = ('modifiedby', 'link_to_B', 'owner')
    list_display_links = ('modifiedby',)

    def link_to_user(self, obj):
        link = reverse("admin:auth_user_change", args=[obj.user_id])
        return format_html('<a href="{}">Edit {}</a>', link, obj.user.username)

    link_to_user.short_description = 'Edit user'

    def link_to_B(self, obj):
        link = reverse("admin:base_user_change", args=[obj.owner_id])  # model name has to be lowercase
        return format_html('<a href="{}">{}</a>', link, obj.owner.email)


# admin.site.register(Office,StatewAdmin)
# admin.site.register(Customer)
# admin.site.register(TrafficRodeNetwork)
# admin.site.register(DetailsCompoundPath)


class RentalAdmin(admin.ModelAdmin):
    pass
    # formfield_overrides = {
    #     map_fields.AddressField: {
    #         'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    # }


# formfield_overrides = {

#         map_fields.AddressField: { 'widget':
#             map_widgets.GoogleMapsAddressWidget(attrs={
#             'data-autocomplete-options': json.dumps({ 'types': ['geocode',
#             'establishment'], 'componentRestrictions': {
#                         'country': 'ye'
#                     }
#                 })
#             })
#             }


# map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},


# formfield_overrides = {
#     map_fields.AddressField: {
#       'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
# }


# admin.site.register(Rental,RentalAdmin)

# Register your models here.
# from admin_reports import Report, register


# @register()
# class MyReport(Report):
#     'admin_reports:my_report'

#     def aggregate(self, **kwargs):
#         aa = User.objects.all()

#         return [a.__dict__ for a in aa
#                 # dict([(k, v) for v, k in enumerate('abcdefgh')]),
#                 # dict([(k, v) for v, k in enumerate('abcdefgh')]),
#                 ]


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class StateAdmin(admin.ModelAdmin):

#     fieldsets = (
#         (None, {
#             # 'classes': ('wide ' ,),
#             "fields": ((
#                 'username',
#                 'first_name',
#                 'last_name'),
#                 'email',
#                 'is_staff',
#                 'is_active',)}),
#         ('Advanced options', {
#             'classes': ('collapse card' ,),
#             "fields":(
#                 'date_joined',
#                 'owner',
#                 'modifiedby',
#                 'deletedby',
#                 'deleted',
#                 'type_user',
#                 'phone',
#                 )}),
#         (None, {
#             'classes': ('wide '),
#             "fields":(

#                             ),
#                         }),
#                     )
#     raw_id_fields = ("modifiedby",)
#     search_fields = ['owner']
#     autocomplete_fields = ['owner']
#     prepopulated_fields = {"first_name": ("first_name",)}
#     list_display = ('first_name', 'is_active', 'email','is_staff',                'date_joined',
#                 'owner',
#                 'modifiedby',
#                 'deletedby',
#                 'deleted',
#                 'type_user',
#                 'phone',
#         )   

#     # inlines = [

#     #     DelivryDriverOfficeInline
#     # ]
#     # list_display_links = ('first_name',)
#     list_editable   = ('email',)
#     # exclude =('',)list_display 
#     date_hierarchy = 'createdat'
#     # def active(self, obj):
#     #     return obj.is_active == 1
#     #
#     # active.boolean = True
#     #
#     # def make_active(modeladmin, request, queryset):
#     #     queryset.update(is_active = 1)
#     #     messages.success(request, "Selected Record(s) Marked as Active Successfully !!")
#     #
#     # def make_inactive(modeladmin, request, queryset):
#     #     queryset.update(is_active = 0)
#     #     messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")
#     #
#     # admin.site.add_action(make_active, "Make Active")
#     # admin.site.add_action(make_inactive, "Make Inactive")
#     #
#     # def has_delete_permission(self, request, obj = None):
#     #     return False
#     #
#     # def has_add_permission(self, request):
#     #     return False
#     #
#     class Media:
#         # css = {
#         #     "all": ("my_styles.css",)
#         # }
#         js = ("get_ajax.js",)

# admin.site.register(User, StateAdmin)


# admin.site.register(Rental, RentalAdmin)


# class DelivryDriverOfficeAdmin(StateAdmin):
#     '''Admin View for DelivryDriverOffice'''

#     # list_display = ('',)
#     # list_filter = ('',)
#     inlines = StateAdmin.inlines + [DelivryDriverOfficeInline, ]
#     # raw_id_fields = ('',)
#     # readonly_fields = ('',)
#     # search_fields = ('',)
#     # date_hierarchy = ''
#     # ordering = ('',)

# from delivery_agents.models import DelivryDriverOffice

# admin.site.unregister(User)
# admin.site.register(User, DelivryDriverOfficeAdmin)

# from django import forms

# from .models import MyModel


# class MyModelForm(forms.ModelForm):

#     class Meta:
#         fields = ('location', 'location_lat', 'location_lon', )
#         model = MyModel

# @admin.register(MyModel)
# class MyModelAdmin(admin.ModelAdmin):
#     '''Admin View for MyModel'''

#     # list_display = ('',)
#     # list_filter = ('',)
#     # inlines = [
#     #     Inline,
#     # ]
#     # raw_id_fields = ('',)
#     # readonly_fields = ('',)
#     # search_fields = ('',)
#     # date_hierarchy = ''
#     # ordering = ('',)
#     class Media:

#         js = ("js/vendor/leaflet.js","js/osm_field.js",)
#         css = {
#             "all": ("css/vendor/leaflet.css","css/osm_field.css",)
#         }


from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


# from django.contrib import admin
# from django.apps import apps
# from .models import *
# #Register your models here.
# models = apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass