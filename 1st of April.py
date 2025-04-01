import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def binary_search(array, item, end):
    l = -1
    r = end
    m = round((l+r)/2+0.1)
    while array[m] != item and r-l > 1:
        if array[m] < item:
            l = m
        else:
            r = m
        m = round((l+r)/2+0.1)
    return m
def gort_sort(array):
    for i in range(len(array)):
        item = array[i]
        sorted_pos = binary_search(array, item, i)
        array.pop(i)
        array.insert(sorted_pos, item)
    return array

random_nums = random_numbers(200, 1000)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))