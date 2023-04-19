class Solution(object):
    def deleteGreatestValue(self, grid):
        temp_max = []
        answer = 0
        while grid[0] != []:
            for j in range(len(grid)):
                temp_max.append(max(grid[j]))
                grid[j].remove(max(grid[j]))
            answer += max(temp_max)
            temp_max = []
        return answer