import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

random_nums = random_numbers(20, 20)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
gort = gort_sort(random_nums)
print(gort)