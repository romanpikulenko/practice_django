# Generated by Django 4.1.5 on 2023-02-04 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
