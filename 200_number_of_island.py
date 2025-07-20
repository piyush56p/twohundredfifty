class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        visited = set()
        island = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                r,c = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    if (r+dr) in range(row) and (c+dc) in range(col) and ((r+dr, c+dc) not in visited) and grid[r+dr][c+dc] == "1":
                        q.append((r+dr, c+dc))  
                        visited.add((r+dr, c+dc))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island +=1 
        return island
