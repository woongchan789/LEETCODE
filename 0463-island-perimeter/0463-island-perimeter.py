class Solution(object):
    def islandPerimeter(self, grid):
        w = len(grid[0])
        h = len(grid)
        
        perimeter = 0
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i>0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j>0 and grid[i][j-1] == 1:
                        perimeter -= 2
                        
        return perimeter