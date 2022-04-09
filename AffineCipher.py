import sys


def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y 

def modinv(a, m): 
  gcd, x, y = egcd(a, m) 
  if gcd != 1: 
    return None  
  else: 
    return x % m 
 
def encrypt(text, key): 
  return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ]) 


def decrypt(cipher, key): 
  return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 


if len(sys.argv) <= 8:
    key = [17,20]
    if sys.argv[1] == '-a' and sys.argv[3] == '-b' and sys.argv[5] == '-e' :
        key[0] = int(sys.argv[2])
        key[1] = int(sys.argv[4])
        text = str(sys.argv[6])
        enc_text = encrypt(text, key) 
        print('Encrypted sentence: {}'.format(enc_text)) 
    
    if  sys.argv[1] == '-a' and sys.argv[3] == '-b'and sys.argv[5] == '-d' :
        text = str(sys.argv[6]) 
        key[0] = int(sys.argv[2])
        key[1] = int(sys.argv[4])
        dec_text = decrypt(text, key)
        print('Decrypted sentence: {}'.format(dec_text)) 
else:
    print('Format Error')

