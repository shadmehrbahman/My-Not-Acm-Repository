def bubble_sort (numbers):
    while True:
        for position in range (0, len(numbers)-1):
            if numbers[position] < numbers[position + 1]:
                numbers[position], numbers[position + 1] = numbers[position + 1], numbers[position]
                sw = True
        if sw == False:
            break
        sw = False
    return numbers

if __name__ == "__main__":
    numbers = [int(x) for x in input().strip().split()]
    sorted_arr = bubble_sort(numbers)
    print(sorted_arr)
