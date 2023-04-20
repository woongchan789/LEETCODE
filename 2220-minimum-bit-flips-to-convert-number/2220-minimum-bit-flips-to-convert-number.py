class Solution(object):
    def minBitFlips(self, start, goal):
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        
        dif_len = abs(len(start_bin) - len(goal_bin))
        if len(start_bin)>len(goal_bin):
            for i in range(dif_len):
                goal_bin = '0' + goal_bin
        elif len(start_bin)<len(goal_bin):
            for i in range(dif_len):
                start_bin = '0' + start_bin
        
        answer = 0
        
        for i in range(len(start_bin)):
            answer += int(start_bin[i]) != int(goal_bin[i])
        
        return answer