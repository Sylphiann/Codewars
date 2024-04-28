# kata: https://www.codewars.com/kata/54ba84be607a92aa900000f1

# ---
# I know there are one line solutions but wcyd

def is_isogram(string):
    dic = {}
    for char in string:
        if dic.get(char.lower()):
            return False
        else:
            dic[char.lower()] = True
    return True