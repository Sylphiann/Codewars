# kata: https://www.codewars.com/kata/5a28cf591f7f7019a80000de

# In this Kata, you will be given a string of numbers in sequence and your task will be to return the missing number. 
# If there is no number missing or there is an error in the sequence, return -1
# The sequence will always be in ascending order.

# For example:
# missing("123567") = 4 
# missing("899091939495") = 92
# missing("9899101102") = 100
# missing("599600601602") = -1 -- no number missing
# missing("8990919395") = -1 -- error in sequence. Both 92 and 94 missing.

# ---
# Nesting monstrosity DX
def missing(s):
    digit = 1
    for i in range(len(s)):
        first, rest, miss = s[:digit], s[digit:], None
        print(first, rest, digit)
        for j in range(len(s)//digit):
            second = str(int(first) + 1)
            jump = str(int(first) + 2)
            if rest.startswith(second):
                first = rest[:len(second)]
                rest = rest[len(second):]
                continue
            elif rest.startswith(jump):
                if miss is None:
                    miss = int(jump)-1
                    first = rest[:len(jump)]
                    rest = rest[len(jump):]
                else:
                    miss = -1
        if (miss is not None) and (len(rest) == 0):
            return miss
        else:
            digit += 1
    return -1