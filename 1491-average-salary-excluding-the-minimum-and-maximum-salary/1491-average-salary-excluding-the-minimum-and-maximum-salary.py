class Solution(object):
    def average(self, salary):
        salary.sort()
        return float(sum(salary[1:-1]))/float((len(salary)-2))