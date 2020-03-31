#This modules converts
#RGB values -> Hexadecimal
#Decimal - Hexadecimal - Binary

def hexcolor(r,g,b):
    hex_codes=[]
    r=hex(r)
    g=hex(g)
    b=hex(b)
    
    hex_codes.append(r)
    hex_codes.append(g)
    hex_codes.append(b)    
    hex_codes=[l.replace('0x','') for l in hex_codes]
    for i in range(len(hex_codes)):
        if len(hex_codes[i])==1:
            hex_codes[i]='0'+hex_codes[i]
        
    hex_color=''.join(hex_codes)
    hex_color='#'+hex_color
    return hex_color

class decimal:
    def binary(decimal_number):
        decimal_number=int(decimal_number)
        binary=list(bin(decimal_number))
        binary.pop(1)
        binary.pop(0)
        binary=''.join(binary)
        return binary
    def hexadecimal(decimal_number):
        decimal_number=int(decimal_number)
        hexadecimal=list(hex(decimal_number))
        hexadecimal.pop(1)
        hexadecimal.pop(0)
        hexadecimal=''.join(hexadecimal)
        return hexadecimal

class binary:
    def decimal(binary):
        binary_number=str(binary)
        if binary_number[0]=='0' and binary_number[1]=='b':
            binary_number=list(binary_number)
            binary_number.pop(1)
            binary_number.pop(0)
            binary_number=''.join(binary_number)
        decimal=str(int(binary_number,2))
        return decimal
    def hexadecimal(binary):
        binary_number=str(binary)
        if binary_number[0]=='0' and binary_number[1]=='b':
            binary_number=list(binary_number)
            binary_number.pop(1)
            binary_number.pop(0)
            binary_number=''.join(binary_number)
        decimal=int(binary_number,2)
        hexadecimal=list(hex(decimal))
        hexadecimal.pop(1)
        hexadecimal.pop(0)
        hexadecimal=''.join(hexadecimal)
        return hexadecimal

class hexadecimal:
    def decimal(hexadecimal):
        hex_number=str(hexadecimal)
        if hex_number[0]=="0" and hex_number[1]=="x":
            hex_number=list(hex_number)
            hex_number.pop(1)
            hex_number.pop(0)
            hex_number=''.join(hex_number)
        decimal=str(int(hex_number,16))
        return decimal
    def binary(hexadecimal):
        hex_number=str(hexadecimal)
        if hex_number[0]=="0" and hex_number[1]=="x":
            hex_number=list(hex_number)
            hex_number.pop(1)
            hex_number.pop(0)
            hex_number=''.join(hex_number)
        decimal=int(hex_number,16)
        binary=list(bin(decimal))
        binary.pop(1)
        binary.pop(0)
        binary=''.join(binary)
        return binary

