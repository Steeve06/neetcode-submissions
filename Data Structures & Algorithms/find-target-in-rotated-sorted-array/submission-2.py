class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize left and right pointers
        # while left<=right, calculate the median
        # if target == median, return the median
        # Check if the left subarray is sorted
        # Check if the right subarray is sorted


        left,right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2

            if target == nums[mid]:
                return mid
            
            #check if left subarray is sorted.
            if nums[mid] >= nums[left]:
                if target > nums[mid] or  target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid]  or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
        