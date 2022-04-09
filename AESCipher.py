from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import binascii
import sys
    
key = pad(b"mykey", AES.block_size)
iv = pad(b"myiv", AES.block_size)


def encrypt(plaintext):
    data_bytes = bytes(plaintext, 'utf-8')
    padded_bytes=pad(data_bytes, AES.block_size)
    AES_obj = AES.new(key, AES.MODE_CBC,iv)
    ciphertext = AES_obj.encrypt(padded_bytes)
    return ciphertext

def decrypt(ciphertext):
    AES_obj = AES.new(key, AES.MODE_CBC, iv)
    raw_bytes=AES_obj.decrypt(ciphertext)
    extracted_bytes = unpad(raw_bytes, AES.block_size)
    return extracted_bytes

def read_txt(file):
    file = open(file, 'r')
    return file.read()

def save_to_txt(file, result):
    f = open(file, 'w+')
    f.write(result.decode('utf-8'))
    f.close()
    return f

if __name__ == '__main__':

    plaintext = "foeiafjeifajoeiafjo"
    f = open('test.txt', 'w+')
    f.write(plaintext)
    f.close() 
       
   
    
    if len(sys.argv) == 3:
        if sys.argv[1] == '-e':
            file = str(sys.argv[2])
            plaintext = read_txt(file)
            ciphertext = encrypt(plaintext)
            binascii_ = binascii.hexlify(ciphertext)
            plaintext_enc = save_to_txt('encrypted.txt', binascii_)
            print("encrypted.txt added")
    
        if sys.argv[1] == '-d':
            file = sys.argv[2] 
            binascii_data  = read_txt(bytes(file, 'utf-8'))
            ciphertext = binascii.unhexlify(binascii_data)
            plaintext_dec = decrypt(ciphertext)
            plaintext = save_to_txt('plaintext.txt', plaintext_dec)
            print("plaintext.txt added")
    else:
        print('Format Error')