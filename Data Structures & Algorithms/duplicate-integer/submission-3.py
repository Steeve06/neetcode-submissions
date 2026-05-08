class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        found = False
        for num in nums:
            if num in arr:
                found =True
            else:
                arr.append(num)

        return found
