class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # movement is in four directions
        # 1 = land, 0 = water
        # should be surrounded by water 
        

        Rows, Cols = len(grid), len(grid[0])
        numberOfIslands = 0
        IslandVisited = set()

        def backtrack(row,col):
            
            if min(row,col) < 0 or row >= Rows or col >= Cols or (row,col) in IslandVisited or grid[row][col] == "0":
                return 0
            grid[row][col] = "0"
            
            IslandVisited.add((row,col))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in directions:
                backtrack(row+dr,col+dc)
            IslandVisited.remove((row,col))

        for row in range(Rows):
            for col in range(Cols):
                if (row,col) not in IslandVisited:
                    if grid[row][col] == "1":
                        backtrack(row,col)
                        numberOfIslands += 1
        return numberOfIslands