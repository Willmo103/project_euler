import time, sys
sys.setrecursionlimit(10000)

memo = {}
def how_sum(targetSum, numbers):
    # print(targetSum)
    if targetSum in memo.keys(): return memo[targetSum]

    if targetSum == 0: return []
    if targetSum < 0: return None
    for num in numbers:
        remainder = targetSum - num
        result_remainder = how_sum(remainder, numbers)
        if result_remainder is not None:
            result_remainder.append(num)
            memo[targetSum] = result_remainder
            return result_remainder

    memo[targetSum] = None
    return None

print(how_sum(7, [2, 3]))
memo = {}
print(how_sum(7, [5, 3, 4, 7]))
memo = {}
print(how_sum(7, [2, 4]))
memo = {}
print(how_sum(4000, [2, 3, 5]))

# seems like issues with memo are fixed by creating a global dict
#  and resetting it in between each call of the external function
# possible computer is not clearing cache fast enough or at all in between
# the recursive calls of the function. Likely how python works in a way
# I seem to remember something about interpreted languages and cache management
# It would make sense since the calls to the function are using the ref of the data
#
