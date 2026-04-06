class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)#this constructs a hashmap where there is default list present


        for string in strs:
            count = [0] * 26 # 26 zeroes from a to z
            for char in string:
                count[ord(char)-ord("a")]+=1
            
            hashmap[tuple(count)].append(string)
        return list(hashmap.values())
        