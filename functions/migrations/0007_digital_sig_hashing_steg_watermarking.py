# Generated by Django 3.0.5 on 2020-05-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0006_delete_digitalsignature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Digital_Sig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Hashing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Steg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='WaterMarking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to='')),
            ],
        ),
    ]
