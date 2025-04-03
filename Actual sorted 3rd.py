import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort(array):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(array)-1):
            if array[i+1] < array[i]:
                not_sorted = True
                array[i], array[i+1] = array[i+1], array[i]

    return array


random_nums = random_numbers(20, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))