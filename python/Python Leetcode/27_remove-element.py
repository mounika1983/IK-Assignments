from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        
        return slow
    
    def removeElementViaFor(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        
        return i