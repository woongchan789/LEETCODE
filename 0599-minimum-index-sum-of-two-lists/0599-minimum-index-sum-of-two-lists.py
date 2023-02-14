class Solution(object):
    def findRestaurant(self, list1, list2):
        M = 2000
        final = []
        for i in range(len(list1)):
            if list1[i] in list2:
                for j in range(len(list2)):
                    if list2[j] == list1[i] and M > i + j:
                        M = i + j
                        final = [list1[i]]
                    elif list2[j] == list1[i] and M == i + j:
                        final.append(list1[i])
        return final
                