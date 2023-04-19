class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        if len(set(arr)) == 1:
            return True
        elif len(set(arr)) != len(arr):
            return False
        else:
            answer = list(range(arr[0], arr[-1]+1, arr[1]-arr[0]))
        return True if answer==arr else False