# Generated by Django 5.1.1 on 2024-10-03 14:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_profile_bio_profile_profession"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="profession",
        ),
    ]
