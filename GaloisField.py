def degree(digit):
    for i in range(len(digit)):
        if digit[i] == 1:
            return len(digit) - i - 1
    return -1


def index_of_power(power, len_list):
    return len_list - power - 1

def multiply(a, b):
    res = [0] * (degree(a) + degree(b) + 1)
    len_res = len(res)
    len_a = len(a)
    len_b = len(b)
    for power_a in range(degree(a), -1, -1):
        for power_b in range(degree(b), -1, -1):
            res_index = index_of_power(power_a+ power_b, len_res)
            a_index = index_of_power(power_a, len_a)
            b_index = index_of_power(power_b, len_b)
            res[res_index] += a[a_index] * b[b_index]
    for i in range(len(res)):
        res[i] = res[i]%2
    return res


def xor(a, b):
  
    a_degree = degree(a)
    b_degree = degree(b)
    a_size = len(a)
    b_size = len(b)
    if(a_size > b_size):
        b = resize(b, a_size)
    elif(a_size < b_size):
        a = resize(a, b_size) 
    res = []
    for i in range(a_size):
        res.append(a[i]^b[i])
    return res

def modulo(a, b):
  
    a_degree = degree(a)
    b_degree = degree(b)
    div_res_degree = a_degree
    div_res = [0] * div_res_degree
    remainder = a
    remainder_degree = degree(a)

    multi_res = []

    while remainder_degree >= b_degree:
        div_res_power = remainder_degree - b_degree 
        div_res_power_index = index_of_power(div_res_power, div_res_degree)
        div_res[div_res_power_index] = 1
        multi_res = multiply(div_res[div_res_power_index:], b)
        remainder = xor(remainder, multi_res)
        remainder_degree = degree(remainder)
    return remainder

def resize(binary, n):
    binary_size = len(binary)
    if(binary_size < n):
        binary = [0]*(n - binary_size) + binary
    elif(binary_size > n):
        binary = binary[binary_size-n:]
    return binary

def gf_multiply_modular(a,b,mod,m):
    multi_res = multiply(a,b)
    res = modulo(multi_res, mod)
  
    return resize(res, m)

a_string = '00000111'
b_string = '00000011'
mod_string ='100011011'
m = 8
a = list(map(lambda i:int(i), a_string))
b = list(map(lambda i:int(i), b_string))
mod = list(map(lambda i:int(i), mod_string))

print(f"Multiplication of '{a_string}' and '{b_string}' :",gf_multiply_modular(a,b, mod, m))
print('\n')

from BitVector import BitVector

mod = BitVector(bitstring=mod_string)    
a = BitVector(bitstring= a_string)
b = BitVector(bitstring= b_string)
quotient1, remainder1 = a.gf_divide_by_modulus(mod, m)
quotient2, remainder2 = b.gf_divide_by_modulus(mod, m)

print("Division by Modulos")
print('Quotient a:', quotient1)                            
print('Remainder a:',remainder1)
print('Quotient b:', quotient2)                            
print('Remainder b:',remainder2)

