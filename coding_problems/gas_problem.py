gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]

    #  start starting index of the gas array
    # current gas starts at 0 and adds the gas from the
    # starting station and subtracts the cost from the starting index
    # loop starting at the start
    # call function again start += 1
    # if current index > len(arr)
    # start at 0
    # if the current index = start
    # return start

# def can_traverse(gas, cost, start):
#     # print('start')
#     n = len(gas)
#     i = start
#     current_gas = 0
#     started = False
#     while n != start or not started:
#         started = True
#         current_gas += gas[i]
#         print(current_gas)
#         if current_gas - cost[i] < 1:
#             if start + 1 >= len(gas):
#                 start = 0
#             else:
#                 start += 1
#             can_traverse(gas, cost, start)
#         else:
#             current_gas -= cost[i]
#             # if i == start:
#             #     return start

# print(can_traverse(gas, cost, 0))


def can_traverse(gas, cost, start):
    n = len(gas)
    i = start
    current_gas = 0
    started = False
    while i != start or not started:
        started = True
        current_gas += gas[i] - cost[i]
        if current_gas < 0:
            return False
        i = (i + 1) % n
    return True


def gas_station(gas, cost):
    for i in range(len(gas)):
        if can_traverse(gas, cost, i):
            return i
    return -1


print(gas_station(gas, cost))

# this one was much more of a challenge, I initially wanted to use recursion
# to solve the problem passing the updated start and calling the function again
# had to look to the solution to get the problem right after thinking about it for a
# a while. I will have to revisit this one and see if i can make it work in another
# way to mix it up some.
