class Solution(object):
    def isPalindrome(self, s):

        new = ''.join(i for i in s if i.isalnum())
        new = list(new.lower())

        for i in range(len(new)//2):
            if new[i] != new[-(i+1)]:
                return False

        return True