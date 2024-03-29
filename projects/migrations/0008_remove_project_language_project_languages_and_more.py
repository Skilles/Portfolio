# Generated by Django 4.1 on 2022-09-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='language',
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='try_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(),
        ),
    ]
