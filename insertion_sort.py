def insertion_sort(arr):
    for position in range (0, len(arr)):
        i = position
        while(arr[i] > arr[i-1] and i > 0):
           temp = arr[i]
           arr[i] = arr[i - 1]
           arr[i - 1] = temp
           i -= 1
    return arr
if __name__ == "__main__":
    array = input()
    array = [int(x) for x in array.split(" ")]
    sorted_array = insertion_sort(array)
    print(sorted_array)
