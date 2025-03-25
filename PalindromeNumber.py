import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        size = len(word)
        
        if size % 2 == 0:
            count = 0          
            pointer1 = word[count]
            pointer2 = word[size - (1+count)]
            while pointer1 == pointer2:
                pointer1 = word[count]
                pointer2 = word[size - (1+count)]
                
                if count - (size-(1+count)) == -1:
                    return True
                count += 1
                
        else:
            center = math.floor(size/2)
            count = 1
            left = word[center - count]
            right = word[center + count]
            while left == right:
                left = word[center-count]
                right = word[center+count]
                
                if center - count == 0:
                    return True
                count += 1
                
        return False
    
print(Solution().isPalindrome(123))