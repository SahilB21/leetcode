class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        for i in range(len(s)):
            if s[i] in pairs.keys():
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    if pairs[stack[-1]] == s[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        