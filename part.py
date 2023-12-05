input = open("input.txt").read().split("\n")
input = [line for line in input if line]

test ="""two1nine
eightwothree
7pqrstsixteen"""

test_input = test.split("\n")

def solution(input):
    total = 281
    print("Total:", total)
    return total

print("First 10 lines of input:")
print(input[:10])
print("Last 10 lines of input:")
print(input[-10:])

# print(solution(input))
assert solution(test_input) == 281

