# Generated by Django 3.2.5 on 2021-07-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0002_profile_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cgpa',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='school_percentage',
            field=models.IntegerField(default=50),
        ),
    ]
