array = [1, 2, 5, 7, 9, 8, 10]
def n_largest(n, arr: list):
    arr.sort()
    return arr[-n]

print(n_largest(3, array))
# >> 8
print(n_largest(4, array))
# >> 7

#  this doesn't seem like the most efficient solution
#  but this is the best I can think of for the time being
# I would assume that the time would be O(n) but I know theirs something
# I'm missing about the complexity of sorting, i think that it also has to
# iterate over the array to do its magic
