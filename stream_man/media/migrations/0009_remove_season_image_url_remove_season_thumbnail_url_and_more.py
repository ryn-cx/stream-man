# Generated by Django 4.2.2 on 2023-07-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("media", "0008_remove_episode_image_url_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="season",
            name="image_url",
        ),
        migrations.RemoveField(
            model_name="season",
            name="thumbnail_url",
        ),
        migrations.RemoveField(
            model_name="show",
            name="image_url",
        ),
        migrations.RemoveField(
            model_name="show",
            name="thumbnail_url",
        ),
        migrations.AddField(
            model_name="season",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AddField(
            model_name="show",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
    ]