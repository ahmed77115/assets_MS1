from django.contrib import admin

from base.admin import BaseModelAdmin, BaseTabularInline, office, branch
from base.base_delivry import delivry_admin
from base.general.admin import general_admin
from .models import *


# Register your models here.
# Store
# WarehouseShelves
# ParcelProperties
# Units
# Category
# ParcelType
# ParcelCategoryPricing
# TypesExpenses
# Parcel
# ParcelExpenses

class WarehouseShelvesInline(admin.TabularInline):
    '''Tabular Inline View for WarehouseShelves'''

    model = WarehouseShelves
    min_num = 3
    max_num = 20
    extra = 1
    # raw_id_fields = (,)


# @admin.register(Store)
class StoreAdmin(BaseModelAdmin):
    '''Admin View for Store'''

    list_display = ('name', 'number', 'address', 'phone',)
    # list_filter = ('',)
    # inlines = [
    #     WarehouseShelvesInline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


office.register(Store, StoreAdmin)
branch.register(Store, StoreAdmin)
general_admin.register(Store, StoreAdmin)


# WarehouseShelves

# @admin.register(WarehouseShelves)
class WarehouseShelvesAdmin(BaseModelAdmin):
    '''Admin View for WarehouseShelves'''

    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


# ParcelProperties
# @admin.register(ParcelProperties)
class ParcelPropertiesAdmin(BaseModelAdmin):
    '''Admin View for ParcelProperties'''

    list_display = ('name', 'description')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


branch.register(ParcelProperties, ParcelPropertiesAdmin)
general_admin.register(ParcelProperties, ParcelPropertiesAdmin)


# Units
# @admin.register(Units)
class UnitsAdmin(BaseModelAdmin):
    '''Admin View for Units'''

    list_display = ('name', 'number')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name',)
    # date_hierarchy = ''
    # ordering = ('',)


general_admin.register(Units, UnitsAdmin)
branch.register(Units, UnitsAdmin)


# Category

# @admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    '''Admin View for Category'''
    fieldsets = (
        (None, {
            "fields": (
                ('number', 'name', 'unit',),
            ),
        }),
        (None, {
            "fields": (
                ('from_qty', 'to_qty',),
                ('from_length', 'to_length',),
                ('from_width', 'to_width',),
                ('from_height', 'to_height',),
                ('from_weight', 'to_weight',),
                # ('tolerance_ratio', 'extra_increase_volume',),
            ),
        }),

    )
    search_fields = ('name',)
    autocomplete_fields = ('unit',)
    list_display = ('number', 'name',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


general_admin.register(Category, CategoryAdmin)
branch.register(Category, CategoryAdmin)


class CategoryInline(BaseTabularInline):
    '''Tabular Inline View for Category'''

    model = Category
    min_num = 3
    max_num = 20
    extra = 1
    # raw_id_fields = (,)


# ParcelType

class ParcelTypeAdmin(BaseModelAdmin):
    '''Admin View for ParcelType'''
    filter_horizontal = ('category', 'properties')
    search_fields = ('name', 'number', 'description',)

    list_display = ('name', 'number', 'description',)
    list_filter = ('category', 'properties')
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


general_admin.register(ParcelType, ParcelTypeAdmin)
branch.register(ParcelType, ParcelTypeAdmin)


# ParcelCategoryPricing
# @admin.register(ParcelCategoryPricing)

class ParcelCategoryPricingAdmin(BaseModelAdmin):
    '''Admin View for ParcelCategoryPricing'''
    list_display = ('parcel_type', 'category', 'amount', 'currency', 'enabled', 'from_date', 'to_date',)
    list_filter = ('parcel_type', 'category', 'enabled',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    date_hierarchy = 'date'
    # ordering = ('',)

general_admin.register(ParcelCategoryPricing, ParcelCategoryPricingAdmin)


# TypesExpenses
# @admin.register(TypesExpenses)

class TypesExpensesAdmin(BaseModelAdmin):
    '''Admin View for TypesExpenses'''
    list_display = ('name', 'description', 'one_time', 'type_value', 'rate_value',)
    list_filter = ('one_time', 'type_value',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)

    search_fields = ('name',)
    # date_hierarchy = ''
    # ordering = ('',)


general_admin.register(TypesExpenses, TypesExpensesAdmin)
branch.register(TypesExpenses, TypesExpensesAdmin)


# class ParcelInline(BaseStackedInline):
#     '''Stacked Inline View for Parcel'''

#     model = Parcel
#     # min_num = 3
#     # max_num = 20
#     extra = 1
#     # raw_id_fields = (,)

# Parcel
# @admin.register(Parcel)
class ParcelAdmin(BaseModelAdmin):
    '''Admin View for Parcel'''

    list_display = ('number', 'parcel_type', 'category', 'sender', 'reciver', 'source', 'destination',)
    list_filter = ('parcel_type', 'category', 'source', 'destination',)
    # inlines = [
    #     ParcelExpensesInline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
    # def has_add_permission(self, request):
    #     return False

    # def has_edit_permission(self, request):
    #     return False

    # def has_delete_permission(self, request):
    #     return False


# ParcelExpenses


general_admin.register(Parcel, ParcelAdmin)
branch.register(Parcel, ParcelAdmin)
office.register(Parcel, ParcelAdmin)
delivry_admin.register(Parcel, ParcelAdmin)