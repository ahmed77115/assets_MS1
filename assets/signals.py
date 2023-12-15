from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_init_location(sender, **kwargs):

    from .models import Location
    Location.objects.update_or_create(
        defaults={
        "is_group": False,
        "area":0 ,
        "parent": None,
        "university": None,},
        **{"name": "الافتتاحي",
        "location_type":"7" ,
        "description":"الافتتاجي المخزون" ,
             }
        
        )
    Location.objects.update_or_create(
defaults={
        "is_group": False,
        "area":0 ,
        "parent": None,
        "university": None,},
        **{"name": "عملاء",
        "location_type":"2" ,
        "description":" عملاء" ,
             }
   
        )
    Location.objects.update_or_create(
defaults={
        "is_group": False,
        "area":0 ,
        "parent": None,
        "university": None,},
        **{"name": "موردين",
        "location_type":"5" ,
        "description":" موردين" ,
        }

        )
    Location.objects.update_or_create(
defaults={
        "is_group": False,
        "area":0 ,
        "parent": None,
        "university": None,},
        **{"name": "صيانه",
        "location_type":"6" ,
        "description":" صيانه" ,
      }
        )
    Location.objects.update_or_create(
defaults={
        "is_group": False,
        "area":0 ,
        "parent": None,
        "university": None,},
        **{"name": "الاصول المفقودة والزائدة",
        "location_type":"4" ,
        "description":"الاصول المفقودة والزائدة" ,
      }
        )
