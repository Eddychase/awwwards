# Generated by Django 3.1.8 on 2021-04-12 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='screenshot_1',
            new_name='upload_1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='screenshot_2',
            new_name='upload_2',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='screenshot_3',
            new_name='upload_3',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='screenshot_4',
            new_name='upload_4',
        ),
    ]
