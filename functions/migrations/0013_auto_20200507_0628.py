# Generated by Django 3.0.5 on 2020-05-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0012_hashing_hash'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OperationTime',
        ),
        migrations.AddField(
            model_name='digitalsig',
            name='op_time',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='digitalsig',
            name='sig',
            field=models.CharField(default='', max_length=10096),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hashing',
            name='op_time',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='keys',
            name='op_time',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watermarking',
            name='op_time',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
    ]
