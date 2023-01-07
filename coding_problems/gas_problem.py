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


# print(gas_station(gas, cost))

# this one was much more of a challenge, I initially wanted to use recursion
# to solve the problem passing the updated start and calling the function again
# had to look to the solution to get the problem right after thinking about it for a
# a while. I will have to revisit this one and see if i can make it work in another
# way to mix it up some.

def gas_station_2(gas, cost):
    current_gas = 0
    previous_gas = 0
    current_station = 0
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        if current_gas < 0:
            current_gas = 0
            current_station = i + 1
            previous_gas += current_gas
    if current_station == len(gas) or current_gas + previous_gas < 0:
        return -1
    else:
        return current_station

print(gas_station_2(gas, cost))

# this is the better solution, But i will still have to wrap my head around whats
# going on here. I understand that were skipping the stations where we run out of
# since we know that all stations in between cannot be that answer, but im still
# a little unclear as to why we know we can go from the end all the way back around
# again
#
# we use the previous gas amount as a check to see if there will be a < 0
# gas amount after reaching the end because this would indicate that if you used
# the gas you had at the end of the array to start from the start again we would still
# run out along the way thus there is no station that is valid otherwise the
# current station is returned as the valid station
#
