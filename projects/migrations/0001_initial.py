# Generated by Django 4.0 on 2021-12-31 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.DateTimeField(verbose_name='date created')),
                ('link', models.TextField()),
            ],
        ),
    ]
