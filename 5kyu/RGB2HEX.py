# kata: https://www.codewars.com/kata/513e08acc600c94f01000001

# The rgb function is incomplete. 
# Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
# Valid decimal values for RGB are 0 - 255. 
# Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

def rgb(r, g, b):
    res = ""
    for val in [r, g, b]:
        if int(val) < 0 : res = res + "00"
        elif int(val) > 255 : res = res + "FF"
        else:
            res = res + "{:0>2}".format(hex(int(val))[2:].upper())
    return res