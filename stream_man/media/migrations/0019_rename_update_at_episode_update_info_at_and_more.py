# Generated by Django 5.0.3 on 2024-03-30 01:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("media", "0018_episode_update_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="episode",
            old_name="update_at",
            new_name="update_info_at",
        ),
        migrations.RenameField(
            model_name="season",
            old_name="update_at",
            new_name="update_info_at",
        ),
        migrations.RenameField(
            model_name="show",
            old_name="update_at",
            new_name="update_info_at",
        ),
    ]
