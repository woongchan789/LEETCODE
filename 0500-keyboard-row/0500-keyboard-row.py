class Solution(object):
    def findWords(self, words):
        final = []
        
        line1 = set("qwertyuiop")
        line2 = set("asdfghjkl")
        line3 = set("zxcvbnm")
        
        for i in words:
            if set(i.lower()).issubset(line1) or set(i.lower()).issubset(line2) or \
            set(i.lower()).issubset(line3):
                final.append(i)
                
        return final