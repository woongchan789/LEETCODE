class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        rule_dict ={"type" : 0,
                    "color" : 1,
                    "name" : 2}
        cnt = 0
        
        for j in range(len(items)):
            if items[j][rule_dict[ruleKey]] == ruleValue:
                cnt += 1
                
        return cnt
                
        