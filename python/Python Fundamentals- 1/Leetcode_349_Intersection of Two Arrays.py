class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for elem in nums1:
            if (elem in nums2):
                if (not elem in ans):
                    ans.append(elem)

        return ans

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = list()
        unique_nums1 = list()

        for elem in nums1:
            if not elem in unique_nums1:
                unique_nums1.append(elem)

        unique_nums2 = list()

        for elem in nums2:
            if not elem in unique_nums2:
                unique_nums2.append(elem)

        for elem in unique_nums1:
            if elem in unique_nums2:  # O(n)
                result.append(elem)

        return result


# another solution

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        i = 0
        j = 0
        nums1.sort()
        nums2.sort()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if len(result) == 0:
                    result.append(nums1[i])
                else:
                    if result[-1] != nums1[i]:
                        result.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1

        return result


