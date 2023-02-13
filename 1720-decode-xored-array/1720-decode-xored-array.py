class Solution(object):
    def decode(self, encoded, first):
        arr = [0] * (len(encoded) + 1)
        arr[0] = first
        for i in range(len(arr)-1):
            arr[i+1] = encoded[i] ^ arr[i]
        return arr
        