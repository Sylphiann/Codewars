# kata: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

# ---
# Had fun doing this in 2 AM

def snail(snail_map):
    snail_map = list(snail_map)
    n = len(snail_map)
    if snail_map == [[]]:
        return []
    if n == 0:
        return []
    elif n == 1:
        return[snail_map[0][0]]

    position, result = [0, 0], [snail_map[0][0]]
    # I found a numerical pattern to traverse along the surface of the matrix
    for i in range(1, (n-1)*4):
        if ((i-1)//(n-1) == 0):
            position[1] += 1
        elif ((i-1)//(n-1) == 1):
            position[0] += 1
        elif ((i-1)//(n-1) == 2):
            position[1] -= 1
        elif ((i-1)//(n-1) == 3):
            position[0] -= 1
        result.append(snail_map[position[0]][position[1]])
    return result + snail(row[1:-1] for row in snail_map[1:-1])