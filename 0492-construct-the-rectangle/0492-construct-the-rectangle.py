class Solution(object):
    def constructRectangle(self, area):
        for i in range(int(area**0.5), 0, -1):
            if area % i == 0:
                return [area // i, i]
            else:
                continue