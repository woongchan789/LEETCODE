class Solution(object):
    def isIsomorphic(self, s, t):
        
        if len(s) != len(t):
            return False
        
        def newnumber(string):
            cnt_dict = {}
            cnt = 0
            new = []
            
            for i in string:
                if i not in cnt_dict:
                    new.append(cnt)
                    cnt_dict[i] = cnt
                    cnt += 1
                else:
                    new.append(cnt_dict[i])
            return new
        
        return False if newnumber(s) != newnumber(t) else True

        
        