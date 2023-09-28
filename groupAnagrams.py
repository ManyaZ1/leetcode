class Solution(object):
    def groupAnagrams(self, strs):
        dict={}
        for string in strs:
            ls=[]
            sortedStr=str(sorted(string))
            if sortedStr in dict:
                dict[sortedStr].append(string)
            else:
                ls.append(string)
                dict[sortedStr]=ls
        
        my_list = list(dict.values())
        return my_list
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
#with defaultdict
"""def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())"""
