# Generated by Django 5.0.3 on 2024-03-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0003_remove_driver_groups_remove_driver_user_permissions_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="published_date",
            field=models.DateTimeField(
                default=models.TextField(default="", max_length=255)
            ),
        ),
    ]
