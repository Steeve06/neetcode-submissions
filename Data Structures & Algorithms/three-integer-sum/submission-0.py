class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        - Check whether we have duplicates or not. To do that:
        - Iterate through each index and values of input array
        - If index>0 and first elmt a is equals to nums[index-1] + nums[index]
        - Continue to the next index and values
        - Use the rest of array to find 3sum given that l<r
        - 3sum = a + nums[l] + nums[r]
        - If 3sum<target, increase l and if it is greater decrease r
        - If 3sum equals target append all three values to a list
        - Update l and r for the while loop
        - To rule out duplicates, we increase l by 1 while l<r and nums[l]==nums[l-1]
        
        """
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    Sum = nums[i] + nums[j] + nums[k]
                    if Sum == 0 :
                        tmp = [nums[i],nums[k],nums[j]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]
      