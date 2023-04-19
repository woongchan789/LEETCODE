class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x:x[1], reverse=True) 
        answer = 0
        for i in boxTypes:
            if i[0] < truckSize:
                answer += i[0]*i[1]
                truckSize -= i[0]
            else:
                answer += truckSize * i[1]
                break
        return answer