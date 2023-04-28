class Solution(object):
    def mergeArrays(self, nums1, nums2):
        temp = nums1 + nums2
        temp.sort(key=lambda x:x[0])

        temp_dict = {}

        for i in temp:
            if i[0] not in temp_dict:
                temp_dict[i[0]] = i[1]
            else:
                temp_dict[i[0]] += i[1]

        answer = []
        for key, val in temp_dict.items():
            answer.append([key,val])
        
        answer.sort(key=lambda x:x[0])
        
        return answer