class Solution(object):
    def countAsterisks(self, s):
        answer = 0
        for i in range(0,len(s.split('|')), 2):
            answer += s.split('|')[i].count('*')
        return answer