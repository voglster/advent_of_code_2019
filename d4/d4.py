puzzle_input = "254032-789860"

low, high = puzzle_input.split("-")
low = int(low)
high = int(high)


def digits_dont_decrease(number):
    num = str(number)
    for a, b in zip(num[:-1], num[1:]):
        if int(b) < int(a):
            return False
    return True


def has_double_digit(number):
    num = str(number)
    return any(b == a for a, b in zip(num[:-1], num[1:]))


count = 0
for i in range(low, high + 1):
    if digits_dont_decrease(i) and has_double_digit(i):
        count += 1

print(count)
