class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr12 = []
        arr = []
        arr1 = Counter(arr1)
        for i in arr2:
            arr12+=[i]*arr1[i]
        for i in arr1:
            if i not in arr2:
                arr+=[i]*arr1[i]
        return arr12+sorted(arr)