# kata: https://www.codewars.com/kata/59c8b38423dacc7d95000008

# Now we will confect a reagent. There are eight materials to choose from, numbered 1,2,..., 8 respectively.

# We know the rules of confect:
# material1 and material2 cannot be selected at the same time
# material3 and material4 cannot be selected at the same time
# material5 and material6 must be selected at the same time
# material7 or  material8 must be selected(at least one, or both)

# ---
# Note: I struggled too much on this for an 8 kyu kata.

def isValid(formula):
    if (1 in formula) and (2 in formula):
        return False
    if (3 in formula) and (4 in formula):
        return False
    if (7 not in formula) and (8 not in formula):
        return False
    if (5 in formula) or (6 in formula):
        return True if (5 in formula and 6 in formula) else False
    return True