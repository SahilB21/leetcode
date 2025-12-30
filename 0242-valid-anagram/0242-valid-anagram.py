class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()
        if len(s) != len(t):
            return False
            
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        for letter in t:
            if letter in letters:
                if letters[letter] <= 0:
                    return False
                else:
                    letters[letter] -= 1
            else:
                return False
        return True

        