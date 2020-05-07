"""
    This code has been copied and/or directly derived from;
    https://gist.github.com/petri/650e27c712888bf4cb27c99716d36e45
    All credit is due to this user, and it's further credits
    Kyle Teixeira makes no claim to this code, and is not credited with it's ownership
"""


"""digicheck - create and verify signatures for files
Usage:
  digicheck keys
  digicheck public <keyfilename>
  digicheck sign <filename> <keyfilename>
  digicheck check <filename> <keyfilename> <signaturefilename>
  digicheck (-h | --help)
  digicheck --version
Use the command-line to first create a key pair, then a
signature for a file, and finally when you need to make
sure file has not been tampered with in the meantime,
check that the signatures are still equal.
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import sys
import docopt

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

def generate_keys():
   random_generator = Random.new().read
   key = RSA.generate(2048, random_generator)
   return (key)

def generate_hash(data):
   return SHA256.new(data).digest()

def generate_signature(hash, key):
   return key.sign(hash, '')

def verify_signature(hash, public_key, signature):
   return public_key.verify(hash, signature)

if __name__ == "__main__":

   args = docopt.docopt(__doc__)

   if args["keys"]:

      private, public = generate_keys()
      keys = private + "\n\n" + public
      print(keys.strip())

   elif args["public"]:

      with open(args["<keyfilename>"], "r") as keyfile:
         public_key = keyfile.read().split("\n\n")[1]
      print(public_key.strip())

   elif args["sign"]:

      with open(args["<filename>"], "rb") as signedfile:
         hash = generate_hash(signedfile.read())

      with open(args["<keyfilename>"], "r") as keyfile:
         private_key = RSA.importKey(keyfile.read().split("\n\n")[0].strip())

      print(generate_signature(hash, private_key)[0])

   elif args["check"]:

      with open(args["<filename>"], "rb") as signedfile:
         hash = generate_hash(signedfile.read())

      with open(args["<keyfilename>"], "r") as keyfile:
         public_key = RSA.importKey(keyfile.read().split("\n\n")[1].strip())

      with open(args["<signaturefilename>"], "r") as signaturefile:
         signature = long(signaturefile.read())

      if verify_signature(hash, public_key, (signature,)):
         sys.exit("valid signature :)")
      else:
         sys.exit("invalid signature! :(")