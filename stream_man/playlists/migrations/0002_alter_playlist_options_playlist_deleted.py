# Generated by Django 4.2.2 on 2023-06-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("playlists", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="playlist",
            options={"ordering": ["name"]},
        ),
        migrations.AddField(
            model_name="playlist",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
    ]
