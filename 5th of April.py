import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort(array):
    if len(array) <= 1:
        return array
    sum = 0
    for item in array:
        sum += item
    sum = sum/len(array)

    array1 = []
    array2 = []
    equal = True
    for item in array:
        if item < sum:
            array1.append(item)
            continue
        array2.append(item)
        if item != sum and equal:
            equal = False
    if equal:
        return array

    array1 = gort_sort(array1)
    array2 = gort_sort(array2)
    array1.extend(array2)

    return array1
    

random_nums = random_numbers(100, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
gort = gort_sort(random_nums)
print(gort)