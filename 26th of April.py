import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def is_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

def find_part(array, index):
    for i in range(index + 1, len(array)):
        if array[index] <= array[i]:
            return i
    return len(array)

def gort_sort_once(array):
    for i in range(len(array)):
        dound_index = find_part(array, i)
        array[i], array[dound_index-1] = array[dound_index-1], array[i]
    return array

def gort_sort(array):
    not_sorted = True
    while not_sorted:
        array = gort_sort_once(array)
        not_sorted = not is_sorted(array)

    return array


random_nums = random_numbers(20, 20)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))