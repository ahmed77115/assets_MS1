from . import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from .admin import RentalAdmin,CountryAutocompleteFromList
from .views import some_view
from django.contrib.auth import views as auth_views


urlpatterns = [

   path(
        'ahmed/',
        views.Ahmed.as_view(),
        name='ahmed',
    ),
    # path('',some_view,name='sasa'),
    path('RentalAdmin', RentalAdmin,name='RentalAdmin'),
    path('UserJson', views.UserJson.as_view(),name='UserJson'),
    path('UserView', views.UserView.as_view(),name='UserView'),

    path('OfficeJson', views.OfficeJson.as_view(),name='OfficeJson'),
    path('OfficeView', views.OfficeView.as_view(),name='OfficeView'),
    # path('DelvryJson', views.DelvryJson.as_view(),name='DelvryJson'),
    # path('DelvryView', views.DelvryView.as_view(),name='DelvryView'),
    # path('ParcelJson', views.ParcelJson.as_view(),name='ParcelJson'),
    # path('ParcelView', views.ParcelView.as_view(),name='ParcelView'),
    # url('country_list_autocomplete', CountryAutocompleteFromList.as_view(),name='country_list_autocomplete'),

    # path('', views.IndexView.as_view(), name='/index/'),
    # url(
    #     'test-autocomplete/$',
    #     autocomplete.Select2QuerySetView.as_view(model=TypeOfCourse),
    #     name='select2_fk',
    # ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
