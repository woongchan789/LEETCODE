class Solution(object):
    def reverseVowels(self, s):
        temp = []
        final = ''
        cnt = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        for i in s:
            if i in vowels:
                temp.append(i)
        temp.reverse()
        
        for i in s:
            if i not in vowels:
                final += i
            else:
                final += temp[cnt]
                cnt += 1
                
        return final
        