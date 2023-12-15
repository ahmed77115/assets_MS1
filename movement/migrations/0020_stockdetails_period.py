# Generated by Django 4.2.6 on 2023-12-11 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('periods', '0003_alter_period_options'),
        ('movement', '0019_remove_stockdetails_period_maindata'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdetails',
            name='period',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='periods.period', verbose_name='الفترة'),
            preserve_default=False,
        ),
    ]
