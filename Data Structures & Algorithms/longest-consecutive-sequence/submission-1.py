class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        - for every number in nums, check if it has a left value or not
        - if it has, move to next number
        - if it doesn't, check if it has a right value
        """

        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numSet:
                count = 1
                while (n + count) in numSet:
                    count += 1
                longest = max(count,longest)
        return longest