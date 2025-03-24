class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)
        if '-' in number:
            number = int('-' + number[:0:-1])
        else:
            number = int(number[::-1])
        
        if number in range(-2**(31), 2**(31) -1):
            return number
        else:
            return 0
        
print(Solution().reverse(x=-123))