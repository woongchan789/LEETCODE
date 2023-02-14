class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.", \
                      "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        cnt_dict = {}
        
        for i in words:
            temp = ''
            for w in i:
                temp += morse_list[ord(w) - 97]
            if temp not in cnt_dict:
                cnt_dict[temp] = 1
        
        return len(cnt_dict)
        