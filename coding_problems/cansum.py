
def can_sum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        remainder = targetSum - num
        if can_sum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))

# this is somehow always returning True now and I cannot figure out why the memo
# is breaking the code in this way.
