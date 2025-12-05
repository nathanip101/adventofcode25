import bisect 

def part1_naive(input_file):
    with open(input_file, "r") as f:
        # Go through lines and parse ranges and ids
        ranges = []
        ids = []
        parsing_ranges = True
        valid_count = 0
        for line in f.readlines():
            line = line.strip()
            if line == "":
                parsing_ranges = False
                continue
            if parsing_ranges:
                parts = line.split("-")
                ranges.append(range(int(parts[0]), int(parts[1])))
            else:
                ids.append(int(line))
        
        for id in ids:
            for r in ranges:
                if id in r:
                    valid_count += 1
                    break

    return valid_count


def part1(input_file):
    ranges = []
    ids = []
    parsing_ranges = True
    valid_count = 0
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                parsing_ranges = False
                continue
            if parsing_ranges:
                a, b = map(int, line.split("-"))
                ranges.append((a, b))
            else:
                ids.append(int(line))

    ranges.sort()
    consolidated = []

    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            consolidated.append((current_start, current_end))
            current_start, current_end = start, end

    consolidated.append((current_start, current_end))
    starts = [start for start, _ in consolidated]

    for id in ids:
        start_index = bisect.bisect_right(starts, id) - 1
        
        if start_index != 0:
            range_start, range_end = consolidated[start_index]
            if range_start <= id <= range_end:
                valid_count += 1
    return valid_count


def part2(input_file):
    ranges = []

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            a, b = map(int, line.split("-"))
            ranges.append((a, b))  # inclusive

    # Sort by starting point
    ranges.sort()

    total = 0
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start > current_end + 1:
            total += current_end - current_start + 1
            current_start, current_end = start, end
        else:
            current_end = max(current_end, end)

    total += current_end - current_start + 1
    return total

def timed_execution(func, *args):
    import time
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    return result

if __name__ == "__main__":
    input_file = "day5/inputs/input"

    print(f"Part 1 naive: {timed_execution(part1_naive, input_file)}")
    print(f"Part 1: {timed_execution(part1, input_file)}")
    print(f"Part 2: {timed_execution(part2, input_file)}")