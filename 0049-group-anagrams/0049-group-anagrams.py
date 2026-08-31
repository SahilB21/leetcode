class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            letters = sorted(string)
            word = "".join(letters)
            if (word) not in result:
                result[word] = []
            result[word].append(string)
        
        return list(result.values())