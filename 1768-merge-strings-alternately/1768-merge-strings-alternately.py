class Solution(object):
    def mergeAlternately(self, word1, word2):
        max_len = min(len(word1), len(word2))
        answer = ''
        for i in range(max_len):
            answer += word1[i]
            answer += word2[i]
        if len(word1) < len(word2):
            answer += word2[i+1:]
        else:
            answer += word1[i+1:]
        return answer