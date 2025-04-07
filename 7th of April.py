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
        index1 = random.randint(0,len(array)-1)
        index2 = random.randint(0,len(array)-1)
        array[index1], array[index2] = array[index2], array[index1]
        not_sorted = not is_sorted(array)
    return array 
        
def is_sorted(array):

    previous = 0
    for i in array:
        if i < previous:
            return False
        previous = i
    return True
    

random_nums = random_numbers(7, 20)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
gort = gort_sort(random_nums)
print(gort)