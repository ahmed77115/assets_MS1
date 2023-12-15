from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.admin import AdminSite
from base.models import Address,User
from base.admin import BaseModelAdmin,BaseStackedInline,BaseTabularInline
from django.contrib.contenttypes.admin import GenericTabularInline,GenericStackedInline


# Managing freight offices
class FreightAdmin(AdminSite):
    site_header = _("Managing freight offices")
    site_title = "Managing freight offices Portal"
    index_title = "Welcome to Managing freight offices portal"

delivry_admin = FreightAdmin(name='delivry')



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
                if request.user.content_type.model_class()== OfficeTransport:
                    return db_field.remote_field.model._default_manager.get_queryset(request.user).filter(pk=request.user.user_office.pk).using(db)
        return super().get_field_queryset(db,db_field, request=request)
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

