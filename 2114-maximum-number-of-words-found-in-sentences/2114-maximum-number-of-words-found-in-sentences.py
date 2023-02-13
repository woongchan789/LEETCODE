class Solution(object):
    def mostWordsFound(self, sentences):
        max_cnt = 0
        for i in sentences:
            temp = i.split()
            cnt = len(temp)
            if cnt > max_cnt:
                max_cnt = cnt
        return max_cnt
        