import time, sys
sys.setrecursionlimit(10000)

# memo = {}

def how_sum(targetSum, numbers, memo=None, first=True):
    # global memo
    if first:
        first = False
        memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None
    for num in numbers:
        remainder = targetSum - num
        result_remainder = how_sum(remainder, numbers, memo, first)
        if result_remainder is not None:
            result_remainder.append(num)
            memo[targetSum] = result_remainder
            return result_remainder

    memo[targetSum] = None
    return None

print(how_sum(7, [2, 3]))
# memo = {}
print(how_sum(7, [5, 3, 4, 7]))
# memo = {}
print(how_sum(7, [2, 4]))
# memo = {}
print(how_sum(8, [2, 3, 5]))
# memo = {}
print(how_sum(300, [7, 14]))

# seems like issues with memo are fixed by creating a global dict
#  and resetting it in between each call of the external function
# possible computer is not clearing cache fast enough or at all in between
# the recursive calls of the function. Likely how python works in a way
# I seem to remember something about interpreted languages and cache management
# It would make sense since the calls to the function are using the ref of the data
#

# coding the same algo in javascript seems to act just like i assumed it would
# so I am left to assume that the way that python is interpreted is preventing the
# operation the way im attempting to code it here
# this could be alleviated with creating a decorator and wrapping the recursive calls
# and passing it the updated dict

# was able to refactor the code to set memo = None in the initial call,
# and set a boolean value to denote a first call the the recursion
# and then create memo as an empty dict to be passed along to the further
#  iterations thus allowing the cache under the hood to be cleared in between
# the individual calls to the function without having to declare a global memo
# variable.. YAY! ^_^ figured it out all on my own!!
#
