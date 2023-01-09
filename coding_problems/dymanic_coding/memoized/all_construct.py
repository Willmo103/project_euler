
# def all_construct(target, word_bank):
#     if target == '': return [[]]

#     result = []

#     for sub in word_bank:
#         if target.find(sub) == 0:
#             suffix = target[len(sub):len(target)]
#             suffix_ways = all_construct(suffix, word_bank, start, memo)
#             target_ways = []
#             for way in suffix_ways:
#                 new_way = [sub, *way]
#                 target_ways.append(new_way)
#             result += target_ways
#     return result

# print(all_construct("abcdef", ['ab', 'abc', 'cd', "def", 'abcd']))
# print(all_construct("purple", ['purp', 'p', 'ur', "le", 'purpl']))
# print(all_construct("skateboard", ['bo', 'rd', 'ate', "t", 'ska', 'sk', 'boar']))
# print(all_construct("enterapotentpot", ['a', 'p', 'ent', "enter", 'ot', 'o', 't']))
# print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', "eeeee", 'eeeeee', 'eeeeeee']))

# THIS one took some time to try and sort out the map function that
# took me down a deep rabbit hole. The map function in JS doesn't exactly map to the
# same map function in python like I expected so ill put a pin in that to try and understand
# that a little better, or maybe there is another function that does a similar thing to map and
# forEach in JS. I'd love to know how to use something like that in python as they are
# some of my favorites in JS

# it was cool to learn about the spread operator in python as well as the fact you dont
# need to use it because you can just do [th, is] + [t, h, i, s] to get [th, is, t, h, i, s]



def all_construct(target, word_bank, start=True, memo=None):
    if start:
        start = False
        memo = {}
    if target in memo: return memo[target]
    if target == '': return [[]]

    result = []

    for sub in word_bank:
        if target.find(sub) == 0:
            suffix = target[len(sub):len(target)]
            suffix_ways = all_construct(suffix, word_bank, start, memo)
            target_ways = []
            for way in suffix_ways:
                new_way = [sub, *way]
                target_ways.append(new_way)
            result += target_ways


    memo[target] = result
    return result

print(all_construct("abcdef", ['ab', 'abc', 'cd', "def", 'abcd']))
print(all_construct("purple", ['purp', 'p', 'ur', "le", 'purpl']))
print(all_construct("skateboard", ['bo', 'rd', 'ate', "t", 'ska', 'sk', 'boar']))
print(all_construct("enterapotentpot", ['a', 'p', 'ent', "enter", 'ot', 'o', 't']))
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ['e', 'ee', 'eee', "eeeee", 'eeeeee', 'eeeeeee']))

# last example is how memoization cannot speed this up where it will still have to return a HUGE 2d array
# driving the complexity up a lot O(n^2)
