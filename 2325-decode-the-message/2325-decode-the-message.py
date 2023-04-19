class Solution(object):
    def decodeMessage(self, key, message):
        j = 0
        correct_dict = {}
        key = key.replace(' ', '')
        for i in key:
            if i not in correct_dict.keys():
                correct_dict[i] = chr(97+j)
                j += 1
            else:
                continue
        correct_dict[' '] = ' '
        answer = ''
        for k in message:
            answer += correct_dict[k]
        return answer