
# def can_sum(targetSum, numbers, memo={}):
#     if targetSum in memo: return memo[targetSum]
#     if targetSum == 0: return True
#     if targetSum < 0: return False

#     for num in numbers:
#         remainder = targetSum - num
#         if can_sum(remainder, numbers, memo) == True:
#             memo[targetSum] = True
#             return True

#     memo[targetSum] = False
#     return False

# print(can_sum(7, [2, 3]))
# print(can_sum(7, [5, 3, 4, 7]))
# print(can_sum(7, [2, 4]))
# print(can_sum(8, [2, 3, 5]))
# print(can_sum(300, [7, 14]))

# this is somehow always returning True now and I cannot figure out why the memo
# is breaking the code in this way.


def can_sum(targetSum, numbers, first=True, memo=None):
    if first:
        first = False
        memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        remainder = targetSum - num
        if can_sum(remainder, numbers, first, memo) == True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))

# similar to the answer to the next version of this problem I was able
# to deduce that the cache that python uses was keeping the same dict in between
# calls of the recursion and the outside calls to the function thus keeping the
# same dict and effecting the correctness of the answer, i.e. if the first call returned True
# than that value would be stored in the dict in between new calls to can_cum()
# this is fixed with adding a check for the initial call to the function and resetting the memo
# dict to an empty dict. I feel pretty good about this solution as it isn't requiring a
# global dict that still must be reset each call!
