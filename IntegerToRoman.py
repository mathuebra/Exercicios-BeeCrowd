import math

'''
num = 3749
resultado = MMMDCCXLIX
INCOMPLETO
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {
            1:'I',
            4:'IV',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }
        result = ''
        while num != 0:
            if num >= 1000:
                rest = num % 1000
                new = math.floor(num/1000)
                
                
                