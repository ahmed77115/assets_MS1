


from django.shortcuts import render
from .forms import UserForm,OfficeForm
from django.http import HttpResponse
from .models import Office
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
# from datatableview.views import DatatableView
from django_datatables_view.base_datatable_view import  BaseDatatableView


class Ahmed(CreateView):
    def get(self, request, *args, **kwargs):
        print("dsfsdsdfsdfdfffffffffffffffffffffffffffffffffffffff")

        return JsonResponse({"data":{"email":"shfjshfkjdsfhksd"}})


# Create your views here.
class UserView(CreateView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.GET.keys():
            if request.GET.get('id'):
                try:
                    formdata = User.objects.filter(pk=int(request.GET.get('id')))
                    result = {"status": 1, "data": serializers.serialize('json',formdata)}
                    return JsonResponse(result)
                except:
                    result = {'status':0,'data':'error show the data for edit it'}
        else:
            context = {'form': UserForm(request.GET or None),
                    'title': _('User Data'),
                    'url':reverse('UserView'),
                    'urljson':reverse('UserJson'),

                    }
            return render(request, 'user.html', context)

    def post(self, request, *args, **kwargs):
        

        form = UserForm(request.POST, request.FILES)
        
       
        if request.POST.get('id'):
            data_form = get_object_or_404(User,pk=int(request.POST.get('id')))
            form = UserForm(request.POST, instance=data_form)
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
        pk = int(QueryDict(request.body).get('id'))
        if pk:
            try:
                data = get_object_or_404(User,pk=int(pk))
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



class UserJson(BaseDatatableView):
    from django.contrib.auth import get_user_model
    # User = get_user_model()
    model = get_user_model()
    columns =[
        'id',
        'username',
        'first_name',
        'last_name',
        'email',   
        'action',
    ]
    order_columns=[
        'id',
        'username',
        'first_name',
        'last_name',
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
                'title="{3}"><i class= "fas fa-trash fa-2x " style="color:red"  ></i></a>'.format(row.pk,"Edit",reverse('UserView'),"delete")
            
        else:
            return super(UserJson, self).render_column(row, column)
    def filter_queryset(self, qs):
        search = self.request.GET.get('sSearch')
        if search:
            qs = qs.filter(Q(email__icontains=search) | Q(id__icontains=search) 
            | Q(id__icontains=search))
        return qs



class OfficeView(CreateView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.GET.keys():
            if request.GET.get('id'):
                try:
                    formdata = Office.objects.filter(pk=int(request.GET.get('id')))
                    result = {"status": 1, "data": serializers.serialize('json',formdata)}
                    return JsonResponse(result)
                except:
                    result = {'status':0,'data':'error show the data for edit it'}
        else:
            context = {'form': OfficeForm(request.GET or None),
                    'title': _('Office Data'),
                    'url':reverse('OfficeView'),
                    'urljson':reverse('OfficeJson'),
                    }
            return render(request, 'office.html', context)

    def post(self, request, *args, **kwargs):
        

        form = OfficeForm(request.POST, request.FILES)
        
       
        if request.POST.get('id'):
            data_form = get_object_or_404(Office,pk=int(request.POST.get('id')))
            form = OfficeForm(request.POST, instance=data_form)
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
                data = get_object_or_404(Office,pk=int(pk))
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

class OfficeJson(BaseDatatableView):
    model = Office
    columns =[
        'id',
        'office_no',
        'name_office',
        'location',
        'Email',
        
        'office_type',
        'area_service',
        'action',
    ]
    order_columns=[
        'id',
        'office_no',
        'name_office',
        'location',
        'Email',
        
        'office_type',
        'area_service',
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
                'title="{3}"><i class= "fas fa-trash fa-2x " style="color:red"  ></i></a>'.format(row.pk,"Edit",reverse('OfficeView'),"delete")
            
        else:
            return super(OfficeJson, self).render_column(row, column)
    def filter_queryset(self, qs):
        search = self.request.GET.get('sSearch')
        if search:
            qs = qs.filter(Q(name_office__icontains=search) 
            | Q(id__icontains=search)) # )
        return qs
        
# class DelvryView(CreateView):
#     def get(self, request, *args, **kwargs):
#         if 'id' in request.GET.keys():
#             if request.GET.get('id'):
#                 try:
#                     formdata = Delvry.objects.filter(pk=int(request.GET.get('id')))
#                     result = {"status": 1, "data": serializers.serialize('json',formdata)}
#                     return JsonResponse(result)
#                 except:
#                     result = {'status':0,'data':'error show the data for edit it'}
#         else:
#             context = {'form': DelvryForm(request.GET or None),
#                     'title': _('Delvry Data'),
#                     'url':reverse('DelvryView'),
#                     'urljson':reverse('DelvryJson'),
#                     }
#             return render(request, 'Delvry.html', context)

#     def post(self, request, *args, **kwargs):
        

#         form = DelvryForm(request.POST, request.FILES)
        
       
#         if request.POST.get('id'):
#             data_form = get_object_or_404(Delvry,pk=int(request.POST.get('id')))
#             form = DelvryForm(request.POST, instance=data_form)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     obj = form.save(commit=False)
#                     obj.owner_id = 1
#                     obj.save()
#                     if request.GET.get('id'):
#                         if obj.id:
#                             result = {'status':1, 'massage':"the update operation complete successfully"}
#                         else:
#                             result = {'status':2, 'massage':"the update operation  error"}
#                     else:
#                         if obj.id:
#                             result = {'status':1, 'massage':"the save operation complete successfully"}
#                         else:
#                             result = {'status':2, 'massage':"the save operation  error"}
#                     return JsonResponse(result)
#             except Exception as e:
#                 print(str(e))
#                 result = {'status':2, 'message':"message error"}
#             return JsonResponse(result)
#         else:
#             result = {'status':0, 'error_form':form.errors.as_json()}
#             return JsonResponse(result)

#     def delete(self, request, *args, **kwargs):
#         print("ssssssssssssssssssssssssssssssssssssssssssssssssssssss")
#         pk = int(QueryDict(request.body).get('id'))
#         print("ddddddddddddddddddddddd",pk)
#         if pk:
#             try:
#                 data = get_object_or_404(Delvry,pk=int(pk))
#                 data.delete()
#                 msg = _('Deleted Successfulful')
#                 result = {'status':1,'massage':msg}

#             except:
#                 msg = _('Error Deleted ')
#                 result = {'status':0,'massage':msg}
#         else:
#             msg = _('Error Deleted Not Found ID')
#             result = {'status':0,'massage':msg}
#         return JsonResponse(result)

# class DelvryJson(BaseDatatableView):
#     model = Delvry
#     columns =[
#         'id',
#         'customer_number',
#         'customer_type',
#         'Name',
#         'phone_number',
#         'email',
#         'action',
#     ]
#     order_columns=[
#         'id',
#         'customer_number',
#         'customer_type',
#         'Name',
#         'phone_number',
#         'email',
#         'action',
#     ]
#     count=0
#     def render_column(self,row,column):
#         if column=='id':
#             self.count+=1
#             return self.count
#         elif column=="action":
#             # return '<a href="#" class="edit_row" data-url="#" ><i class="fa fa-edit"></i></a>'
#             # return '<button type="button" id="bt">Edit</button>'

#             # return '<a href="#" class="btn btn-success edit" id="{0}" data-toggle="tooltip">Edit</a>'.format(row.id)
#             return '<a class="edit_row" data-url="{2}" data-id="{0}"'\
#                 'style="display: -webkit-inline-box;" data-toggle="tooltip"'\
#                 'title="{1}">  <i class= "fa fa-edit fa-2x" ></i></a>'\
#                 '&ensp;&ensp;<a class="delete_row" data-url="{2}" data-id="{0}"'\
#                 'style="display: -webkit-inline-box;" data-toggle="tooltip"'\
#                 'title="{3}"><i class= "fas fa-trash fa-2x " style="color:red"  ></i></a>'.format(row.pk,"Edit",reverse('DelvryView'),"delete")
            
#         else:
#             return super(DelvryJson, self).render_column(row, column)
#     def filter_queryset(self, qs):
#         search = self.request.GET.get('sSearch')
#         if search:
#             qs = qs.filter(Q(email__icontains=search) | Q(Name__icontains=search) 
#             | Q(id__icontains=search)) # )
#         return qs



# class ParcelView(CreateView):
#     def get(self, request, *args, **kwargs):
#         if 'id' in request.GET.keys():
#             if request.GET.get('id'):
#                 try:
#                     formdata = Parcel.objects.filter(pk=int(request.GET.get('id')))
#                     result = {"status": 1, "data": serializers.serialize('json',formdata)}
#                     return JsonResponse(result)
#                 except:
#                     result = {'status':0,'data':'error show the data for edit it'}
#         else:
#             context = {'form': ParcelForm(request.GET or None),
#                     'title': _('Parcel Data'),
#                     'url':reverse('ParcelView'),
#                     'urljson':reverse('ParcelJson'),
#                     }
#             return render(request, 'Parcel.html', context)

#     def post(self, request, *args, **kwargs):
        

#         form = ParcelForm(request.POST, request.FILES)
        
       
#         if request.POST.get('id'):
#             data_form = get_object_or_404(Parcel,pk=int(request.POST.get('id')))
#             form = ParcelForm(request.POST, instance=data_form)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     obj = form.save(commit=False)
#                     obj.owner_id = 1
#                     obj.save()
#                     if request.GET.get('id'):
#                         if obj.id:
#                             result = {'status':1, 'massage':"the update operation complete successfully"}
#                         else:
#                             result = {'status':2, 'massage':"the update operation  error"}
#                     else:
#                         if obj.id:
#                             result = {'status':1, 'massage':"the save operation complete successfully"}
#                         else:
#                             result = {'status':2, 'massage':"the save operation  error"}
#                     return JsonResponse(result)
#             except Exception as e:
#                 print(str(e))
#                 result = {'status':2, 'message':"message error"}
#             return JsonResponse(result)
#         else:
#             result = {'status':0, 'error_form':form.errors.as_json()}
#             return JsonResponse(result)

#     def delete(self, request, *args, **kwargs):
#         print("ssssssssssssssssssssssssssssssssssssssssssssssssssssss")
#         pk = int(QueryDict(request.body).get('id'))
#         print("ddddddddddddddddddddddd",pk)
#         if pk:
#             try:
#                 data = get_object_or_404(Parcel,pk=int(pk))
#                 data.delete()
#                 msg = _('Deleted Successfulful')
#                 result = {'status':1,'massage':msg}

#             except:
#                 msg = _('Error Deleted ')
#                 result = {'status':0,'massage':msg}
#         else:
#             msg = _('Error Deleted Not Found ID')
#             result = {'status':0,'massage':msg}
#         return JsonResponse(result)



# class ParcelJson(BaseDatatableView):
#     model = Parcel
#     columns =[
#         'id',
#         'customer_number',
#         'customer_type',
#         'Name',
#         'phone_number',
#         'email',
#         'action',
#     ]
#     order_columns=[
#         'id',
#         'customer_number',
#         'customer_type',
#         'Name',
#         'phone_number',
#         'email',
#         'action',
#     ]
#     count=0
#     def render_column(self,row,column):
#         if column=='id':
#             self.count+=1
#             return self.count
#         elif column=="action":
#             # return '<a href="#" class="edit_row" data-url="#" ><i class="fa fa-edit"></i></a>'
#             # return '<button type="button" id="bt">Edit</button>'

#             # return '<a href="#" class="btn btn-success edit" id="{0}" data-toggle="tooltip">Edit</a>'.format(row.id)
#             return '<a class="edit_row" data-url="{2}" data-id="{0}"'\
#                 'style="display: -webkit-inline-box;" data-toggle="tooltip"'\
#                 'title="{1}">  <i class= "fa fa-edit fa-2x" ></i></a>'\
#                 '&ensp;&ensp;<a class="delete_row" data-url="{2}" data-id="{0}"'\
#                 'style="display: -webkit-inline-box;" data-toggle="tooltip"'\
#                 'title="{3}"><i class= "fas fa-trash fa-2x " style="color:red"  ></i></a>'.format(row.pk,"Edit",reverse('ParcelView'),"delete")
            
#         else:
#             return super(ParcelJson, self).render_column(row, column)
#     def filter_queryset(self, qs):
#         search = self.request.GET.get('sSearch')
#         if search:
#             qs = qs.filter(Q(email__icontains=search) | Q(Name__icontains=search) 
#             | Q(id__icontains=search)) # )
#         return qs


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.utils.functional import Promise


# def render(request, template_name, context=None, content_type=None, status=None, using=None):
#     """
#     Return a HttpResponse whose content is filled with the result of calling
#     django.template.loader.render_to_string() with the passed arguments.
#     """
#     content = loader.render_to_string(template_name, context, request, using=using)
#     return HttpResponse(content, content_type, status)


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    context = {'form': OfficeForm(request.GET or None),
            'title': _('Office Data'),
            # 'url':reverse('OfficeView'),
            # 'urljson':reverse('OfficeJson'),
            }
    content = loader.render_to_string('office.html', context, request, using=None)
    # ww= render(request, 'office.html', context)
    print("#"*100)
    print("#"*100)
    print(content)
    print("#"*100)
    print("#"*100)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    from django.utils.html import format_html
    p.drawString(200,0, (((content))))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
#######################################
################################
    from markdown import markdown
    import pdfkit

    # input_filename = 'README.md'
    output_filename = 'README.pdf'

    # with open(input_filename, 'r') as f:
    #     html_text = markdown(f.read(), output_format='html4')

    options = {
        'page-size': 'Letter',
        'margin-top': '0.25in',
        'margin-right': '0.25in',
        'margin-bottom': '0.25in',
        'margin-left': '0.25in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    try:
        config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
# p   dfkit.from_string(html, 'MyPDF.pdf', configuration=config)
        print(reverse('UserView'))

        pdfkit.from_url('http://127.0.0.1:8000/branch/shipping/storemovement/', 'output_filename.pdf', options=options,configuration=config)
    except Exception as e:
        print(e)

        print("fffffffffffff")



    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')



from wkhtmltopdf.views import PDFTemplateView


class MyPDF(PDFTemplateView):
    # filename = 'my_pdf.pdf'
    template_name = 'office.html'
    cmd_options = {
        'margin-top': 3,
    }