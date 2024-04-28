# kata: https://www.codewars.com/kata/563b662a59afc2b5120000c6

# ---
# Took my time figuring out how to count recursive calls

def nb_year(p0, percent, aug, p):
    if p0 >= p: return 0
    return 1 + nb_year(int(p0 + p0 * percent / 100 + aug), percent, aug, p)