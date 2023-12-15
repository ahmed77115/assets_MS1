# Generated by Django 4.2.6 on 2023-11-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_assetcategory_category_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='activation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='asset',
            name='barcode',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Replacement', 'Replacement')], max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]