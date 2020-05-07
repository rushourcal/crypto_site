from django.db import models
from django import forms

class Function(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path="/img")
    op_time=models.CharField(max_length=4096)


class UploadFile(models.Model):
    file= models.FileField(upload_to='uploads/', null=True, verbose_name="")

class DigitalSig(models.Model):
    upload = UploadFile()
    isActive=False
    isSigned=False
    sig=models.CharField(max_length=10096)
    public = models.CharField(max_length=4096)
    private = models.CharField(max_length=4096)

class Keys(models.Model):
    isActive=False
    public = models.CharField(max_length=4096)
    private = models.CharField(max_length=4096)

class WaterMarking(models.Model):
    upload = UploadFile()
    isActive=False

class Hashing(models.Model):
    upload = UploadFile()
    isActive=False
    hash = models.CharField(max_length=10096)



