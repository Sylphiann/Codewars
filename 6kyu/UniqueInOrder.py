# kata: https://www.codewars.com/kata/54e6533c92449cc251001667

# Implement the function unique_in_order which takes as argument a sequence 
# and returns a list of items without any elements with the same value next to each other 
# and preserving the original order of elements.

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    list = []
    for char in sequence:
        if char not in list:
            list.append(char)
        if char != list[-1]:
            list.append(char)
    return list