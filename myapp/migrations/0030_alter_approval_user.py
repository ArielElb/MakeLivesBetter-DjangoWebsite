# Generated by Django 4.1 on 2022-09-05 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_rename_aproval_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.userextend'),
        ),
    ]
