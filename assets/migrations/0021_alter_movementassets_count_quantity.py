# Generated by Django 4.2.7 on 2023-12-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0020_movementassets_count_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movementassets',
            name='count_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='الكمية المحسوبة'),
        ),
    ]
