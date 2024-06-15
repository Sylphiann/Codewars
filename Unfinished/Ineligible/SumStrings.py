# kata: https://www.codewars.com/kata/5324945e2ece5e1f32000370

# ---
# I accidentally proceeded to look at the tests which made me inelligible for this kata :(
from collections import deque

def sum_strings(x, y):
    # Strip 0s at the left of the String
    x = x.lstrip('0')
    y = y.lstrip('0')
    lenx, leny = len(x), len(y)

    # Special cases
    if lenx + leny == 0:
        return "0"
    elif lenx == 0:
        return y
    elif leny == 0:
        return x

    # Iterate through
    res = deque()
    over = 0
    pivot = lenx if lenx < leny else leny
    for i in range(-1, -pivot-1, -1):
        add = int(x[i]) + int(y[i]) + over
        over = 0
        if add > 9:
            over = int(str(add)[:-1])
            add = str(add)[-1]
        pivot = i
        res.appendleft(str(add))

    # TODO tomorrow
    if lenx != leny:
        # Making sure the x is the longer string
        (x, y, lenx, leny) = (y, x, leny, lenx) if lenx < leny else (x, y, lenx, leny)
        for i in range(pivot-1, -lenx-1, -1):
            add = int(x[i]) + over
            if add > 9:
                over = int(str(add)[:-1])
                add = str(add)[-1]
            res.appendleft(str(add))
    if over != 0:
        res.appendleft(over)

    return "".join(res)

print(sum_strings("00111001", "23"))