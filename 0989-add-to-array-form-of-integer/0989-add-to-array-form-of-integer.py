class Solution(object):
    def addToArrayForm(self, num, k):
        arraytoint = ''
        final = []
        for i in range(len(num)):
            arraytoint += str(num[i])
        inttoarray = str(int(arraytoint) + k)
        for i in range(len(inttoarray)):
            final.append(int(inttoarray[i]))
        return final
        