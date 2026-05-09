class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            elements = []
            r_min, r_max = layer, m - 1 - layer
            c_min, c_max = layer, n - 1 - layer
            for c in range(c_min, c_max): elements.append(grid[r_min][c])
            for r in range(r_min, r_max): elements.append(grid[r][c_max])
            for c in range(c_max, c_min, -1): elements.append(grid[r_max][c])
            for r in range(r_max, r_min, -1): elements.append(grid[r][c_min])
            curr_k = k % len(elements)
            rotated = elements[curr_k:] + elements[:curr_k]
            i = 0
            for c in range(c_min, c_max):
                grid[r_min][c] = rotated[i]
                i += 1
            for r in range(r_min, r_max):
                grid[r][c_max] = rotated[i]
                i += 1
            for c in range(c_max, c_min, -1):
                grid[r_max][c] = rotated[i]
                i += 1
            for r in range(r_max, r_min, -1):
                grid[r][c_min] = rotated[i]
                i += 1
        return grid