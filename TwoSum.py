from typing import List

'''
nums = [2, 7, 11, 15]
target = 9
output = [0, 1]
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for number in nums:
            j = 0
            while j < len(nums):
                if i == j:
                    j += 1
                    continue
                if (number + nums[j]) == target:
                    return [i, j]
                j += 1
            i += 1
            
print(Solution().twoSum(nums=[3,2,4], target=6))