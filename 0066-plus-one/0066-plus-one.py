class Solution(object):
    def plusOne(self, digits):
        arraytostr = ''
        final = []
        for i in range(len(digits)):
            arraytostr += str(digits[i])
        strtoarray = str(int(arraytostr) + 1)
        for i in range(len(strtoarray)):
            final.append(int(strtoarray[i]))
        return final