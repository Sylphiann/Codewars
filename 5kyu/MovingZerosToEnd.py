# kata: https://www.codewars.com/kata/52597aa56021e91c93000cb0

# ---
# Should've just... pop and append... I facepalmed myself, full force, when I looked into the solutions
# What is this nesting conditionals monster have I just made
# My brother it's basic data structure... :(

def move_zeros(lst):
    if (lst == []) or (all(x == lst[0] for x in lst)):
        return lst
    index, zeros = 0, 0
    while (index + zeros < len(lst)):
        print(lst)
        if (zeros > 0):
            lst[index] = lst[index + zeros]
        while (lst[index] == 0):
            zeros += 1
            if (index + zeros) >= len(lst):
                break
            if lst[index + zeros] != 0:
                lst[index] = lst[index + zeros]
        index += 1
    if (zeros > 0):
        lst[-zeros:] = [0] * zeros
    return lst