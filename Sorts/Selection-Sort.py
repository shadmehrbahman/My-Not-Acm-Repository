def selection_sort (numbers):
    for p1 in range(0, len(numbers)):
        imin = p1
        for p2 in range(p1, len(numbers)):
            if numbers[p2] > numbers[p1]:
                imin = p2
            if (imin > p1):
                numbers[imin], numbers[p1] = numbers[p1], numbers[imin]
    return numbers

if __name__ == "__main__":
    numbers = [int(x) for x in input().strip().split()]
    sorted_arr = selection_sort(numbers)
    print(sorted_arr)
