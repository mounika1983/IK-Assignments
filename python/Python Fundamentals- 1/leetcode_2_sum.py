def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(0, len(nums)):
        num1 = nums[i]
        for j in range(i + 1, len(nums)):
            num2 = nums[j]
            if num1 + num2 == target:
                return [i, j]


list1 = [2, 10, 9, 20, 5, 7]
result = twoSum(list1, 11)
print(result)
