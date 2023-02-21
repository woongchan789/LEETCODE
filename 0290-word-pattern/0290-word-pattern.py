class Solution(object):
    def wordPattern(self, pattern, s):
        
        equivalence = {}

        words = s.split()
        if len(pattern) != len(words): return False

        for p, word in zip(pattern, words):
            if p in equivalence: 
                if word != equivalence[p]:
                    return False
            elif word in equivalence.values():
                    return False
            else:
                equivalence[p] = word
        return True
            