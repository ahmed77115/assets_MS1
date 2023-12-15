# Generated by Django 4.2.7 on 2023-11-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movement', '0004_alter_movement_options_movement_asset_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movement',
            name='status',
            field=models.CharField(choices=[('in', 'in'), ('out', 'out'), ('non', 'in')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movement',
            name='type_movement',
            field=models.CharField(choices=[('in', 'in'), ('out', 'out'), ('non', 'in')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
