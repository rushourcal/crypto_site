from django.db import models
from django import forms

class Function(models.Model):
    order = models.IntegerField(default=0)
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
    isInvalid=False
    sig=models.CharField(max_length=10096)
    public = models.CharField(max_length=4096)
    private = models.CharField(max_length=4096)

class Keys(models.Model):
    isActive=False
    isDownload=False
    public = models.CharField(max_length=4096)
    private = models.CharField(max_length=4096)
    out_file=None

class WaterMarking(models.Model):
    upload = UploadFile()
    isActive=False
    isValidImg=False
    isDownload=False
    x = models.IntegerField(default=3)
    y = models.IntegerField(default=8)
    font_size = models.IntegerField(default=14)
    mark_text = models.CharField(max_length=4096)
    out_img = None
    out_fName=''

class Hashing(models.Model):
    upload = UploadFile()
    isActive=False
    hash = models.CharField(max_length=10096)



