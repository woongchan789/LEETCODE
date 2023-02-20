class Solution(object):
    def isAnagram(self, s, t):
        
        def make_dict(string):
            cnt_dict = {}
            for i in string:
                if i not in cnt_dict:
                    cnt_dict[i] = string.count(i)
            return cnt_dict
        
        return False if make_dict(s) != make_dict(t) else True