# Generated by Django 4.2.6 on 2023-11-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_alter_asset_activation_date_alter_asset_asset_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='activation_date',
            field=models.DateField(verbose_name='تاريخ التفعيل'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_admin',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='مسؤول الأصل'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='borrow_able',
            field=models.BooleanField(verbose_name='جاهزللأعارة'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='creation_date',
            field=models.DateField(verbose_name='تاريخ الاضافة'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='usage_period',
            field=models.CharField(max_length=100, verbose_name='فترة الأستخدام'),
        ),
    ]