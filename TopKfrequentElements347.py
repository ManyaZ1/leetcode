class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict={}
        for x in nums:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        sortedDict=sorted(dict.items(), key=lambda x:x[1])
        ls=[]
        for i in range(k):
            ls.append(sortedDict[-1-i][0])
        return ls
    
if __name__=="__main__":
            nums=[3,2,4,6,6,6,7,7]
            k=2
            p=Solution()
            l=p.topKFrequent(nums,k)
            print(l)
            