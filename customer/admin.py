from django.utils.translation import gettext_lazy as _

from django.contrib import admin

from base.base_delivry import delivry_admin
from base.general.admin import general_admin
from .models import Partner, PartnerAddress
from base.admin import BaseModelAdmin, BaseStackedInline, BaseTabularInline, office, branch
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget, PhoneNumberPrefixWidget
# Register your models here.
from django import forms


class CustomerForm(forms.ModelForm):
    """Form definition for Partner."""
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget())

    class Meta:
        """Meta definition for Customerform."""

        model = Partner
        fields = '__all__'


class CustomerAddressInline(admin.TabularInline):
    '''Stacked Inline View for PartnerAddress'''
    fieldsets = (
        (_(" معلومات عنوان العميل"), {
            "fields": (
                ('partner',),
                ('type_address','note',),
           
                )
        }),)
    list_display=['partner','type_address','note']

    model = PartnerAddress
    # min_num = 3
    max_num = 20
    extra = 1
    #autocomplete_fields = ("address",)
    show_change_link = True

    # raw_id_fields = (,)

class CustomerAdmin(BaseModelAdmin):
    list_display = ('customer_number', 'customer_type', 'name',)
    search_fields = ('customer_number', 'customer_type', 'name',)

    fieldsets = (
        (_("البيانات الاساسية "), {
            "fields": (
                ('customer_number', 'customer_type', 'name', 'date_joined','user_type','status','gender'

                 ),),
        }),
        # (_(" بيانات الاتصال"), {
        #     "fields": (('phone_number', 'user_email',),),
        # }),
        (_(" الهويه "), {
            "classes": ("collapse",),
            "fields": (
                'identity_type', 'identification_number', 'issuer', 'release_date', 'expiry_date',
            ),
        }),
        (_("خيارات متقدمة "), {
            'classes': ('collapse',),
            "fields": (
                'stop', 'reason',

            )}),
    )

    # list_display = ('',)
    form = CustomerForm
    inlines = (CustomerAddressInline,)

    def save_model(self, request, obj, form, change):
        print("#" * 100)
        print(request.user)
        print("#" * 100)
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

           
admin.site.register(Partner, CustomerAdmin)

   
office.register(Partner, CustomerAdmin)
branch.register(Partner, CustomerAdmin)
general_admin.register(Partner, CustomerAdmin)
delivry_admin.register(Partner, CustomerAdmin)
