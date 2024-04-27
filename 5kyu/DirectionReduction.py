# kata: https://www.codewars.com/kata/550f22f4d758534c1100025a

# ---
# I'm tired, this is a really weird solution I must admit

pop_if = {"NORTH" : "SOUTH", "SOUTH" : "NORTH", "EAST" : "WEST", "WEST" : "EAST"}

def dir_reduc(arr):
    stack = []
    for wind in arr[:]:
        stack.append(arr.pop(0))
        if (len(arr) == 0):
            break
        if (arr[0] == pop_if.get(stack[-1])):
            stack.pop(-1)
            arr.pop(0)
            return dir_reduc(stack + arr)
    return stack
