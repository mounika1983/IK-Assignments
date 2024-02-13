# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:

#         freq = dict()

#         for elem in nums:
#             if elem in freq:
#                 freq[elem] += 1

#             else:
#                 freq[elem] = 1

#         for key in freq.keys():
#             if freq[key] > (len(nums) / 2):
#                 return key;

#         return -1
    
    
def example(a): 
	a = a + '2' 
	# a = a*2 
	return a 

example("hello")






