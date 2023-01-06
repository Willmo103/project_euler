# def largest_prime(n: int, x: int = 2, p = 0) -> int:
#     if x >= n:
#         return x
#     if n % x == 0:
#         p = x
#         n = n / x
#     else:
#         x += 1
#     return largest_prime(n, x, p)

# print(largest_prime(600851475143))

def largest_prime(n):
    prime = None
    x = 2
    while x <= n:
        if n % x == 0:
            prime = x
            n = n / x
        else:
            x += 1
    return prime
print(largest_prime(600851475143))
