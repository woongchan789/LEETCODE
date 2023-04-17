class Solution(object):
    def arrayRankTransform(self, arr):
        store = {}
        sort_arr = sorted(set(arr))

        for i in range(len(sort_arr)):
            store[sort_arr[i]] = i+1

        
        for i in range(len(arr)):
            arr[i] = store[arr[i]]
        
        return arr