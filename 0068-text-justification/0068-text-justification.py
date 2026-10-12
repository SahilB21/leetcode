class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        curr = []
        numLetters = 0
        for w in words:
            if numLetters + len(w) + len(curr) > maxWidth:
                for i in range(maxWidth-numLetters):
                    curr[i%(len(curr)-1 or 1)] += ' '
                ans.append(''.join(curr))
                curr = []
                numLetters = 0
            curr += [w]
            numLetters += len(w)
        return ans + [' '.join(curr).ljust(maxWidth)]