# Generated by Django 5.0 on 2024-01-01 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("media", "0013_alter_episode_options_alter_episodewatch_options_and_more"),
        ("playlists", "0008_alter_playlist_thumbnail"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="playlistimportqueue",
            name="PlaylistImportQueue_playlist_url",
        ),
        migrations.RemoveConstraint(
            model_name="playlistshow",
            name="PlaylistShow_show_playlist",
        ),
        migrations.AlterField(
            model_name="playlist",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="playlistimportqueue",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="playlistshow",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AddConstraint(
            model_name="playlistimportqueue",
            constraint=models.UniqueConstraint(
                fields=("playlist", "url"), name="UQ_PlaylistImportQueue_playlist_url"
            ),
        ),
        migrations.AddConstraint(
            model_name="playlistshow",
            constraint=models.UniqueConstraint(
                fields=("show", "playlist"), name="UQ_PlaylistShow_show_playlist"
            ),
        ),
    ]