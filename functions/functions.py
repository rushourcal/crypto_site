from .DigitalSignature import *
import time
import subprocess
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img_formats = [
    'rgb',
    'gif',
    'pbm',
    'pgm',
    'ppm',
    'tiff',
    'rast',
    'xbm',
    'jpeg',
    'jpg',
    'bmp',
    'png',
    'webp',
    'exr',
]

#   Clear temp files on startup


startup = True
if startup:
    subprocess.run('rm ./uploads/uploads/*', shell=True)
    subprocess.run('rm ./watermarks/*', shell=True)
    startup = False

def CreateDigitalSignature(digital_object, f):
    private = digital_object.private
    public = digital_object.private.publickey().exportKey()

    start = time.time()
    with open(digital_object.upload.file.path, "rb") as signedfile:
        hash = generate_hash(signedfile.read())

    signature = generate_signature(hash, private)[0]

    f.op_time = str(time.time() - start)
    return signature, f

def CreateKeys(key_object, f):
    start = time.time()

    keys = generate_keys()
    key_object.public = keys.publickey().exportKey() 
    key_object.private = keys.exportKey()
    pem_file = keys.exportKey('PEM')

    f.op_time = str(time.time() - start)
    return key_object, pem_file, f


def CreateSecureHashing(hashing_object, f):

    start = time.time()

    with open(hashing_object.upload.file.path, "rb") as signedfile:
        hash = generate_hash(signedfile.read())
    hash = hash.hex()

    f.op_time = str(time.time() - start)
    return hash, f

'''
    This watermarking code has been directly used and derived from the example 
    code written by: October 17, 2017Pythonimages, Pillow, PythonMike
    at https://www.blog.pythonlibrary.org/2017/10/17/how-to-watermark-your-photos-with-python/
'''
def CreateWaterMarking(water_object, f):
    start = time.time()
    pos = (water_object.x, water_object.y)

    photo = Image.open(water_object.upload.file.path)

    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype('./arial.ttf', water_object.font_size)
    drawing.text(pos, water_object.mark_text, fill=black, font=font)
    fName = './watermarks/watermarked_' + water_object.upload.file.name.split('uploads/')[1]
    photo.save(fName)

    f.op_time = str(time.time() - start)

    return open(fName, 'rb'), fName, f