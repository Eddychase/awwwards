# Generated by Django 3.1.8 on 2021-04-12 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0002_auto_20210412_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='upload_1',
            new_name='screenshot_1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='upload_2',
            new_name='screenshot_2',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='upload_3',
            new_name='screenshot_3',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='upload_4',
            new_name='screenshot_4',
        ),
    ]
