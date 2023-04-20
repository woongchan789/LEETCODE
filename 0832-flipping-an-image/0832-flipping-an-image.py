class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image[0])
        # flip
        for i in range(n):
            image[i].reverse()
        # invert
        answer = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(int(bool(image[i][j]-1)))
            answer.append(temp)
        return answer