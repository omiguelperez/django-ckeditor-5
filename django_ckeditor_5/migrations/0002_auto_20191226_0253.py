# Generated by Django 3.0 on 2019-12-26 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_ckeditor_5', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ckeditorimageupload',
            old_name='image',
            new_name='upload',
        ),
    ]
