# kata: https://www.codewars.com/kata/52efefcbcdf57161d4000091

# The main idea is to count all the occurring characters in a string. 
# If you have a string like "aba", then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    if len(s) < 0:
        return {}
    dic = dict()
    for chr in s:
        if chr not in dic:
            dic[chr] = 1
        else:
            dic[chr] = dic[chr] + 1
    return dic