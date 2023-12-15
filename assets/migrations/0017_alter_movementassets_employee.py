# Generated by Django 4.2.6 on 2023-12-02 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_partner_customer_number_and_more'),
        ('assets', '0016_alter_asset_activation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movementassets',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movement_lines_as_from_employee_mov', to='customer.partner', verbose_name='العميل'),
        ),
    ]