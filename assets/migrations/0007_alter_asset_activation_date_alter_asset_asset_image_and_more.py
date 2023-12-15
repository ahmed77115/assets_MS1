# Generated by Django 4.2.6 on 2023-11-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_alter_asset_activation_date_alter_asset_barcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='activation_date',
            field=models.DateField(verbose_name='تاريخ الاضافة'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_image',
            field=models.ImageField(default='default.jpeg', upload_to='images/', verbose_name='الصورة'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='barcode',
            field=models.CharField(max_length=100, verbose_name='الباركود'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='maintenance_required',
            field=models.BooleanField(verbose_name='الصيانة مطلوبة'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='quantity',
            field=models.IntegerField(verbose_name='الكمية'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Replacement', 'Replacement')], max_length=100, verbose_name='الحالة'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='القيمة'),
        ),
    ]