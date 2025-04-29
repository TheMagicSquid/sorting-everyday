import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort(array):
    for i in range(len(array)):
        max_index = 0
        for j in range(len(array)-i):
            if array[j] < array[max_index]:
                max_index = j
        value = array.pop(max_index)
        array.append(value)
    return array


random_nums = random_numbers(20, 20)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))