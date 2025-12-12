from common import timed_execution

def part1(input_file):
    with open(input_file, "r") as f:
        visited = set()
        # Construct the grid from the input file
        grid = [list(line.strip()) for line in f]
        rows = len(grid)
        cols = len(grid[0])

        # Do bfs to find all the split points
        def bfs(r, c):
            queue = [(r, c)]
            print(f"Starting at {grid[r][c]}")
            while queue:
                curr_r, curr_c = queue.pop(0)
                nr, nc = curr_r, curr_c
                while 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '^':
                    nr, nc = nr + 1, nc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == '^':
                    visited.add((nr, nc))
                    queue.append((nr, nc + 1))
                    queue.append((nr, nc - 1))


        bfs(0, cols // 2)
        return len(list(visited))
    
def part2_no_dp(input_file):
    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f]
        rows = len(grid)
        cols = len(grid[0])

    results = 0
    end_points = [(rows - 1, c) for c in range(cols)]
    visited = set()

    def dfs(r, c):
        nonlocal results
        if not (0 <= r < rows and 0 <= c < cols):
            return
        if (r, c) in visited: 
            return

        visited.add((r, c))
        
        if (r, c) in end_points:
            results += 1
        else:
            directions = [(1, 0)]
            if grid[r][c] == "^":
                directions = [(0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        visited.remove((r, c))

    dfs(0, cols//2)

    return results
    

def part2_dp(input_file):
    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f]
        rows = len(grid)
        cols = len(grid[0])

    dp = {}
    end_points = [(rows - 1, c) for c in range(cols)]

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return
        if (r, c) in dp: 
            return dp[(r, c)]

        if (r, c) in end_points:
            return 1
        
        directions = [(1, 0)]
        if grid[r][c] == "^":
            directions = [(0, 1), (0, -1)]

        dp[(r, c)] = sum([dfs(r + dr, c + dc) for dr, dc in directions])
        return dp[(r, c)]
    return dfs(0, cols//2)


                    
    
if __name__ == "__main__":
    input_file = "day7/inputs/input"
    print(f"Part 1 Result: {timed_execution(part1, input_file)}")
    print(f"Part 2 Result: {timed_execution(part2_dp, input_file)}")