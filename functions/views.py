from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from .functions import *
from django.conf import settings
from django.core.files.storage import default_storage
import os

def functions_index(request, isDigitalSig=0, isKeys=0, isHashing=0, isWatermark=0,
                        digital_object=DigitalSig(), key_object=Keys(), 
                        hashing_object=Hashing(), water_object=WaterMarking() ):
    functions = Function.objects.all()

    form = UploadFileForm()
    keyInputForm = KeyInputForm()


    if request.method == 'POST' and isDigitalSig:
        if digital_object.isActive:
            digital_object.private = RSA.importKey(request.POST.get('private'))
            for f in functions:
                if 'Digital' in f.name:
                    digital_object.sig, f = CreateDigitalSignature(digital_object,f)
                    break
            digital_object.isSigned = True

    if request.method == 'POST' and len(request.FILES):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = UploadFile(file=request.FILES['file'])
            file.isFile = True
            file.save()
            if isDigitalSig:
                digital_object.upload = file
                digital_object.isActive = True
            elif isHashing:
                hashing_object.upload = file
                hashing_object.isActive = True
                for f in functions:
                    if 'Hashing' in f.name:
                        hashing_object.hash, f = CreateSecureHashing(hashing_object,f)
                        break
            elif isWatermark:
                water_object.upload = file
                water_object.isActive = True
            form.isFile = True

    if isDigitalSig or isKeys or isHashing or isWatermark:
        if isDigitalSig:
            key_object.isActive, hashing_object.isActive, water_object.isActive = False, False, False
            key_object.upload, hashing_object.upload, water_object.upload = UploadFile(None), UploadFile(None), UploadFile(None)
        elif isKeys:
            key_object.isActive = True
            for f in functions:
                    if 'Keys' in f.name:
                        key_object, pem_file, f = CreateKeys(key_object, f)
                        break
            digital_object.isActive, hashing_object.isActive, water_object.isActive = False, False, False
            digital_object.upload, hashing_object.upload, water_object.upload = UploadFile(None), UploadFile(None), UploadFile(None)
            response = HttpResponse(pem_file, content_type='PEM')
            response['Content-Disposition'] = 'attachment; filename=newKeys.pem'
            return response
        elif isHashing:
            key_object.isActive, digital_object.isActive, water_object.isActive = False, False, False
            key_object.upload, digital_object.upload, water_object.upload = UploadFile(None), UploadFile(None), UploadFile(None)
        elif isWatermark:
            key_object.isActive, hashing_object.isActive, digital_object.isActive = False, False, False
            key_object.upload, hashing_object.upload, digital_object.upload = UploadFile(None), UploadFile(None), UploadFile(None)
        digital_object.save()
        key_object.save()
        hashing_object.save()
        water_object.save()

    context = {
        'functions': functions,
        'form': form,
        'keyInputForm': keyInputForm,
        'isDigitalSig': isDigitalSig, 
        'isKeys': isKeys, 
        'isHashing': isHashing, 
        'isWatermark': isWatermark,
        'digital_object': digital_object,
        'key_object': key_object,
        'hashing_object': hashing_object,
        'water_object': water_object
    }
    return render(request, 'functions_index.html', context)
