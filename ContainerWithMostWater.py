from typing import List

'''
Ta errado porque eu esqueci de considerar o eixo de separação das
componentes verticais e também tem que considerar que tem que ser um
container inteiro, de forma que a água não vaze
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def volume(x, y):
            return x*y
        max = 0
        holder = 1
        for current in height:
            count = holder
            while count < len(height):
                actual = volume(current, height[count])
                max = actual if actual > max else max
                count += 1
            holder += 1
        
        return max

print(Solution().maxArea(height=[1,8,6,2,5,4,8,3,7]))