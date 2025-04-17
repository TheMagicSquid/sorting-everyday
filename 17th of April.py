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

def create_sorted_lists(array):
    sorted_array = []
    unsorted_array = []
    for i in array:
        if len(sorted_array) == 0 or sorted_array[-1] < i:
            sorted_array.append(i)
        else:
            unsorted_array.append(i)
    list_of_sorted_list = [sorted_array]
    if len(unsorted_array) > 0:
        list_of_sorted_list.extend(create_sorted_lists(unsorted_array))
    return list_of_sorted_list

def gort_sort(array):
    lists = create_sorted_lists(array)
    final_sort = lists[0]
    for i in range(1, len(lists)):
        final_sort = merge_sorted_lists(final_sort, lists[i])
    return final_sort

random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))