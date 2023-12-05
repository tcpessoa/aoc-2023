input = open("input2.txt").read().split("\n")
input = [line for line in input if line]

test ="""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

test_input = test.split("\n")

nums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def is_number(tmp_num):
    for num in nums:
        if num in tmp_num:
           return str(nums[num])
    return False

def solution(input):
    total = 0
    tmp_results = []
    for line in input:
        tmp = ''
        tmp_num = ''
        for char in line:
            if char.isdigit():
                tmp += char
                break
            if char.isalpha():
                tmp_num += char
                if is_number(tmp_num):
                    tmp += is_number(tmp_num) # type: ignore
                    tmp_num = ''
                    break
        for char in line[::-1]:
            if char.isdigit():
                tmp += char
                break
            if char.isalpha():
                tmp_num = char + tmp_num
                if is_number(tmp_num):
                    tmp += is_number(tmp_num) # type: ignore
                    tmp_num = ''
                    break
        tmp_results.append(tmp)
    for i, result in enumerate(tmp_results):
        if i < 10:
            print(input[i], result)
        if len(result) == 2:
            total += int(result)
    print("Total:", total)
    return total

print("First 10 lines of input:")
print(input[:10])
print("Last 10 lines of input:")
print(input[-10:])

print(solution(input))
assert solution(test_input) == 281

