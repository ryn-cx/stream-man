# Generated by Django 5.0.3 on 2024-03-29 22:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("media", "0016_alter_show_media_type_alter_show_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="season",
            name="update_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
