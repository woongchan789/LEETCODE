class Solution(object):
    def addStrings(self, num1, num2):
        num1_len = len(num1)
        num2_len = len(num2)
        temp1 = 0
        for i in num1:
            temp1 += 10**(num1_len-1)*(ord(i)-48)
            num1_len -= 1
        for j in num2:
            temp1 += 10**(num2_len-1)*(ord(j)-48)
            num2_len -= 1
        return str(temp1)