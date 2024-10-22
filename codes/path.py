class Solution:
    def valid_path(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #generate graph
        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        #traverse
        queue = {source}
        while queue:
            if destination in queue:
                return True
            current = queue.pop()
            queue.update(graph[current])
            graph[current] = []
        return False
