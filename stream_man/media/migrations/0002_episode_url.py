# Generated by Django 4.2.2 on 2023-06-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("media", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="episode",
            name="url",
            field=models.CharField(default="WOOPS", max_length=255),
            preserve_default=False,
        ),
    ]
