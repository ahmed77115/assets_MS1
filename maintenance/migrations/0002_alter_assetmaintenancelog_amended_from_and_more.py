# Generated by Django 4.2.6 on 2023-10-30 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmaintenancelog',
            name='amended_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maintenance.assetmaintenancelog'),
        ),
        migrations.AlterField(
            model_name='assetmaintenancelog',
            name='certificate_attachment',
            field=models.FileField(blank=True, null=True, upload_to='certificates/'),
        ),
        migrations.AlterField(
            model_name='assetmaintenancelog',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assetmaintenancelog',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='deletedby'),
        ),
        migrations.AlterField(
            model_name='assetmaintenancelog',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='modifiedby'),
        ),
        migrations.AlterField(
            model_name='assetmaintenancelog',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='OWner'),
        ),
        migrations.AlterField(
            model_name='assetrepair',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assetrepair',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='deletedby'),
        ),
        migrations.AlterField(
            model_name='assetrepair',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='modifiedby'),
        ),
        migrations.AlterField(
            model_name='assetrepair',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='OWner'),
        ),
        migrations.AlterField(
            model_name='assetrepairconsumeditem',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='deletedby'),
        ),
        migrations.AlterField(
            model_name='assetrepairconsumeditem',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='modifiedby'),
        ),
        migrations.AlterField(
            model_name='assetrepairconsumeditem',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='OWner'),
        ),
        migrations.AlterField(
            model_name='maintenanceasset',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='deletedby'),
        ),
        migrations.AlterField(
            model_name='maintenanceasset',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='modifiedby'),
        ),
        migrations.AlterField(
            model_name='maintenanceasset',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='OWner'),
        ),
        migrations.AlterField(
            model_name='maintenancemember',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='deletedby'),
        ),
        migrations.AlterField(
            model_name='maintenancemember',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='modifiedby'),
        ),
        migrations.AlterField(
            model_name='maintenancemember',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='OWner'),
        ),
        migrations.AlterField(
            model_name='maintenanceteam',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='deletedby'),
        ),
        migrations.AlterField(
            model_name='maintenanceteam',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='modifiedby'),
        ),
        migrations.AlterField(
            model_name='maintenanceteam',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='OWner'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deletedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deletedby_set', to=settings.AUTH_USER_MODEL, verbose_name='deletedby'),
        ),
        migrations.AlterField(
            model_name='task',
            name='modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_modifiedby_set', to=settings.AUTH_USER_MODEL, verbose_name='modifiedby'),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL, verbose_name='OWner'),
        ),
    ]