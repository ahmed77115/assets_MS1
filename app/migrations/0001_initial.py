# Generated by Django 4.2.6 on 2023-11-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_number', models.IntegerField()),
                ('asset_name', models.CharField(max_length=100)),
                ('asset_type', models.CharField(max_length=100)),
                ('asset_status', models.CharField(max_length=100)),
                ('asset_quantity', models.IntegerField()),
                ('asset_value', models.FloatField()),
                ('date_added', models.DateField()),
                ('department', models.CharField(max_length=100)),
                ('asset_admin', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_number', models.IntegerField()),
                ('university_number', models.IntegerField()),
                ('barcode', models.CharField(max_length=100)),
                ('location_name', models.CharField(max_length=100)),
                ('university_name', models.CharField(max_length=100)),
                ('asset_number', models.IntegerField()),
                ('location_type', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('site_status', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_number', models.IntegerField()),
                ('university_name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('student_count', models.IntegerField()),
                ('faculty_count', models.IntegerField()),
                ('maintenance_required', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Universities',
            },
        ),
    ]
