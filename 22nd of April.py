import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort(array):
    pos = 0
    while pos < len(array):
        if (pos == 0 or array[pos] >= array[pos-1]):
            pos += 1
        else:
            array[pos], array[pos-1] = array[pos-1],array[pos]
            pos -= 1
    return array
    

random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))