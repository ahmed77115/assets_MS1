# Generated by Django 4.2.6 on 2023-12-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movement', '0017_alter_stockdetails_options_remove_stockdetails_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockdetails',
            options={'verbose_name': 'تفاصيل الجرد', 'verbose_name_plural': ' جرد الأصول'},
        ),
        migrations.AddField(
            model_name='stockdetails',
            name='new_recipient',
            field=models.CharField(default=1, max_length=100, verbose_name='المستلم الجديد'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='barcode',
            field=models.IntegerField(blank=True, null=True, verbose_name='رقم الباركود'),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='recipient',
            field=models.CharField(max_length=100, verbose_name='المستلم '),
        ),
    ]
