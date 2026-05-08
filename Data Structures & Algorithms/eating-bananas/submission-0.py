class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        startRate,endRate = 1, max(piles)
        res = endRate

        while startRate <= endRate:
            midRate = (startRate + endRate)//2
            
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/midRate)

            if totalTime <= h:
                res = midRate
                endRate = midRate - 1
            else:
                startRate = midRate + 1
        return res
                
                

