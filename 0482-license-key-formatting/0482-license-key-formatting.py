class Solution(object):
    def licenseKeyFormatting(self, s, k):
        st = ""
        s = s.replace("-","").upper()
        s = s[::-1]
    
        for i in range(0,len(s),k):
            st+=s[i:i+k]
            st+="-"
        sts=st[::-1]
       
        sts=sts.replace("-","",1)
        return sts
