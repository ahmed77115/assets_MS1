# Generated by Django 4.2.6 on 2023-12-06 18:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0017_alter_movementassets_employee'),
        ('periods', '0002_alter_period_options_alter_perioddetail_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movement', '0013_stodetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stodetails',
            new_name='StockDetails',
        ),
    ]
