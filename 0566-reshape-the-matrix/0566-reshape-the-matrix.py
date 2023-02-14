class Solution(object):
    def matrixReshape(self, mat, r, c):
        
        if r*c != len(mat)*len(mat[0]):
            return mat
        
        fc_list = [val for row in mat for val in row]
        
        final = []
        
        for i in range(0, len(fc_list), c):
            final.append(fc_list[i:i+c])
        
        return final