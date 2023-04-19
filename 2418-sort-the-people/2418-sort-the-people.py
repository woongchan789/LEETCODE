class Solution(object):
    def sortPeople(self, names, heights):
        ans = []
        for i in range(len(heights)):
            ans.append([names[i], heights[i]])
        ans.sort(reverse=True, key=lambda x:x[1])
        return [name for name, height in ans]