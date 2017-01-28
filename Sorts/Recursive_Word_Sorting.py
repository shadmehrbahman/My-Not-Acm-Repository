def sort_two_words(first, second, i = 0):
    if len(first) > len(second):
        first, second = second, first
    if i == len(first):
        return [first, second]
    if first[i] < second[i]:
        return [first, second]
    elif first[i] > second[i]:
        return [second, first]
    elif first[i] == second[i]:
        return sort_two_words(first, second, i + 1)
