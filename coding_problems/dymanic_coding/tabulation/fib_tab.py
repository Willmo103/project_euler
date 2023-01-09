# going back to the basics to understand tabulation for speeding up recursive problems

def fib(n):
    table = [0] * (n + 3)
    table[1] = 1
    for i in range(0, n):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    print(table)
    return table[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(9))
print(fib(50))

# im really learning a lot about the way that python differs from javascript
# as i make the code translations from the js tutorials. apparently js does't
#  care if you do operations to items outside of the currently defined array
# index but to get this to work first took figuring out why it wasn't and how to
# implement the changes to make it consistent for the further examples.
#
# MUST remember to fill indexes longer by furthest out operation preformed + 1

