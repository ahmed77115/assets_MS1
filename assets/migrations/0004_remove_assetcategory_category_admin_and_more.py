# Generated by Django 4.2.6 on 2023-11-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_alter_asset_asset_admin_alter_asset_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetcategory',
            name='category_admin',
        ),
        migrations.AlterField(
            model_name='assetcategory',
            name='description',
            field=models.CharField(max_length=100, verbose_name='الوصف'),
        ),
        migrations.AlterField(
            model_name='assetcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='الاسم'),
        ),
    ]
