# Generated by Django 4.0.2 on 2022-03-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wally', '0002_rename_image_post_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to='posts'),
        ),
    ]
