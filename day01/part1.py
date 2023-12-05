input = open("input.txt").read().split("\n")

test ="""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

test_input = test.split("\n")

def solution(input):
    total = 0
    tmp_results = []
    for line in input:
        tmp = ''
        for char in line:
            if char.isdigit():
                tmp += char
                break
        for char in line[::-1]:
            if char.isdigit():
                tmp += char
                break
        tmp_results.append(tmp)
    for result in tmp_results:
        if len(result) == 2:
            total += int(result)
    return total

# print(solution(input))
print(solution(test_input))
assert solution(test_input) == 142
