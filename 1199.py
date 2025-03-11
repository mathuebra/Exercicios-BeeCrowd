import sys
import math

def dec_to_hex(number):
    return False

def hex_to_dec(number):
    return False


for line in sys.stdin:
    if '0x' in line:
        size = len(line)
        result = hex_to_dec(line[2:size-1])
    
    