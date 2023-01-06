def even_fib_sum(a: int = 1, b: int = 2, sum: int = 2 ):
    if a >= 4000000 or b >= 4000000:
        print(sum)
        return
    next: int = a + b
    if next % 2 == 0:
        return even_fib_sum(b, next, sum + next)
    else:
        return even_fib_sum(b, next, sum)

even_fib_sum()
