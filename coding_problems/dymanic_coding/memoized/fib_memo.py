
def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    result = fib(n-1, memo) + fib(n-2, memo)
    if result not in memo:
        memo[n] = result
    return result

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(1000))

# fist example of using a memo object to cut down recursion
