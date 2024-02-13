
# Brute Force Solution 
def find_left_sum(nums, i):
    sum = 0
    for j in range(0, i):
        sum = sum + nums[j]

    return sum


def find_right_sum(nums, i):
    sum = 0
    for j in range(i + 1, len(nums)):
        sum = sum + nums[j]

    return sum


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            left_sum = find_left_sum(nums, i)
            right_sum = find_right_sum(nums, i)

            if left_sum == right_sum:
                return i

        return -1

# better solution

class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
