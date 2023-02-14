class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        sum = 0
        
        if len(arr)<=2:
            for i in arr:
                sum += i
        else:          
            cnt_list = list(i for i in range(1,len(arr)+1, 2))

            for i in cnt_list:
                for j in range(len(arr)+1-i):
                    for k in arr[j:j+i]:
                        sum += k
                
        return sum