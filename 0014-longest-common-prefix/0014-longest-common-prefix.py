class Solution(object):
    def longestCommonPrefix(self, strs):
        n = 0
        min_len = 200
        correct_num = 0
        
        for i in range(len(strs)):
            if len(strs[i]) <= min_len:
                min_len = len(strs[i])
        
        while n < min_len:
            for j in range(len(strs)-1):
                correct_num += int(strs[j][n] == strs[j+1][n])
            if correct_num == (len(strs)-1):
                n += 1
                correct_num = 0
            else:
                break

        return strs[0][:n]



