class Solution(object):
    def twoSum(self, nums, target):  #BEST O(N)
        seen={}
        for i in range(len(nums)):
            b=target-nums[i]
            if b in seen:
                return [seen[b],i]
            else:
                seen[nums[i]]=i    
    def twoSumDICTIONARYZIP (self, nums, target):  #O(2n) ????
        a=len(nums)
        roll_no = [ x for x in range(0,a) ]
        # using zip() to map values
        m = zip(nums, roll_no)
        mapped=dict(m)
        for i in range(0,a):
            b=target-nums[i]
            if b in mapped.keys() and mapped[b]!=i:
                return [i,mapped[b]]
            
    def twoSumN2(self, nums, target): #O(N^2)
        
    
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]"""
        ##################     BRUTE FORCE    ##################
        a=len(nums)
        for i in range(0,a):
            b=target-nums[i]
            for j in range (0,a):
                if(j!=i):
                    if (b==nums[j]):
                        l=[i,j]
                        return l
                        



if __name__=="__main__":
            nums=[3,2,4]
            p=Solution()
            l=p.twoSum(nums,6)
            print(l)
            
