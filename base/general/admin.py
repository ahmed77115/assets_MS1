from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.admin import AdminSite
from base.models import Address, User
from base.admin import BaseModelAdmin, BaseStackedInline, BaseTabularInline
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline
from base.admins.user_admin import UserAdmin

class UserInline(GenericTabularInline):
    '''Tabular Inline View for User'''

    model = User
    min_num = 3
    max_num = 20
    extra = 1
    # raw_id_fields = (,)


class GeneralAdmin(AdminSite):
    site_header = "General Administration"
    site_title = "General Administration Portal"
    index_title = "Welcome to General Administration Portal"

    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view
        *at least one* page in the admin site.
        """
        ii = request.user.is_active and request.user.is_staff
        if not request.user.is_anonymous:
            if request.user.type_user == '1':
                return ii
            elif request.user.is_superuser:
                return request.user.is_active and request.user.is_staff
            else:
                return False


        else:
            return request.user.is_active and request.user.is_staff


general_admin = GeneralAdmin(name='general_admin')


# @admin.register(OfficeArea)
class OfficeAreaAdmin(BaseModelAdmin):
    '''Admin View for OfficeArea'''
    pass
    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     UserInline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


# class OfficeAreaAdmin(BaseModelAdmin):
#     pass
# list_display = ('',)

# from delivery_agents.admin import DelivryDriverOfficeInline


# general_admin.register(OfficeArea, OfficeAreaAdmin)
general_admin.register(User,UserAdmin)

# import autocomplete_light
# from autocomplete_light.contrib.generic_m2m import GenericModelForm,GenericModelMultipleChoiceField

# # from models import ModelGroup
# from django.contrib.auth.models import Group

# class ModelGroupForm(GenericModelForm):
#     """
#     Use AutocompleteTaggableItems defined in
#     gfk_autocomplete.autocomplete_light_registry.
#     """

#     related = GenericModelMultipleChoiceField(
#         widget=autocomplete_light.MultipleChoiceWidget(
#             'AutocompleteTaggableItems'))

#     class Meta:
#         model = Group


# from django.contrib import admin

# # from models import ModelGroup
# # from forms import ModelGroupForm


# class ModelGroupAdmin(admin.ModelAdmin):
#     form = ModelGroupForm
# admin.site.register(Group, ModelGroupAdmin)
