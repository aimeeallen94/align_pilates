# Generated by Django 3.2.25 on 2024-06-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0009_alter_ratings_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
    ]