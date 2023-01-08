def count_construct(string, word_bank, start=True, memo=None):
    if start:
        start = False
        memo = {}
    if string in memo: return memo[string]
    if string == '': return 1

    total_count = 0

    for sub in word_bank:
        if string.find(sub) == 0:
            number_ways =  count_construct(string[len(sub):len(string)], word_bank, start, memo)
            memo[string] = number_ways
            total_count += number_ways

    memo[string] = 0
    return total_count

print(count_construct("abcdef", ['ab', 'abc', 'cd', "def", 'abcd']))
print(count_construct("skateboard", ['bo', 'rd', 'ate', "t", 'ska', 'sk', 'boar']))
print(count_construct("enterapotentpot", ['a', 'p', 'ent', "enter", 'ot', 'o', 't']))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', "eeeee", 'eeeeee', 'eeeeeee']))

# very similar to the ones that count the sums of number and the ways to make those
