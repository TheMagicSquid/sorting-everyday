import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort(array):
    big = 0
    for i in array:
        big = max(i+1, big)

    big_array = []
    for i in range(big):
        big_array.append(0)

    for i in array:
        big_array[i] += 1

    element_number = 0
    for i in range(big):
        for j in range(big_array[i]):
            array[element_number] = i
            element_number += 1

    return array


random_nums = random_numbers(100, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
gort = gort_sort(random_nums)
print(gort)