# Generated by Django 3.2.25 on 2024-06-09 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_full_name_contactdetails_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdetails',
            old_name='user',
            new_name='full_name',
        ),
    ]
