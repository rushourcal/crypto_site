# Generated by Django 3.0.5 on 2020-05-07 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0017_watermarking_font_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
