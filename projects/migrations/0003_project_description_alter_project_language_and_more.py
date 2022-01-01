# Generated by Django 4.0 on 2021-12-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='Generic description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
