# kata: https://www.codewars.com/kata/55c04b4cc56a697bb0000048

# Complete the function scramble(str1, str2) that returns true if a portion of 
# str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.

# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

# ---
# Today I learnt that a solution for this in one line exists using the modules from collections
# Though I'm quite proud with this solution that I came up with the complexity of O(m+n) instead of O(mn) 

def scramble(s1, s2):
    dic = dict()
    for i in range(len(s1)):
        char = s1[i]
        if char in dic:
            dic[char] = dic.get(char) + 1
        # For the sake of reducing complexity
        elif char in s2:
            dic[char] = dic.get(char, 0) + 1
    print(dic)
    for char in s2:
        if (char in dic) and (dic[char] > 0):
            dic[char] = dic.get(char) - 1
        else:
            print(char, dic)
            return False
    return True

print(scramble("rkqodlw", "world"))