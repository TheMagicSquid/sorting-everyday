import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def merge_sorted_lists(array1, array2):
    newarray = []
    while len(array1) > 0 and len(array2) > 0:
        if array1[0] < array2[0]:
            value = array1.pop(0)
        else:
            value = array2.pop(0)
        newarray.append(value)
    if len(array1) > 0:
        newarray.extend(array1)
    else:
        newarray.extend(array2)
    return newarray

def gort_sort(array):
    if(len(array) <= 1):
        return array
    median = round(len(array)/2)
    return merge_sorted_lists(gort_sort(array[:median]), gort_sort(array[median:]))
    

random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))