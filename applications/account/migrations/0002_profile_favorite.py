# Generated by Django 4.0.3 on 2022-03-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_delete_search'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to='movies.movie'),
        ),
    ]
