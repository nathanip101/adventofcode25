import math

from common import timed_execution

def part1(input_file):
    with open(input_file, "r") as f:
        columns = [
            [int(val) if val.isdigit() else val for val in line.strip().split(" ") if val]
            for line in f
        ]

        total = 0
        for *nums, operation in zip(*columns):
            if operation == '*':
                total += math.prod(nums)
            elif operation == '+':
                total += sum(nums)
    return total

def part2(input_file):
    with open(input_file, "r") as f:
        lines = [line.replace("\n", "") for line in f]
        total = 0
        nums = []
        operation = None
        for column in range(len(lines[0]) - 1, -1, -1):
            num = ""
            operation = lines[len(lines) - 1][column]
            for i in range(len(lines) - 1):
                if lines[i][column] == ' ':
                    if num:
                        break
                    continue
                num += lines[i][column]
            nums.append(int(num) if num else 0)
            if operation == '*':
                total += math.prod([num for num in nums if num])
                nums = []
            elif operation == '+':
                total += sum(nums)
                nums = []
        return total
        

if __name__ == "__main__":
    input_file = "day6/inputs/demo"
    print(f"Part 1 Result: {part1(input_file)}")
    print(f"Part 2 Result: {part2(input_file)}")