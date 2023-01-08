import time

def time_logger():
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"time: {start - end} seconds")
            return result
        return wrapper
    return decorator

@time_logger()
def best_sum(targetSum, numbers, start=True, memo=None):
    if start:
        memo = {}
        start = False
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortest = None

    for num in numbers:
        remainder = targetSum - num
        remainder_combination = best_sum(remainder, numbers, start, memo)
        if remainder_combination is not None:
            remainder_combination.append(num)
            if shortest is None or len(remainder_combination) < len(shortest):
                shortest = remainder_combination
            memo[targetSum] = remainder_combination

    memo[targetSum] = None
    return shortest

print(best_sum(7, [2, 3]))
print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(7, [2, 4]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(300, [7, 14, 30, 300]))


# in this one the main take away for me is that if the early return statement
# is in the numbers loop that will effect the ability to complete all of the
# calculations on all paths which we need to determine the shortest possible answer
# just a simple tweaking of the initial algo from the last 2 problems to get to the
# most efficient solution for the problem
