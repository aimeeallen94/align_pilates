# Generated by Django 3.2.25 on 2024-06-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0012_remove_class_type_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
