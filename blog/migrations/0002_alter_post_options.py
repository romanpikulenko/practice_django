# Generated by Django 4.1.5 on 2023-01-31 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "verbose_name": "Create a post",
                "verbose_name_plural": "Create posts",
            },
        ),
    ]
