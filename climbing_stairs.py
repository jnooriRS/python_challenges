def climbing(n: int) -> int:
    input, comp = 1, 1
    for i in range(n - 1):
        temp = input
        input = input + comp
        input = temp
    return input


print(climbing(8))
