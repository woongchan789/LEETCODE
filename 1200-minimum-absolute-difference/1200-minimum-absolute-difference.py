class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_value = 10000
        answer = []
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) < min_value:
                min_value = arr[i+1] - arr[i]
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) == min_value:
                answer.append([arr[i],arr[i+1]])
        return answer