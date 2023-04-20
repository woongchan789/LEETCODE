class Solution(object):
    def maxDepth(self, s):
        m,c,n=0,0,len(s)
        for i in range(n):
            if s[i]=='(':
                c+=1
                m=max(c,m)
            elif s[i]==')':
                c-=1
        return m          