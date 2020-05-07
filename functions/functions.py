from .DigitalSignature import *
import time

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


def CreateWaterMarking(water_object, f):
    start = time.time()
    

    f.op_time = str(time.time() - start)
    return water_object, f