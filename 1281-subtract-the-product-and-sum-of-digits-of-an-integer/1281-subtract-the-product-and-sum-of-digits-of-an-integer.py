class Solution(object):
    def subtractProductAndSum(self, n):
        sep = []
        for i in str(n):
            sep.append(int(i))
        pod = sep[0]
        for i in range(len(sep)-1):
            pod *= sep[i+1]
        return pod - sum(sep)