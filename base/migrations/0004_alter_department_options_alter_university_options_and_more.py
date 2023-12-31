# Generated by Django 4.2.6 on 2023-11-18 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_address_address_line_alter_address_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'الاقسام', 'verbose_name_plural': 'الاقسام'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'الجامعة', 'verbose_name_plural': 'الجامغة'},
        ),
        migrations.AlterModelManagers(
            name='university',
            managers=[
                ('_tree_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='createdat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ الانشاء'),
        ),
        migrations.AlterField(
            model_name='address',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='هل حذف'),
        ),
        migrations.AlterField(
            model_name='address',
            name='deletedat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ الحذف'),
        ),
        migrations.AlterField(
            model_name='address',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='حذفه '),
        ),
        migrations.AlterField(
            model_name='address',
            name='location',
            field=models.CharField(max_length=50, verbose_name='الموقع'),
        ),
        migrations.AlterField(
            model_name='address',
            name='modifiedat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ التعديل'),
        ),
        migrations.AlterField(
            model_name='address',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='عدله '),
        ),
        migrations.AlterField(
            model_name='address',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='انشائه '),
        ),
        migrations.AlterField(
            model_name='department',
            name='createdat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ الانشاء'),
        ),
        migrations.AlterField(
            model_name='department',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='هل حذف'),
        ),
        migrations.AlterField(
            model_name='department',
            name='deletedat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ الحذف'),
        ),
        migrations.AlterField(
            model_name='department',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='حذفه '),
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(verbose_name='الوصف'),
        ),
        migrations.AlterField(
            model_name='department',
            name='modifiedat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ التعديل'),
        ),
        migrations.AlterField(
            model_name='department',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='عدله '),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='department',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='انشائه '),
        ),
        migrations.AlterField(
            model_name='department',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to='base.university', verbose_name='الجامعة'),
        ),
        migrations.AlterField(
            model_name='university',
            name='address',
            field=models.CharField(max_length=100, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='university',
            name='createdat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ الأنشاء'),
        ),
        migrations.AlterField(
            model_name='university',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='هل محذوف'),
        ),
        migrations.AlterField(
            model_name='university',
            name='deletedat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ الحذف'),
        ),
        migrations.AlterField(
            model_name='university',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='عدله'),
        ),
        migrations.AlterField(
            model_name='university',
            name='modifiedat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ التعديل'),
        ),
        migrations.AlterField(
            model_name='university',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='حذف'),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=100, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='university',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='انشائه'),
        ),
        migrations.AlterField(
            model_name='university',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='رقم التلفون'),
        ),
        migrations.AlterField(
            model_name='university',
            name='type',
            field=models.CharField(choices=[('Especiall', 'Especiall'), ('governmental', 'governmental')], max_length=50, verbose_name='النوع'),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ الأنشاء'),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleted',
            field=models.BooleanField(blank=True, null=True, verbose_name='هل محذوف'),
        ),
        migrations.AlterField(
            model_name='user',
            name='deletedat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ الحذف'),
        ),
        migrations.AlterField(
            model_name='user',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='عدله '),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name=' هل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='modifiedat',
            field=models.DateField(auto_now=True, verbose_name='تاريخ التعديل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='حذفه '),
        ),
        migrations.AlterField(
            model_name='user',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='انشائه '),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='رقم التلفون'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.CharField(blank=True, choices=[('1', 'General Administration'), ('2', 'District administration'), ('3', 'Manage a service office'), ('4', 'Manage a freight office')], default='1', max_length=1, null=True, verbose_name='نوعه'),
        ),
        migrations.AlterField(
            model_name='user',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university', verbose_name='الجامعة'),
        ),
    ]
