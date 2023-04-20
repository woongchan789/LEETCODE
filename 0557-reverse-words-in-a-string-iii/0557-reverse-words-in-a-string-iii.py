class Solution(object):
    def reverseWords(self, s):
        reverse = ''
        for i in range(1, len(s)+1):
            reverse += s[-i]
        reverse = reverse.split(' ')
        answer = ''
        for i in range(1, len(reverse)+1):
            answer += reverse[-i] + ' '
        return answer[:-1]