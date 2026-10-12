class Solution:
    def checkRecord(self, n: int) -> int:
        last = [[0]*3 for _ in range(2)]
        current = [[0]*3 for _ in range(2)]
        last[0][0] = 1

        for i in range(n):
            for a in range(2):
                for l in range(3):
                    current[a][0] = (current[a][0] + last[a][l]) % (10**9 + 7)
                    if a == 0:
                        current[a+1][0] = (current[a+1][0] + last[a][l]) % (10**9 + 7)
                    if l < 2:
                        current[a][l+1] = (current[a][l+1] + last[a][l]) % (10**9 + 7)
            last = current
            current = [[0]*3 for _ in range(2)]
        
        count = 0
        for i in range(2):
            for j in range(3):
                count += last[i][j]
        return count % (10**9 + 7)