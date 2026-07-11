class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        ans = 0
        
        for i in range(n):
            if not visited[i]:
                nodes = []
                queue = [i]
                visited[i] = True
                
                for node in queue:
                    nodes.append(node)
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                is_complete = True
                k = len(nodes)
                for node in nodes:
                    if len(adj[node]) != k - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    ans += 1
                    
        return ans