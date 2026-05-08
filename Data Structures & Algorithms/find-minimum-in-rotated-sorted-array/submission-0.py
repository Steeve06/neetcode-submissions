class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0 , len(nums)-1
        minElement = float("inf")

        while left <= right:
            mid = (left+right)//2
            minElement = min(minElement,nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return minElement
               

        