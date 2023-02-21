class Solution(object):
    def addDigits(self, num):
        
        if num < 10:
            return num
        
        temp = 0
        while len(str(num)) != 1:
            for i in str(num):
                temp += int(i)
            num = temp
            temp = 0
        
        return num

        