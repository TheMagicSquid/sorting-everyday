import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def small_sort(array):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(array)-1):
            if array[i+1] < array[i]:
                not_sorted = True
                array[i], array[i+1] = array[i+1], array[i]

    return array

def gort_sort(array):
    array_len = len(array)
    if array_len < 4:
        return small_sort(array)
    sorted_arrays = [[], [], [], []]
    for i in range(array_len):
        sorted_arrays[i%4].append(array[i])
    for i in range(4):
        sorted_arrays[i] = gort_sort(sorted_arrays[i])
    array = []
    i = 0
    while len(array) < array_len:
        for j in range(4):
            if len(sorted_arrays[j]) == 0:
                continue
            if len(array) <= i:
                array.append(sorted_arrays[j].pop(0))
                continue

            if sorted_arrays[j][0] < array[i]:
                array.insert(i, sorted_arrays[j].pop(0))
        i += 1
    
    return array


random_nums = random_numbers(20, 20)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))