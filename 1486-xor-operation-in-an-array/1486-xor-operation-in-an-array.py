class Solution(object):
    def xorOperation(self, n, start):
        arr = []
        for i in range(n):
            arr.append(start + 2*i)
        answer = arr[0]
        for i in range(1, len(arr)):
            answer ^= arr[i]
        return answer
        