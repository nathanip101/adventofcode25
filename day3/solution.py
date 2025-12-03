def get_joltage(input_file, digits):
    with open(input_file, 'r') as file:
        total_joltage = 0
        for line in file:
            bank = line.strip()
            total_joltage += _get_joltage(bank, digits)
        return total_joltage


def _get_joltage(bank, digits) -> int:
    if digits < 1:
        raise ValueError("Can't have 0 digit joltage...don't make sense")
    joltage = 0
    k = -1
    for i in range(digits - 1, -1, -1):
        max_digit = 0
        for j in range(len(bank) - i - 1, k, -1):
            max_digit = max(max_digit, int(bank[j]))
            if max_digit == int(bank[j]):
                k = j
        joltage += max_digit * (10 ** i)
    return joltage


if __name__ == "__main__":
    input_file = "day3/inputs/input"
    print(f"Part 1: {get_joltage(input_file, 2)}")
    print(f"Part 2: {get_joltage(input_file, 12)}")