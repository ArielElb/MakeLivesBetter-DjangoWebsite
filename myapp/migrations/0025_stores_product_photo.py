# Generated by Django 4.1 on 2022-09-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_stores_id_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='product_photo',
            field=models.ImageField(blank=True, null=True, upload_to='files/'),
        ),
    ]