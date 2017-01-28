def insertion_sort(arr):
    for position in range (0, len(arr)):
        i = position
        while (i > 0 and sort_two_words(arr[i], arr[i-1])):
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            i -= 1
    return(arr)
def sort_two_words(first, second, i = 0):
    if i == len(first):
        return True
    elif i == len(second):
        return False
    if first[i] < second[i]:
        return True
    elif first[i] > second[i]:
        return False
    elif first[i] == second[i]:
        return sort_two_words(first, second, i + 1)
