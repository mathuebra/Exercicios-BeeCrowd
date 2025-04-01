import math

'''
num = 3749
resultado = MMMDCCXLIX
INCOMPLETO
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        def concat(result, value):
            return result + dictionary[value]
        dictionary = {
            1:'I',
            4:'IV',
            5:'V',
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
        mil = num - (num%1000)
        cen = (num%1000) - (num%100)
        dez = (num%100) - (num%10)
        uni = (num%10)
        while mil != 0:
            result = concat(result, 1000)
            mil -= 1000
        while cen != 0:
            if cen == 900:
                result = concat(result, 900)
                cen = 0
            elif cen >= 500:
                result = concat(result, 500)
                cen -= 500
            elif cen == 400:
                result = concat(result, 400)
                cen = 0
            else:
                result = concat(result, 100)
                cen -= 100
                
        while dez != 0:
            if dez == 90:
                result = concat(result, 90)
                dez = 0
            elif dez >= 50:
                result = concat(result, 50)
                dez -= 50
            elif dez == 40:
                result = concat(result, 40)
                dez = 0
            else:
                result = concat(result, 10)
                dez -= 10
                
        while uni != 0:
            if uni == 9:
                result = concat(result, 9)
                uni = 0
            elif uni >= 5:
                result = concat(result, 5)
                uni -= 5
            elif uni == 4:
                result = concat(result, 4)
                uni = 0
            else:
                result = concat(result, 1)
                uni -= 1
        return result
                
print(Solution().intToRoman(3912))
            
            
                
                
                