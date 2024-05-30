# kata: https://www.codewars.com/kata/5672682212c8ecf83e000050

# ---
# Discovered the bisect module (whoo!)
import bisect

def dbl_linear(n):
    nums, index, dic = [1], 0,  dict()

    while (len(nums) <= 2*n):
        first = (nums[index] * 2) + 1
        dic[first] = dic.get(first, 0)
        if dic[first] == 0:
            bisect.insort_left(nums, first)
            dic[first] += 1

        second = (nums[index] * 3) + 1
        dic[second] = dic.get(second, 0)
        if dic[second] == 0:
            bisect.insort_left(nums, second)
            dic[second] += 1

        index += 1

    return nums[n]