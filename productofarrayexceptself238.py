class Solution(object):
    
    def productExceptSelf(self, nums):
        l=len(nums)
        prefix=[1]*l
        postfix=[1]*l
        result=[1]*l
        
        #postfix[-1]=1
        for i in range(1,l):
            postfix[-1-i]=postfix[-i]*nums[-i]
            #result[-i-1]=postfix[-i-1]*prefix[-i-1]
        result[0]=postfix[0]
        for i in range(1,l):
            prefix[i]=nums[i-1]*prefix[i-1]
            result[i]=prefix[i]*postfix[i]

        return result


        """
        :type nums: List[int]
        :rtype: List[int]
        """
    def productExceptSelf_shortercode(self, nums): #ppio argh
        l=len(nums)
        prefix=1
        postfix=1
        result=[1]*l
        
        #postfix[-1]=1
        for i in range(1,l):
            result[i]=result[i-1]*nums[i-1]#prefix
        for i in range(l):
            result[-1-i]*=postfix
            postfix*=nums[-1-i]
            
        return result
     
    
    
    
    def productExceptSelfWITH_DIVISION(self, nums):
        result=1
        zerosF=0
        l=len(nums)
        for x in range(l):
            if(nums[x]!=0):
                result=result*nums[x]
            else: zerosF+=1
        ls=[]
        for i in range(len(nums)):
            if(zerosF==0):
                if(nums[i]!=0):
                    ls.append(result/nums[i])
                else: ls.append(result)
            elif(zerosF==1):
                if(nums[i]!=0):
                    ls.append(0)
                else: ls.append(result)
            else:
                ls.append(0)

        return ls

        """
        :type nums: List[int]
        :rtype: List[int]
        """

if __name__=="__main__" :
    p=Solution()
    nums=[1,2,3,4]
    l=[]*len(nums)
    l=p.productExceptSelf(nums)
    print(l)
    
