# Generated by Django 4.0.3 on 2022-03-10 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='parent',
        ),
    ]
