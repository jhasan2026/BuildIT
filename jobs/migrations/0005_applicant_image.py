# Generated by Django 5.1.1 on 2024-11-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0004_applicant_address_applicant_city_applicant_country_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="applicant",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="applicant_pic"),
        ),
    ]
