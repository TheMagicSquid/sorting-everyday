import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def get_average(array):
    sum = 0
    for i in array:
        sum += i
    return sum/len(array)

def gort_sort(array):
    tasks = [[0, len(array)-1]]
    while len(tasks) > 0:
        l, r = tasks[0][0], tasks[0][1]
        tasks.pop(0)
        ll, rr = l, r
        average = get_average(array[l:r+1])
        is_average = True
        while l < r:
            if array[l] >= average:
                while array[r] > average and l < r:
                    r -= 1
                array[l], array[r] = array[r], array[l]
            elif array[l] != average:
                is_average = False
            l += 1
        if not is_average:
            if ll != l-1:
                tasks.append([ll,l-1])
            if rr != r:
                tasks.append([l-1,rr])
    return array

random_nums = random_numbers(200, 1000)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))
