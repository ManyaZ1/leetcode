class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lettersS=[x for x in s]
        lettersT=[x for x in t]
        a= len(lettersS)
        b=len(lettersT)
        if(a!=b):
            return False
        lettersS.sort()
        lettersT.sort()
        for i in range(0,a):
            if (lettersS[i]!=lettersT[i]): return False
        return True
        """
        for y in range(0,a):
            success=0
            #search for lettersS[y]
            for j in range(0,len(lettersT)):
                if(lettersS[y]==lettersT[j]):
                    lettersT.pop(j)
                    success=1
                    break

            if(success==0):
                return False
        return True
         """       
        
