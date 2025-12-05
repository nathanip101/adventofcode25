from collections import defaultdict, deque

def part1_naive(input_file):
    with open(input_file, "r") as f:
        # Convert input into 2d array
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
        
        accessible_rolls = 0
        rows = len(lines)
        cols = len(lines[0]) if rows > 0 else 0

        for r in range(rows):
            for c in range(cols):
                if lines[r][c] == '@':
                    adjacent_count = 0
                    for row_offset in [-1, 0, 1]:
                        for col_offset in [-1, 0, 1]:
                            if row_offset == 0 and col_offset == 0:
                                continue
                            adj_r = r + row_offset
                            adj_c = c + col_offset
                            if 0 <= adj_r < rows and 0 <= adj_c < cols:
                                if lines[adj_r][adj_c] == '@':
                                    adjacent_count += 1
                    if adjacent_count < 4:
                        accessible_rolls += 1
                        
        return accessible_rolls
    
def part1(input_file):
    with open(input_file, "r") as f:
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]
        # Convert input into 2d array
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
        
        accessible_rolls = 0
        rows = len(lines)
        cols = len(lines[0]) if rows > 0 else 0

        rolls = {(r, c) for r in range(rows) for c in range(cols) if lines[r][c] == '@'}

        neighbors = defaultdict(set)

        for r, c, in rolls:
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if (rr, cc) in rolls:
                    neighbors[(r, c)].add((rr, cc))

        for r, c in rolls:
            if len(neighbors[(r, c)]) < 4:
                accessible_rolls += 1

        return accessible_rolls
    
def part2_naive(input_file):
    with open(input_file, "r") as f:
        # Convert input into 2d array
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
        
        accessible_rolls = 0
        rows = len(lines)
        cols = len(lines[0]) if rows > 0 else 0

        while True:
            rolls_removed = 0
            for r in range(rows):
                for c in range(cols):
                    if lines[r][c] == '@':
                        adjacent_count = 0
                        for row_offset in [-1, 0, 1]:
                            for col_offset in [-1, 0, 1]:
                                if row_offset == 0 and col_offset == 0:
                                    continue
                                adj_r = r + row_offset
                                adj_c = c + col_offset
                                if 0 <= adj_r < rows and 0 <= adj_c < cols:
                                    if lines[adj_r][adj_c] == '@':
                                        adjacent_count += 1
                        if adjacent_count < 4:
                            accessible_rolls += 1
                            lines[r] = lines[r][:c] + '.' + lines[r][c+1:]
                            rolls_removed += 1
            if rolls_removed == 0:
                break
                        
        return accessible_rolls

def part2(input_file):
    with open(input_file, "r") as f:
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]
        # Convert input into 2d array
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
        
        accessible_rolls = 0
        rows = len(lines)
        cols = len(lines[0]) if rows > 0 else 0

        rolls = {(r, c) for r in range(rows) for c in range(cols) if lines[r][c] == '@'}

        neighbors = defaultdict(set)

        for roll in rolls:
            for row_offset, column_offset in directions:
                neighbor = roll[0] + row_offset, roll[1] + column_offset
                if neighbor in rolls:
                    neighbors[roll].add(neighbor)

        queue = deque([roll for roll in rolls if len(neighbors[roll]) < 4])

        while queue:
            roll = queue.popleft()
            if roll not in rolls:
                continue
            
            rolls.remove(roll)
            accessible_rolls += 1

            for neighbor in neighbors[roll]:
                neighbors[neighbor].remove(roll)
                if len(neighbors[neighbor]) < 4:
                    queue.append(neighbor)

        return accessible_rolls
    
def timed_execution(func, *args, **kwargs):
    import time
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
    return result

if __name__ == "__main__":
    input_file = "day4/inputs/input"


    print(f"Part 1 naive: {timed_execution(part1_naive, input_file)}")
    print(f"Part 1: {timed_execution(part1, input_file)}")
    print(f"Part 2 naive: {timed_execution(part2_naive, input_file)}")
    print(f"Part 2: {timed_execution(part2, input_file)}")