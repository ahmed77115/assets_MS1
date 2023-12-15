# Generated by Django 4.2.6 on 2023-10-28 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("assets", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customer", "0001_initial"),
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AssetsIssuance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "createdat",
                    models.DateField(auto_now=True, verbose_name="createdat"),
                ),
                (
                    "modifiedat",
                    models.DateField(auto_now=True, verbose_name="modifiedat"),
                ),
                (
                    "deletedat",
                    models.DateField(auto_now=True, verbose_name="deletedat"),
                ),
                ("deleted", models.BooleanField(default=False, verbose_name="Deleted")),
                ("checkout_date", models.DateTimeField()),
                ("return_date", models.DateTimeField(null=True)),
                ("checkout_condition", models.TextField()),
                ("return_condition", models.TextField(null=True)),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="assets.asset"
                    ),
                ),
                (
                    "asset_location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="assets.location",
                    ),
                ),
                (
                    "deletedby",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_deletedby_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="deletedby",
                    ),
                ),
                (
                    "modifiedby",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_modifiedby_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="modifiedby",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_ownership",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="OWner",
                    ),
                ),
                (
                    "partner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.partner",
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_ownership",
                        to="base.university",
                        verbose_name="الشركة",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "default_manager_name": "objects",
            },
        ),
    ]
