class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict1 and dict1[complement] != i:
                return [i, dict1[complement]]


# another solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict1:
                return [i, dict1[complement]]
            dict1[nums[i]] = i
