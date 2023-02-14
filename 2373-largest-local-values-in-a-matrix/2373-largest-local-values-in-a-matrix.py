class Solution(object):
    def largestLocal(self, grid):
        
        temp = []
        final = []
        matrix = []
        
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                temp.append(max(grid[i][j:j+3]))
                temp.append(max(grid[i+1][j:j+3]))
                temp.append(max(grid[i+2][j:j+3]))
                final.append(max(temp))
                temp = []
            matrix.append(final)
            final = []
        
        return matrix
            