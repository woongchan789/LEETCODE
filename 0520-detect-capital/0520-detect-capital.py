class Solution(object):
    def detectCapitalUse(self, word):
        if word[0].isupper():
            temp = 0
            for i in word:
                temp += i.isupper()
            return True if temp == 1 or temp == len(word) else False
        else:
            temp = 0
            for i in word:
                temp += i.islower()
            return False if temp != len(word) else True
        