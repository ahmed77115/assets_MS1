from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_init_MovementType(sender, **kwargs):

    from .models import MovementType
    MovementType.objects.update_or_create(
        defaults={
        "source_location": None,
        "target_location": None,},
        **{"name": "أضافة اصل",
        "type":1,
                }
        
        )
    MovementType.objects.update_or_create(
        defaults={
        "source_location": None,
        "target_location": None,},
        **{"name": "أستعارة اصل",
        "type":2,
                }
        
        )
    MovementType.objects.update_or_create(
        defaults={
        "source_location": None,
        "target_location": None,},
        **{"name": "نقل اصل",
        "type":3,
                }
        
        )
    MovementType.objects.update_or_create(
        defaults={
        "source_location": None,
        "target_location": None,},
        **{"name": "صيانة اصل",
        "type":4,
                }
        
        )
    MovementType.objects.update_or_create(
        defaults={
        "source_location": None,
        "target_location": None,},
        **{"name": "شراء اصل",
        "type":5,
                }
        
        )
    MovementType.objects.update_or_create(
        defaults={
        "source_location": None,
        "target_location": None,},
        **{"name": "بيع اصل",
        "type":6,
                }
        
        )
    MovementType.objects.update_or_create(
        defaults={
        "source_location": None,
        "target_location": None,},
        **{"name": "تسوية اصل",
        "type":7,
                }
        
        )
    