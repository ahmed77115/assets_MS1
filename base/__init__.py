# class UserView(CreateView):
#     def get(self, request, *args, **kwargs):
#         if 'id' in request.GET.keys():
#             if request.GET.get('id'):
#                 try:
#                     formdata = User.objects.filter(pk=int(request.GET.get('id')))
#                     result = {"status": 1, "data": serializers.serialize('json',formdata)}
#                     return JsonResponse(result)
#                 except:
#                     result = {'status':0,'data':'error show the data for edit it'}
#         else:
#             context = {'form': UserForm(request.GET or None),
#                     'title': _('User Data'),
#                     'url':reverse('UserView'),
#                     }
#             return render(request, 'user.html', context)

#     def post(self, request, *args, **kwargs):
        

#         form = UserForm(request.POST, request.FILES)
        
       
#         if request.POST.get('id'):
#             data_form = get_object_or_404(User,pk=int(request.POST.get('id')))
#             form = UserForm(request.POST, instance=data_form)
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
#         pk = int(QueryDict(request.body).get('id'))
#         if pk:
#             try:
#                 data = get_object_or_404(User,pk=int(pk))
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



# class UserJson(BaseDatatableView):
#     model = User
#     columns =[
#         'id',

#         'action',
#     ]
#     order_columns=[
#         'id',
        
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
#                 'title="{3}"><i class= "fas fa-trash fa-2x " style="color:red"  ></i></a>'.format(row.pk,"Edit",reverse('UserView'),"delete")
            
#         else:
#             return super(UserJson, self).render_column(row, column)
#     def filter_queryset(self, qs):
#         search = self.request.GET.get('sSearch')
#         if search:
#             qs = qs.filter(Q(email__icontains=search) | Q(id__icontains=search) 
#             | Q(id__icontains=search)) # )
#         return qs
