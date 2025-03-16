'''
s = 'babad'
output = 'bab'
output = 'aba'
Qualquer uma das respostas ta certa
'''
import math

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
    
        start, max_lenght = 0, 0
        
        def expandAroundCenter(left: int, right: int):
            nonlocal start, max_lenght
            while left>=0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > max_lenght:
                    start = left
                    max_lenght = right - left + 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            expandAroundCenter(i, i)
            expandAroundCenter(i, i+1)
        
        return s[start: start + max_lenght]
        
        