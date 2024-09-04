# Generated by Django 5.0.4 on 2024-09-03 17:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("medicine", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                    "patient_first_name",
                    models.CharField(default="firstname", max_length=255),
                ),
                (
                    "patient_last_name",
                    models.CharField(default="lastname", max_length=255),
                ),
                ("patient_phone_number", models.CharField(default="1", max_length=20)),
                ("patient_national_id", models.CharField(default="1", max_length=20)),
                ("patient_gender", models.CharField(default="gender", max_length=10)),
                ("date", models.DateTimeField()),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(0, "scheduled"), (1, "cancelled"), (2, "completed")],
                        default=0,
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointments",
                        to="medicine.provider",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="service_appointments",
                        to="medicine.service",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_appointments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "appointment",
            },
        ),
    ]
