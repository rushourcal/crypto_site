# Generated by Django 3.0.5 on 2020-05-05 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0008_auto_20200505_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digitalsig',
            name='uploaded_file',
        ),
        migrations.RemoveField(
            model_name='hashing',
            name='uploaded_file',
        ),
        migrations.RemoveField(
            model_name='steg',
            name='uploaded_file',
        ),
        migrations.RemoveField(
            model_name='watermarking',
            name='uploaded_file',
        ),
    ]
