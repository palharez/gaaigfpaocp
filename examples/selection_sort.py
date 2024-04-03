def find_smallest(arr):
    smallest = arr[0]
    smallets_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallets_index = i

    return smallets_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr

print(selection_sort([5,3,6,2,10]))
