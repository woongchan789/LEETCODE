class Solution(object):
    def isPowerOfThree(self, n):
        answer_list = [3**i for i in range(0, len(str(n))*5)]
        return True if n in answer_list else False