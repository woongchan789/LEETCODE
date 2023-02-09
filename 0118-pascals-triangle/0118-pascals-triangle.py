class Solution(object):
    def generate(self, numRows):
        final = []
        
        for i in range(numRows):
            b = []
            b.append(1)
            
            if i==1:
                b.append(1)
            
            if i>=2:
                for j in range(i-1):
                    b.append(final[i-1][j] + final[i-1][j+1])
                b.append(1)

            final.append(b)
            
        return final