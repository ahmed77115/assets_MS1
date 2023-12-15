from django.db import models

# Create your models here.


class Location(models.Model):
    location_number = models.IntegerField()
    university_number = models.IntegerField()
    barcode = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    asset_number = models.IntegerField()
    location_type = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    site_status = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Locations'

class University(models.Model):
    university_number = models.IntegerField()
    university_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    student_count = models.IntegerField()
    faculty_count = models.IntegerField()
    maintenance_required = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Universities'

class Asset(models.Model):
    asset_number = models.IntegerField()
    asset_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    student_count = models.IntegerField()
    faculty_count = models.IntegerField()
    maintenance_required = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Universities'

class Asset(models.Model):
    asset_number = models.IntegerField()
    asset_name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=100)
    asset_status = models.CharField(max_length=100)
    asset_quantity = models.IntegerField()
    asset_value = models.FloatField()
    date_added = models.DateField()
    department = models.CharField(max_length=100)
    asset_admin = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Assets'






