# kata: https://www.codewars.com/kata/58ad317d1541651a740000c5

# --- 
# This one doesn't pass the performance test

# def middle_permutation(string):
    # perms = itertools.permutations(sorted(string))
    # string_list = [''.join(p) for p in perms]
    # return string_list[(len(string_list)//2) - 1]

#---
    # I found a pattern for the returned value, assuming the stringis already sorted; 
    # one for even length, and one for odd: (Syntax: [starting index : last index(excluded) : asc(1) or desc(-1)])
    # For even length: [n/2] + [n:n/2:-1] + [(n/2)-1:1:-1]
    # For odd length: [(n//2)+1] + [n//2] + [n:(n//2+1):-1] + [(n//2)-1:1:-1]
    # Adjusted to indexing from 0

# ---
def middle_permutation(string):
    sorted_str, n = ''.join(sorted(string)), len(string)
    if n == 3:
        return sorted_str[1] + sorted_str[0] + sorted_str[2]
    elif n < 3:
        return sorted_str
    if (len(string) % 2 == 1):
        return sorted_str[n//2] + sorted_str[(n//2)-1] + sorted_str[n:(n//2):-1] + sorted_str[(n//2)-2:0:-1] + sorted_str[0]
    else:
        return sorted_str[(n//2)-1] + sorted_str[n:(n//2)-1:-1] + sorted_str[(n//2)-2:0:-1] + sorted_str[0]