from django.utils import timezone
from django.db import models

from assets.models import Asset, Location
from base.models import BaseModel, UniversityBaseModel, User
from customer.models import Partner

# Create your models here.




class AssetsIssuance(UniversityBaseModel):
    asset=models.ForeignKey(Asset,on_delete=models.PROTECT)
    asset_location=models.ForeignKey(Location,on_delete=models.PROTECT,blank=True,null=True)
    # date_issued = models.DateTimeField(default=timezone.now)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE,null=True,blank=True)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    checkout_condition = models.TextField()
    return_condition = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.asset

