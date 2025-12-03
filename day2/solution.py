def part1(input_file):
    sum = 0
    for line in open(input_file, 'r'):
        ranges = line.strip().split(',')
        for range in ranges:
            start, end = map(int, range.strip().split('-'))
            while start <= end:
                str_num = str(start)
                len_num = len(str_num)
                if len_num % 2 == 0:
                    if str_num[:len_num // 2] == str_num[len_num // 2:]:
                        sum += start
                start += 1
    return sum

def part2(input_file):
    sum = 0
    for line in open(input_file, 'r'):
        ranges = line.strip().split(',')
        for range in ranges:
            start, end = map(int, range.strip().split('-'))
            while start <= end:
                str_num = str(start)
                if str_num in (str_num + str_num)[1:-1]:
                    sum += start
                start += 1
    return sum



if __name__ == "__main__":
    input_file = "day2/inputs/input"
    print(f"Part 1: {part1(input_file)}")
    print(f"Part 2: {part2(input_file)}")