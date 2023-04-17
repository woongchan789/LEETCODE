class Solution(object):
    def checkIfExist(self, arr):
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i]*2 in arr:
                if arr[i] == 0:
                    if arr.count(0) >= 2:
                        return True
                    else:
                        continue
                else:
                    return True
                
        return False