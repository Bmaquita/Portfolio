# Generated by Django 4.1.7 on 2023-03-31 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_curriculumvitae'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursescertifications',
            name='created_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='education',
            name='created_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='projects',
            name='created_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
