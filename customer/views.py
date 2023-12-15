from django_datatables_view.base_datatable_view import  BaseDatatableView
from django.http import HttpResponse
from django.views.generic import CreateView
from django.http import HttpResponse ,JsonResponse ,QueryDict
from django.shortcuts import render , redirect, get_object_or_404
from django.contrib import messages
from django.forms import formset_factory,modelformset_factory
from django.core import serializers
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.contrib.auth.models import User, Group, ContentType, Permission
from django.db.models import Q
from django.db import transaction
from django.urls import reverse
from dal import autocomplete
from .models import Customer,CustomerAddress
from .forms import CustomerForm
class CustomerView(CreateView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.GET.keys():
            if request.GET.get('id'):
                try:
                    formdata = Customer.objects.filter(pk=int(request.GET.get('id')))
                    result = {"status": 1, "data": serializers.serialize('json',formdata)}
                    return JsonResponse(result)
                except:
                    result = {'status':0,'data':'error show the data for edit it'}
        else:
            context = {'form': CustomerForm(request.GET or None),
                    'title': _('Customer Data'),
                    'url':reverse('CustomerView'),
                    }
            return render(request, 'customer.html', context)

    def post(self, request, *args, **kwargs):
        

        form = CustomerForm(request.POST, request.FILES)
        
       
        if request.POST.get('id'):
            data_form = get_object_or_404(Customer,pk=int(request.POST.get('id')))
            form = CustomerForm(request.POST, instance=data_form)
        if form.is_valid():
            try:
                with transaction.atomic():
                    obj = form.save(commit=False)
                    obj.owner_id = 1
                    obj.save()
                    if request.GET.get('id'):
                        if obj.id:
                            result = {'status':1, 'massage':"the update operation complete successfully"}
                        else:
                            result = {'status':2, 'massage':"the update operation  error"}
                    else:
                        if obj.id:
                            result = {'status':1, 'massage':"the save operation complete successfully"}
                        else:
                            result = {'status':2, 'massage':"the save operation  error"}
                    return JsonResponse(result)
            except Exception as e:
                print(str(e))
                result = {'status':2, 'message':"message error"}
            return JsonResponse(result)
        else:
            result = {'status':0, 'error_form':form.errors.as_json()}
            return JsonResponse(result)

    def delete(self, request, *args, **kwargs):
        print("ssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        pk = int(QueryDict(request.body).get('id'))
        print("ddddddddddddddddddddddd",pk)
        if pk:
            try:
                data = get_object_or_404(Customer,pk=int(pk))
                data.delete()
                msg = _('Deleted Successfulful')
                result = {'status':1,'massage':msg}

            except:
                msg = _('Error Deleted ')
                result = {'status':0,'massage':msg}
        else:
            msg = _('Error Deleted Not Found ID')
            result = {'status':0,'massage':msg}
        return JsonResponse(result)


class CustomerJson(BaseDatatableView):
    model = Customer
    columns =[
        'id',
        'customer_number',
        'customer_type',
        'Name',
        'phone_number',
        'email',
        'action',
    ]
    order_columns=[
        'id',
        'customer_number',
        'customer_type',
        'Name',
        'phone_number',
        'email',
        'action',
    ]
    count=0
    def render_column(self,row,column):
        if column=='id':
            self.count+=1
            return self.count
        elif column=="action":
            # return '<a href="#" class="edit_row" data-url="#" ><i class="fa fa-edit"></i></a>'
            # return '<button type="button" id="bt">Edit</button>'

            # return '<a href="#" class="btn btn-success edit" id="{0}" data-toggle="tooltip">Edit</a>'.format(row.id)
            return '<a class="edit_row" data-url="{2}" data-id="{0}"'\
                'style="display: -webkit-inline-box;" data-toggle="tooltip"'\
                'title="{1}">  <i class= "fa fa-edit fa-2x" ></i></a>'\
                '&ensp;&ensp;<a class="delete_row" data-url="{2}" data-id="{0}"'\
                'style="display: -webkit-inline-box;" data-toggle="tooltip"'\
                'title="{3}"><i class= "fas fa-trash fa-2x " style="color:red"  ></i></a>'.format(row.pk,"Edit",reverse('CustomerView'),"delete")
            
        else:
            return super(CustomerJson, self).render_column(row, column)
    def filter_queryset(self, qs):
        search = self.request.GET.get('sSearch')
        if search:
            qs = qs.filter(Q(email__icontains=search) | Q(Name__icontains=search) 
            | Q(id__icontains=search)) # )
        return qs


