# Generated by Django 4.1 on 2022-09-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_remove_project_language_project_languages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='static/images/default.jpg', upload_to='projects/images/'),
        ),
    ]
