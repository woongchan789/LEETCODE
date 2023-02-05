class Solution(object):
    def kWeakestRows(self, mat, k):
        sum_list = []
        for i in range(len(mat)):
            sum_list.append(sum(mat[i]))
        idx = sorted(range(len(sum_list)), key=lambda k: sum_list[k])
        return idx[:k]
