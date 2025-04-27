import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort(array):
    for i in range(len(array)):
        for j in range(i-1, -1, -1):
            if array[j] <= array[j+1]:
                break
            array[j], array[j+1] = array[j+1], array[j]
    return array

random_nums = random_numbers(20, 20)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))
