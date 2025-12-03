def part1(input_file):
    position = 50
    count = 0
    with open(input_file, 'r') as file:
        for line in file:
            direction = line[0]
            clicks = int(line[1:])
            if direction == "L":
                position = (position - clicks) % 100
            elif direction == "R":
                position = (position + clicks) % 100
            if position == 0:
                count += 1
    return count

def part2_naive(input_file):
    position = 50 
    count = 0
    with open(input_file, 'r') as file:
        for line in file:
            direction = line[0]
            clicks = int(line[1:])

            if direction == "L":
                for click in range(clicks):
                    position = (position - 1) % 100
                    if position == 0:
                        count += 1
                
            elif direction == "R":
                for click in range(clicks):
                    position = (position + 1) % 100
                    if position == 0:
                        count += 1
    return count

def part2_optimized(input_file):
    position = 50
    count = 0
    with open(input_file, 'r') as file:
        for line in file:
            direction = line[0]
            clicks = int(line[1:])

            if direction == "L":
                passes = (position - 1) // 100 - ((position - clicks - 1) // 100)
                count += passes
                position = (position - clicks) % 100

            elif direction == "R":
                passes = (position + clicks) // 100
                count += passes
                position = (position + clicks) % 100
    return count

            

if __name__ == "__main__":
    input_file = "day1/inputs/input"
    print(f"Part 1: {part1(input_file)}")
    print(f"Part 2 Naive: {part2_naive(input_file)}")
    print(f"Part 2 Optimized: {part2_optimized(input_file)}")