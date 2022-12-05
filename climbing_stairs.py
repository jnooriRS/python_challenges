def climbing(n: int) -> int:
    input, comp = 1, 1
    for i in range(n - 1):
        temp = input
        input = input + comp
        comp = temp
    return input


print(climbing(5))

# def climbStairs(num):
#     a = 1
#     b = 1
#     n = num - 1
#     for i in range(n):
#         c = a
#         a = a + b
#         b = c
#     return a

# print(climbStairs(4))
