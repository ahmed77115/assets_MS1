from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    AdminPasswordChangeForm ,
    UserChangeForm as U_Ch_F,
    UserCreationForm as U_Cr_F,
)
from django.contrib.auth.models import Group


from base.models import User,University
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.utils.translation import gettext, gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())
from dal import autocomplete
# from delivery_agents.models import OfficeTransport

class UserCreationForm(U_Cr_F,autocomplete.FutureModelForm):

    # user_office = autocomplete.Select2GenericForeignKeyModelField(
    #     # Model with values to filter, linked with the name field
    #     model_choice=[(OfficeArea, 'id',[('type_user','type_user')]),
    #                 #   (OfficeTransport, 'id',[('type_user','type_user')]),
    #     # model_choice=[(OfficeArea, 'id', [('language', 'spoken_language'),]),
    #                   (University, 'id')],
    #                   required=False,
    # )

    class Meta(U_Cr_F.Meta,autocomplete.FutureModelForm):
        pass


class UserChangeForm(U_Ch_F,autocomplete.FutureModelForm):

    # user_office = autocomplete.Select2GenericForeignKeyModelField(
    #     # Model with values to filter, linked with the name field

    #     model_choice=[(OfficeArea, 'id',[('type_user','type_user')]),
    #                 #   (OfficeTransport, 'id',[('type_user','type_user')]),
    #     # model_choice=[(OfficeArea, 'id', [('language', 'spoken_language'),]),
    #                   (University, 'id')],
    #                   required=False,
    # )

    class Meta(U_Cr_F.Meta,autocomplete.FutureModelForm):
        pass



# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     search_fields = ('name',)
#     ordering = ('name',)
#     filter_horizontal = ('permissions',)

#     def formfield_for_manytomany(self, db_field, request=None, **kwargs):
#         if db_field.name == 'permissions':
#             qs = kwargs.get('queryset', db_field.remote_field.model.objects)
#             # Avoid a major performance hit resolving permission names which
#             # triggers a content_type load:
#             kwargs['queryset'] = qs.select_related('content_type')
#         return super().formfield_for_manytomany(db_field, request=request, **kwargs)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
# createdat
# modifiedat
# owner
# modifiedby
# deletedby
# deletedat
# deleted
# type_user
# phone
# is_manager
# object_id
    fieldsets = (
        (_(' معلومات اساسيه'), {'fields': ('username', 'password',)}),
        (_(' معلومات شخصية'), {'fields': ('first_name', 'last_name', 'email',)}),
        (_('الصلاحيات'), {
            'fields': ('is_active', 'is_staff', 'is_superuser','is_manager', 'groups', 'user_permissions'),
        }),
        (_('تواريخ مهمة '), {'fields': ('last_login', 'date_joined')}),
    )

    fieldsets_office = (
         (_(' معلومات اساسيه'), {'fields': ('username', 'password',)}),
           (_(' معلومات شخصية'), {'fields': ('first_name', 'last_name', 'email',)}),
        (_('الصلاحيات'), {
            'fields': ('is_active', 'is_staff','is_manager', 'groups', 'user_permissions'),
        }),
        (_('تواريخ مهمة '), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',),
        }),
    )
    add_fieldsets_office = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',),
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('username','first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    # autocomplete_fields = ()
    # def get_fieldsets(self, request, obj=None):
    #     if not obj:
    #         # if request.user.user_office == None:

    #         #     return self.add_fieldsets
    #         if request.user.content_type.model_class()== University:
    #             return self.add_fieldsets_office
    #         # elif request.user.content_type.model_class()== OfficeTransport:
    #         #     return self.add_fieldsets_office
    #         else:
    #             return self.add_fieldsets
        # if request.user.user_office:
        #     if request.user.content_type.model_class()== University:
        #         return self.fieldsets_office

        #     # elif request.user.content_type.model_class()== OfficeTransport:
        #     #     return self.fieldsets_office
        #     else:
        #         return super().get_fieldsets(request, obj)

        # else:
        #     return super().get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def get_urls(self):
        return [
            path(
                '<id>/password/',
                self.admin_site.admin_view(self.user_change_password),
                name='auth_user_password_change',
            ),
        ] + super().get_urls()

    def lookup_allowed(self, lookup, value):
        # Don't allow lookups involving passwords.
        return not lookup.startswith('password') and super().lookup_allowed(lookup, value)

    @sensitive_post_parameters_m
    @csrf_protect_m
    def add_view(self, request, form_url='', extra_context=None):
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._add_view(request, form_url, extra_context)

    def _add_view(self, request, form_url='', extra_context=None):
        # It's an error for a user to have add permission but NOT change
        # permission for users. If we allowed such users to add users, they
        # could create superusers, which would mean they would essentially have
        # the permission to change users. To avoid the problem entirely, we
        # disallow users from adding users if they don't have change
        # permission.
        if not self.has_change_permission(request):
            if self.has_add_permission(request) and settings.DEBUG:
                # Raise Http404 in debug mode so that the user gets a helpful
                # error message.
                raise Http404(
                    'Your user does not have the "Change user" permission. In '
                    'order to add users, Django requires that your user '
                    'account have both the "Add user" and "Change user" '
                    'permissions set.')
            raise PermissionDenied
        if extra_context is None:
            extra_context = {}
        username_field = self.model._meta.get_field(self.model.USERNAME_FIELD)
        defaults = {
            'auto_populated_fields': (),
            'username_help_text': username_field.help_text,
        }
        extra_context.update(defaults)
        return super().add_view(request, form_url, extra_context)

    @sensitive_post_parameters_m
    def user_change_password(self, request, id, form_url=''):
        user = self.get_object(request, unquote(id))
        if not self.has_change_permission(request, user):
            raise PermissionDenied
        if user is None:
            raise Http404(_('%(name)s object with primary key %(key)r does not exist.') % {
                'name': self.model._meta.verbose_name,
                'key': escape(id),
            })
        if request.method == 'POST':
            form = self.change_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                change_message = self.construct_change_message(request, form, None)
                self.log_change(request, user, change_message)
                msg = gettext('Password changed successfully.')
                messages.success(request, msg)
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect(
                    reverse(
                        '%s:%s_%s_change' % (
                            self.admin_site.name,
                            user._meta.app_label,
                            user._meta.model_name,
                        ),
                        args=(user.pk,),
                    )
                )
        else:
            form = self.change_password_form(user)

        fieldsets = [(None, {'fields': list(form.base_fields)})]
        adminForm = admin.helpers.AdminForm(form, fieldsets, {})

        context = {
            'title': _('Change password: %s') % escape(user.get_username()),
            'adminForm': adminForm,
            'form_url': form_url,
            'form': form,
            'is_popup': (IS_POPUP_VAR in request.POST or
                         IS_POPUP_VAR in request.GET),
            'add': True,
            'change': False,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_absolute_url': False,
            'opts': self.model._meta,
            'original': user,
            'save_as': False,
            'show_save': True,
            **self.admin_site.each_context(request),
        }

        request.current_app = self.admin_site.name

        return TemplateResponse(
            request,
            self.change_user_password_template or
            'admin/auth/user/change_password.html',
            context,
        )

    def response_add(self, request, obj, post_url_continue=None):
        """
        Determine the HttpResponse for the add_view stage. It mostly defers to
        its superclass implementation but is customized because the User model
        has a slightly different workflow.
        """
        # We should allow further modification of the user just added i.e. the
        # 'Save' button should behave like the 'Save and continue editing'
        # button except in two scenarios:
        # * The user has pressed the 'Save and add another' button
        # * We are adding a user in a popup
        if '_addanother' not in request.POST and IS_POPUP_VAR not in request.POST:
            request.POST = request.POST.copy()
            request.POST['_continue'] = 1
        return super().response_add(request, obj, post_url_continue)


    # def save_model(self, request, obj, form, change):
    #     # print(request.__dict__)
    #     # if request.user.type_user 
    #     if change:
    #         obj.modifiedby = request.user
    #     else:
    #         obj.owner = request.user
    #     if request.user.user_office:
    #         if request.user.content_type.model_class()== University:
    #             obj.user_office = request.user.user_office
    #             obj.type_user = '3'
    #         # elif request.user.content_type.model_class()== OfficeTransport:
    #         #     obj.user_office = request.user.user_office
    #         #     obj.type_user = '4'
                    
    #     super().save_model(request, obj, form, change)
    
    
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

        try:
            qs = self.model._default_manager.get_queryset(user=request.user)
        except Exception as e:
            pass
        # qs = self.model.yobjects.get_queryset(request.user)
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs



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
    #             print("#"*111)
    #             print("in get_field_queryset with related_admin",db_field)
                
    #             return db_field.remote_field.model._default_manager.using(db).order_by(*ordering)
    #     print("#"*111)
    #     print("in get_field_queryset ",db_field)
    #     return db_field.remote_field.model._default_manager.get_queryset(user=request.user).using(db)
    #     return None

