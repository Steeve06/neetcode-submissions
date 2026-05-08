class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # movement is in all directions
        # just consider vertical and horizontal connections
        # if no island return 0
        

        Rows,Cols = len(grid),len(grid[0])
        islandVisited = set()
        areaOfIsland = 0

        def backtrack(row,col):
            if min(row,col) < 0 or row >= Rows or col >= Cols or (row,col) in islandVisited or grid[row][col] == 0:
                return 0
            
            islandVisited.add((row,col))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            area = 1
            for dr,dc in directions:
               area += backtrack(row+dr,col+dc)
            return area

        for row in range(Rows):
            for col in range(Cols):
                    areaOfIsland = max(areaOfIsland,backtrack(row,col))
        return areaOfIsland
        