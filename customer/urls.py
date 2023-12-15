from . import views
from django.urls import path
# from django.conf.urls import url


urlpatterns = [
    path('CustomerJson', views.CustomerJson.as_view(),name='CustomerJson'),
    path('CustomerView', views.CustomerView.as_view(),name='CustomerView'),
]