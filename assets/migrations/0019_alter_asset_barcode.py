# Generated by Django 4.2.6 on 2023-12-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0018_alter_asset_barcode_alter_asset_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='barcode',
            field=models.IntegerField(blank=True, null=True, verbose_name='رقم الباركود'),
        ),
    ]
