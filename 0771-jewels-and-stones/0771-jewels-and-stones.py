class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        cnt_dict = {}
        
        for i in jewels:
            if i in stones and i not in cnt_dict:
                cnt_dict[i] = stones.count(i)
            elif i in stones and i in cnt_dict:
                continue
        
        return sum(cnt_dict.values())
        