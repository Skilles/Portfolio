# Generated by Django 4.1 on 2022-09-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='static/images/default.jpg', upload_to=''),
        ),
    ]