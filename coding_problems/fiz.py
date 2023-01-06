def fizbuzz(x):
    for i in range(1, x):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 7 == 0:
            output += "Bazz"
        if i % 9 == 0:
            output += "Bozz"
        if not output:
            print(i)
        else:
            print(output)

fizbuzz(100)
