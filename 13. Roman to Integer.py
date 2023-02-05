class Solution(object):
    def romanToInt(self, s):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        four_nine_dict = {'IV':4, 'XL':40, 'CD':400, 'IX':9, 'XC':90, 'CM':900}

        num = 0
        count_len = 0
        while count_len <= len(s)-1:
            if count_len == len(s)-1:
                num += roman_dict[s[count_len]]
                break
            if (s[count_len] + s[count_len+1]) in four_nine_dict:
                num += four_nine_dict[s[count_len] + s[count_len+1]]
                count_len = count_len+2
            else:
                num += roman_dict[s[count_len]]
                count_len += 1
        return num
