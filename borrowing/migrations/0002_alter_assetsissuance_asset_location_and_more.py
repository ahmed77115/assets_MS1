# Generated by Django 4.2.6 on 2023-10-30 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_alter_asset_asset_admin_alter_asset_name_and_more'),
        ('customer', '0002_alter_partner_deletedby_alter_partner_expiry_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('borrowing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetsissuance',
            name='asset_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='assets.location'),
        ),
        migrations.AlterField(
            model_name='assetsissuance',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='deletedby'),
        ),
        migrations.AlterField(
            model_name='assetsissuance',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='modifiedby'),
        ),
        migrations.AlterField(
            model_name='assetsissuance',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='OWner'),
        ),
        migrations.AlterField(
            model_name='assetsissuance',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.partner'),
        ),
        migrations.AlterField(
            model_name='assetsissuance',
            name='return_condition',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assetsissuance',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
