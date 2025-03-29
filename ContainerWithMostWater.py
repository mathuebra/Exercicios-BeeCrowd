from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def volume(x, y):
            return x*y
        
        iterator_left = 0
        size = len(height)
        iterator_right = size - 1
        
    
        left = height[iterator_left]
        right = height[iterator_right]
        
        max_value = 0
        
        while iterator_left != iterator_right:
            if right <= left:
                actual = volume(right, abs(iterator_left - abs(iterator_right)))
                max_value = actual if actual > max_value else max_value
                iterator_right -= 1
                right = height[iterator_right]
            elif right > left:
                actual = volume(left, abs(iterator_left - abs(iterator_right)))
                max_value = actual if actual > max_value else max_value
                iterator_left += 1
                left = height[iterator_left]
                
        return max_value
            
print(Solution().maxArea(height=[1,8,6,2,5,4,8,3,7]))