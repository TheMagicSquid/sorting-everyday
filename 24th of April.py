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

def gort_sort(array):
    not_sorted = True
    while not_sorted:
        array.pop(random.randint(0,len(array)-1))
        not_sorted = not is_sorted(array)
    return array


random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))