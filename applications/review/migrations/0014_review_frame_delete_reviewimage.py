# Generated by Django 4.0.3 on 2022-03-28 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0013_remove_review_frame_reviewimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='frame',
            field=models.ImageField(blank=True, null=True, upload_to='review_frames'),
        ),
        migrations.DeleteModel(
            name='ReviewImage',
        ),
    ]
