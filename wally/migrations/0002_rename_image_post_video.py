# Generated by Django 4.0.2 on 2022-03-30 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wally', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='video',
        ),
    ]