# Generated by Django 4.1 on 2022-09-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_merge_20220902_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextend',
            name='store_list',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
    ]
