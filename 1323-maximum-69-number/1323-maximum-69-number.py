class Solution(object):
    def maximum69Number (self, num):
        num = str(num)
        str_list = []
        for i in num:
            str_list.append(i) 
        for i in range(len(num)):
            if num[i] == '9':
                pass
            else:
                str_list[i] = '9'
                break
        answer = ''
        for i in str_list:
            answer += i
        return int(answer)