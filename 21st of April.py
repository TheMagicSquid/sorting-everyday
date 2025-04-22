import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort2(array):
    # Failed today :(
    array.sort()

    return array

def gort_sort(array, k=10):
    #Bucket Sort
    if len(array) == 0:
        return []
    
    buckets = []
    maximum = array[0]
    for i in range(k):
        buckets.append([])

    for i in array:
        maximum = max(i, maximum)

    for i in range(len(array)):
        index = min(k - 1, round((k * array[i] / maximum) - 0.5))
        buckets[index].append(array[i])

    array = []
    for i in range(k):
        array.extend(gort_sort2(buckets[i]))

    return array
    

random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))