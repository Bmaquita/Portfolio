# Generated by Django 4.1.7 on 2023-03-29 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_alter_coursescertifications_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurriculumVitae',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(upload_to='CV')),
            ],
            options={
                'verbose_name': ' Curriculum Vitae',
                'verbose_name_plural': ' Curriculum Vitae',
            },
        ),
    ]
