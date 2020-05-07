from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from .functions import *
from django.conf import settings
from django.core.files.storage import default_storage
import imghdr
import os

def functions_index(request, isDigitalSig=0, isKeys=0, isHashing=0, isWatermark=0,
                        digital_object=DigitalSig(), key_object=Keys(), 
                        hashing_object=Hashing(), water_object=WaterMarking() ):
    functions = Function.objects.all().order_by('order')

    form = UploadFileForm()
    keyInputForm = KeyInputForm()
    response = None
    if not isDigitalSig and not isKeys and not isHashing and not isWatermark:
        digital_object.isInvalid = False
        digital_object.isSigned = False
        hashing_object.isActive = False
        water_object.isActive = False
        key_object.isActive =False
        
    if request.method == 'POST' and isDigitalSig:
        if digital_object.isActive:
            try:
                digital_object.private = RSA.importKey(request.POST.get('private'))
                for f in functions:
                    if 'Digital' in f.name:
                        digital_object.sig, f = CreateDigitalSignature(digital_object,f)
                        break
                digital_object.isSigned = True
            except:
                digital_object.isInvalid=True

    if request.method == 'POST' and isWatermark:
        if water_object.isActive and water_object.isValidImg:
            if water_object.isDownload:
                response = HttpResponse(water_object.out_img, content_type='Image')
                response['Content-Disposition'] = 'attachment; filename='+water_object.out_fName.split('./watermarks/')[1]
                water_object.isDownload = False
                water_object.isValidImg = False
                water_object.isActive = False
                return response
            else:
                water_object.x = int(request.POST.get('x'))
                water_object.y = int(request.POST.get('y'))
                water_object.font_size = int(request.POST.get('font_size'))
                water_object.mark_text = request.POST.get('mark')
                for f in functions:
                    if 'Water' in f.name:
                        water_object.out_img, water_object.out_fName, f = CreateWaterMarking(water_object,f)
                        water_object.isDownload = True
                        break
                    
    if request.method == 'POST' and isKeys:
        if key_object.isActive:
            if key_object.isDownload:
                response = HttpResponse(key_object.out_file, content_type='PEM')
                response['Content-Disposition'] = 'attachment; filename=newKeys.pem'
                key_object.isActive = False
                key_object.isDownload = False
                return response

    if request.method == 'POST' and len(request.FILES):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = UploadFile(file=request.FILES['file'])
            file.isFile = True
            file.save()
            if isDigitalSig:
                digital_object.upload = file
                digital_object.isActive = True
                digital_object.isSigned = False
            elif isHashing:
                hashing_object.upload = file
                hashing_object.isActive = True
                for f in functions:
                    if 'Hashing' in f.name:
                        hashing_object.hash, f = CreateSecureHashing(hashing_object,f)
                        break
            elif isWatermark:
                water_object.isValidImg= False
                if imghdr.what(file.file.path) in img_formats:
                    water_object.upload = file
                    water_object.isActive = True
                    water_object.isValidImg= True
                else:
                    water_object.upload = file
                    water_object.isActive = False
            form.isFile = True

    if isDigitalSig or isKeys or isHashing or isWatermark:
        if isDigitalSig:
            key_object.isActive, hashing_object.isActive, water_object.isActive = False, False, False
            key_object.upload, hashing_object.upload, water_object.upload = UploadFile(None), UploadFile(None), UploadFile(None)
        elif isKeys:
            key_object.isActive = True
            for f in functions:
                    if 'Keys' in f.name:
                        key_object, key_object.out_file, f = CreateKeys(key_object, f)
                        key_object.isDownload = True
                        break
            digital_object.isActive, hashing_object.isActive, water_object.isActive = False, False, False
            digital_object.upload, hashing_object.upload, water_object.upload = UploadFile(None), UploadFile(None), UploadFile(None)
            digital_object.isSigned = False
            digital_object.isInvalid = False
        elif isHashing:
            key_object.isActive, digital_object.isActive, water_object.isActive = False, False, False
            key_object.upload, digital_object.upload, water_object.upload = UploadFile(None), UploadFile(None), UploadFile(None)
            digital_object.isSigned = False
            digital_object.isInvalid = False
        elif isWatermark:
            key_object.isActive, hashing_object.isActive, digital_object.isActive = False, False, False
            key_object.upload, hashing_object.upload, digital_object.upload = UploadFile(None), UploadFile(None), UploadFile(None)
            digital_object.isSigned = False
            digital_object.isInvalid = False
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
        'water_object': water_object,
        'response': response
    }
    return render(request, 'functions_index.html', context)
