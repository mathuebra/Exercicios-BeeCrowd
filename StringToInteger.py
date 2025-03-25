class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        result = ''
        digit_count = 0
        minus_count = 0
        if len(s) == 0:
            return 0
        if s[0] == '-':
            minus_count += 1
            result = result + s[0]
            s = s[1:]
        for char in s:
            if char.isdigit() == False and digit_count != 0:
                break
            if char.isdigit():
                digit_count += 1
                result = result + char
            elif char == '+':
                digit_count += 1
                if minus_count > 0:
                    break
                continue
            else:
                break
        if result == '' or result == '-':
            return 0
    
        result = int(result)
        
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
            
        return result