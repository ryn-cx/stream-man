# Generated by Django 4.2.2 on 2023-06-07 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Episode",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("info_timestamp", models.DateTimeField()),
                ("info_modified_timestamp", models.DateTimeField()),
                ("episode_id", models.CharField(max_length=64)),
                ("name", models.CharField(max_length=500)),
                ("number", models.CharField(max_length=64)),
                ("sort_order", models.PositiveSmallIntegerField(null=True)),
                ("image_url", models.CharField(max_length=256)),
                ("thumbnail_url", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("release_date", models.DateTimeField()),
                ("duration", models.PositiveSmallIntegerField()),
                ("deleted", models.BooleanField()),
            ],
            options={
                "ordering": ["season", "sort_order"],
            },
        ),
        migrations.CreateModel(
            name="EpisodeWatch",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("watch_date", models.DateField()),
            ],
            options={
                "ordering": ["watch_date"],
            },
        ),
        migrations.CreateModel(
            name="Season",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("info_timestamp", models.DateTimeField()),
                ("info_modified_timestamp", models.DateTimeField()),
                ("season_id", models.CharField(max_length=64)),
                ("name", models.CharField(max_length=64)),
                ("sort_order", models.PositiveSmallIntegerField()),
                ("image_url", models.CharField(max_length=255)),
                ("thumbnail_url", models.CharField(max_length=255)),
                ("url", models.CharField(max_length=255)),
                ("deleted", models.BooleanField()),
            ],
            options={
                "ordering": ["show", "sort_order"],
            },
        ),
        migrations.CreateModel(
            name="Show",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("info_timestamp", models.DateTimeField()),
                ("info_modified_timestamp", models.DateTimeField()),
                ("website", models.CharField(max_length=255)),
                ("show_id", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=256)),
                ("media_type", models.CharField(max_length=256)),
                ("description", models.TextField()),
                ("image_url", models.CharField(max_length=256)),
                ("thumbnail_url", models.CharField(max_length=255)),
                ("url", models.CharField(max_length=255)),
                ("favicon_url", models.CharField(max_length=255)),
                ("update_at", models.DateTimeField(blank=True, null=True)),
                ("deleted", models.BooleanField()),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="UpdateQue",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("website", models.CharField(max_length=256)),
                ("next_update_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "update_que",
            },
        ),
        migrations.AddConstraint(
            model_name="updateque",
            constraint=models.UniqueConstraint(fields=("website",), name="UpdateQue_website"),
        ),
        migrations.AddConstraint(
            model_name="show",
            constraint=models.UniqueConstraint(fields=("website", "show_id"), name="Show_website_show_id"),
        ),
        migrations.AddField(
            model_name="season",
            name="show",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="media.show"),
        ),
        migrations.AddField(
            model_name="episodewatch",
            name="episode",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="media.episode"),
        ),
        migrations.AddField(
            model_name="episode",
            name="season",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="media.season"),
        ),
        migrations.AddConstraint(
            model_name="season",
            constraint=models.UniqueConstraint(fields=("show", "season_id"), name="Season_show_season_id"),
        ),
        migrations.AddConstraint(
            model_name="episodewatch",
            constraint=models.UniqueConstraint(
                fields=("episode", "watch_date"), name="EpisodeWatch_episode_watch_date"
            ),
        ),
        migrations.AddConstraint(
            model_name="episode",
            constraint=models.UniqueConstraint(fields=("season", "episode_id"), name="Episode_season_episode_id"),
        ),
    ]
