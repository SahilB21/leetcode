class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        final = []
        for string in strs:
            letters = sorted(string)
            if ("".join(letters)) not in result:
                result[("".join(letters))] = []
            result[("".join(letters))].append(string)

        for word in result.keys():
            final.append(result[word])
        
        return final