# Generated by Django 4.1 on 2022-09-07 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0052_alter_approvedpost_is_approved'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='VolunteeringOption',
        ),
        migrations.AlterModelOptions(
            name='volunteeringoption',
            options={'verbose_name': 'VolunteeringOption', 'verbose_name_plural': 'VolunteeringOptions'},
        ),
    ]
