class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote_dict = {}
        magazine_dict = {}
        for i in range(len(magazine)):
            if magazine[i] not in magazine_dict:
                magazine_dict[magazine[i]] = 1
            else:
                magazine_dict[magazine[i]] = magazine_dict[magazine[i]] + 1
        for j in range(len(ransomNote)):
            if ransomNote[j] not in ransomNote_dict:
                ransomNote_dict[ransomNote[j]] = 1
            else:
                ransomNote_dict[ransomNote[j]] = ransomNote_dict[ransomNote[j]] + 1
        for idx, key in enumerate(ransomNote_dict):
            if (key not in magazine_dict) or (ransomNote_dict[key] > magazine_dict[key]):
                answer = False
                break
            else:
                answer = True
        return answer
            
