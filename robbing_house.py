# https://www.youtube.com/watch?v=73r3KWiEvyk
# Max value from robbing a row of houses but not next to each other

def skip_adjacent_house(num: list[int]) -> int:
    rob_house1, rob_house2 = 0, 0
    for n in num:
        incrementor = max(n + rob_house1, rob_house2)
        rob_house1 = rob_house2
        rob_house2 = incrementor
    return rob_house2


print(skip_adjacent_house([1, 2, 3, 1]))
# output should be four
