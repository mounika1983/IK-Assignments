class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for elem in nums:
            if elem in hset:  # O(1)
                return True
            else:
                hset.add(elem)


        return False



class Solution(object):
    def containsDuplicate(self, nums):
        set1 = set(nums) # O(n)
        
        if len(set1) == len(nums):
            return False

        return True