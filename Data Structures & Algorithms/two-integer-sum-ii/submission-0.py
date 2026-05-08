class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1
        sums = 0

        while l < r:
            sums = numbers[r] + numbers[l]

            if sums == target:
                return [l + 1, r + 1]
            
            if sums < target:
                l = l + 1
            else:
                r = r - 1
        
        return []
            

            
                
        