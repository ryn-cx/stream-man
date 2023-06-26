# Generated by Django 4.2.2 on 2023-06-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("playlists", "0005_remove_playlistshow_playlist_season_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="playlist",
            name="thumbnail",
            field=models.ImageField(blank=True, default=None, max_length=255, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="playlist",
            name="default_filter",
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]