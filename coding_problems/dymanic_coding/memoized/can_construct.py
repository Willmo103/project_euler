# brute force approch

# def can_construct(string, word_bank):
#     if string == '': return True
#     for sub in word_bank:
#         if string.find(sub) == 0:
#             suffix = string[len(sub):len(string)]
#             if can_construct(suffix, word_bank) == True:
#                 return True
#     return False

# print(can_construct("abcdef", ['ab', 'abc', 'cd', "def", 'abcd']))
# print(can_construct("skateboard", ['bo', 'rd', 'ate', "t", 'ska', 'sk', 'boar']))
# print(can_construct("enterapotentpot", ['a', 'p', 'ent', "enter", 'ot', 'o', 't']))
# print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', "eeeee", 'eeeeee', 'eeeeeee']))




def can_construct(string, word_bank, start=True, memo=None):
    if start:
        start = False
        memo = {}
    if string in memo: return memo[string]
    if string == '': return True
    for sub in word_bank:
        if string.find(sub) == 0:
            suffix = string[len(sub):len(string)]
            if can_construct(suffix, word_bank, start, memo) == True:
                memo[string] = True
                return True

    memo[string] = False
    return False

print(can_construct("abcdef", ['ab', 'abc', 'cd', "def", 'abcd']))
print(can_construct("skateboard", ['bo', 'rd', 'ate', "t", 'ska', 'sk', 'boar']))
print(can_construct("enterapotentpot", ['a', 'p', 'ent', "enter", 'ot', 'o', 't']))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', "eeeee", 'eeeeee', 'eeeeeee']))
