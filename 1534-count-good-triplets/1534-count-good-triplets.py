class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):

        cnt = 0
        for i in range(len(arr)):
            for j in range(1, len(arr)):
                for k in range(2, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c \
                    and i<j<k:
                        cnt += 1
        return cnt