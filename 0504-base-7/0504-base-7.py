class Solution(object):
    def convertToBase7(self, num):
        origin = num
        num = abs(num)
        answer = ''
        
        while num != 0:
            re = num % 7
            answer += str(re)
            num = num // 7
        
        if origin < 0:
            return '-' + answer[::-1]
        elif origin == 0:
            return '0'
        else:
            return answer[::-1]