# Generated by Django 4.0 on 2021-12-31 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_image_alter_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='projects/static/images/default.jpg', upload_to='projects/static/images/'),
        ),
    ]
