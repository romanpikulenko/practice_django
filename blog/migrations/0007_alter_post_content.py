# Generated by Django 4.1.5 on 2023-02-04 17:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_post_likes_post_reply_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, max_length=4000, null=True),
        ),
    ]
