# Generated by Django 4.1 on 2022-08-30 12:11

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
