def part1(input_file):
    with open(input_file, 'r') as file:
        sum = 0
        for line in file:
            tens_max = 0
            tens_idx = 0
            unit_max = 0
            bank = line.strip()
            for i in range(len(bank) - 2, -1, -1):
                tens_max = max(int(bank[i]), tens_max)
                if tens_max == int(bank[i]):
                    tens_idx = i
            for i in range (tens_idx + 1, len(bank)):
                unit_max = max(int(bank[i]), unit_max)
            sum += tens_max * 10 + unit_max
        return sum

def part2(input_file):
    with open(input_file, 'r') as file:
        total_joltage = 0
        for line in file:
            bank = line.strip()
            joltage = 0
            k = -1
            for i in range(11, -1, -1):
                max_digit = 0
                for j in range(len(bank) - i - 1, k, -1):
                    max_digit = max(max_digit, int(bank[j]))
                    if max_digit == int(bank[j]):
                        k = j
                joltage += max_digit * (10 ** i)
            total_joltage += joltage
        return total_joltage

if __name__ == "__main__":
    input_file = "day3/inputs/input"
    print(f"Part 1: {part1(input_file)}")
    print(f"Part 2: {part2(input_file)}")