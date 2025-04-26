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

def get_average(array):
    sum = 0
    for i in array:
        sum += i
    return sum/len(array)

def gort_sort_once(array):
    pivot = array[random.randint(0,len(array)-1)]
    left_index = -1
    right_index = len(array)
    while left_index < right_index-1:
        value = array[left_index+1]
        if value > pivot:
            right_index -= 1
            array.pop(left_index+1)
            array.append(value)
        else:
            left_index += 1
    
    return array

def gort_sort(array):
    not_sorted = True
    while not_sorted:
        array = gort_sort_once(array)
        not_sorted = not is_sorted(array)

    return array


random_nums = random_numbers(20, 20)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))