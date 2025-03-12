import sys
import math

def dec_to_hex(number):
    result = ''
    while (number > 0):
        temp = number%16
        if temp == 10:
            result = 'A' + result
        elif temp == 11:
            result = 'B' + result
        elif temp == 12:
            result = 'C' + result
        elif temp == 13:
            result = 'D' + result
        elif temp == 14:
            result = 'E' + result
        elif temp == 15:
            result = 'F' + result
        else:
            result = str(temp) + result
        number = math.floor(number/16)
        
    return result

def hex_to_dec(number):
    number = number.upper()
    result = 0
    i = len(number)-1
    for char in number:
        if char == 'A':
            result = result + equation(10, i)
        elif char == 'B':
            result = result + equation(11, i)
        elif char == 'C':
            result = result + equation(12, i)
        elif char == 'D':
            result = result + equation(13, i)
        elif char == 'E':
            result = result + equation(14, i)
        elif char == 'F':
            result = result + equation(15, i)
        else: 
            result = result + equation(int(char), i)
        
        i = i - 1
        
    return result
                 
def equation(num, i):
    return num*(16**i)

for line in sys.stdin:
    line = line.strip()
    if '-' in line: break
    if '0x' in line:
        size = len(line)
        result = hex_to_dec(line[2:size])
    else:
        result = dec_to_hex(int(line))
        result = '0x' + str(result)
        
    print(result)