import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def find_below(array, pivot, start, end):
    for i in range(start, end+1):
        if array[i] < pivot:
            return i


def gort_sort(array):
    tasks = [[0, len(array)-1]]
    while len(tasks) > 0:
        l, r = tasks[0][0], tasks[0][1]
        tasks.pop(0)
        if l >= r:
            continue

        pivot = array[l]
        pivot_selected = False
        for i in range(l, r):
            if array[i] < pivot:
                continue
            result = find_below(array, pivot, i+1, r)
            if result == None:
                pivot_index = i
                pivot_selected = True
                break
            value = array.pop(result)
            array.insert(i, value)
        if not pivot_selected:
            pivot_index = r
    
        tasks.append([l, pivot_index - 1])
        tasks.append([pivot_index + 1, r])

    return array
        
    
random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
gort = gort_sort(random_nums)
print(gort)