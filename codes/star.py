from collections import Counter

class Solution:
    def find_center(self, edges: List[List[int]]) -> int:
        "on star graph all edgees connect to center"
        return edges[0][0] if edges[0][0] in (edges[1][1], edges[1][0]) else edges[0][1]
