class Solution:
    def find_judge(self, n: int, trust: List[List[int]]) -> int:
        trusted: List[int] = [0]*n
        trusts: List[int] = [0]*n
        for l in trust:
            trusts[l[0]-1] += 1
            trusted[l[1]-1] += 1

        for i in range(n):
            if trusted[i] == n-1 and not trusts[i]:
                return i+1
        return -1
