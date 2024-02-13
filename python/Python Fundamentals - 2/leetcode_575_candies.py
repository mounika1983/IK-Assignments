class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        set1 = set(candyType)
        unique_candies = len(set1)
        total_candies = len(candyType)

        if unique_candies >= (total_candies // 2):
            return (total_candies // 2)

        else:
            return unique_candies
