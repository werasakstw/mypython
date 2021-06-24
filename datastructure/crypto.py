
# Caesar Method.
_chars = '!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'
_clen = len(_chars)
def encode(msg, key):
    def enc(c, key):
        ec = (_chars.find(c) + key) % _clen
        return _chars[ec]
    emsg = ''
    for i in msg:
        emsg += enc(i, key)
    return emsg

def decode(emsg, key):
    def dec(c, key):
        dc = _chars.find(c) - key
        if dc >= _clen:
            dc -= _clen
        elif dc < 0:
            dc += _clen        
        return _chars[dc]
    dmsg = ''
    for i in emsg:
        dmsg += dec(i, key)
    return dmsg

def caesar_test(msg, key):
    em = encode(msg, key)
    print(em)
    print(decode(em, key))
caesar_test("Hello It's nice to see you!", 23)

## In cases we don't know the key.
def brute_force(msg, key):
    em = encode(msg, key)
    print(em)
    for i in range(_clen):
        dm = decode(em, i)
        if 'you' in dm:  ## Suppose we know the message contains 'you'.
            print(i, dm)
            break
# brute_force("Hello It's nice to see you!", 17)

## Asymmetric Key:
from Crypto import Random
from Crypto.PublicKey import RSA
def rsa_test(msg):
    ## generate asymmetric key
    key = RSA.generate(1024)
    with open('private_key', 'wb') as f:
       f.write(key.exportKey()) 
    with open('public_key', 'wb') as f:
       f.write(key.publickey().exportKey())
    
    ## encode with public key
    with open('public_key','rb') as f:
       public_key = RSA.importKey(f.read())
    seed = Random.new().read(16)  ## seed is used for encode only.
    emsg = public_key.encrypt(msg.encode(), seed)
    print(emsg)

    ## decode with private key
    with open('private_key','rb') as f:
      private_key = RSA.importKey(f.read())
    dmsg = private_key.decrypt(emsg)
    print(dmsg.decode())
# rsa_test('Hello how do you do?')

## Symmetric Key:
from Crypto.Cipher import AES
def aes_test(msg):
    # AES key must be either 16, 24, or 32 bytes long
    key = 'hello_1234567890'.encode()
    seed = Random.new().read(AES.block_size)  ## AES.block_size = 16 
    ## The ciphers are depended on both key and seed, we need to keep them alive.
    with open('key', 'wb') as f:
        f.write(key)
    with open('seed', 'wb') as f:
        f.write(seed)

    ## encode
    cipher = AES.new(key, AES.MODE_CFB, seed)
    emsg = cipher.encrypt(msg.encode())
    print(emsg)

    ## decode
    with open('key','rb') as f:
        key = f.read()
    with open('seed','rb') as f:
        seed = f.read()
    cipher = AES.new(key, AES.MODE_CFB, seed)
    dmsg = cipher.decrypt(emsg)
    print(dmsg.decode())
# aes_test("Hello it's nice to see you.")


## Digital Signature:
import hashlib
from Crypto.Hash import SHA256
def hash(msg):
    m = msg.encode()
    h1 = hashlib.md5()           ## MD5
    h2 = hashlib.sha1()          ## SHA1
    h3 = SHA256.new()            ## SHA256
    
    h1.update(m)
    h2.update(m)
    h3.update(m)
    
    print(h1.digest())
    print(h2.hexdigest())
    print(h3.hexdigest())
hash('Hello')

def sig_test():
    def gen(msg):
        h = SHA256.new()
        h.update(msg.encode())
        with open('data/tmp.sig', 'w') as f:
            f.write(h.hexdigest())
    def verify(msg):
        h = SHA256.new()
        h.update(msg.encode())
        new_sig = h.hexdigest()
        with open('data/tmp.sig', 'r') as f:
            old_sig = f.read()
        return new_sig == old_sig
    gen(msg)
    print(verify(msg))
# sig_test()





