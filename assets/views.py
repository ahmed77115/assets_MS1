from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from.models import Asset

# Create your views here.
def get_asset(request):
    asset=Asset.objects.all()
    return render(request,'assets/asset.html',{'asset':asset})
def about(request):
    return render(request,'pages/about.html',{})
