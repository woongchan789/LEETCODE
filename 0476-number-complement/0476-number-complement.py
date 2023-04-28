class Solution(object):
    def findComplement(self, num):
        temp = '0b'
        for i in bin(num)[2:]:
            if int(i):
                temp += '0'
            else:
                temp += '1'
        return int(temp, 2)