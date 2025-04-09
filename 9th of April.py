import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def search(list, compare):
    for i in range(len(list)):
        if list[i] > compare:
            return i

def gort_sort(array):
    stacks = []
    minimum = []
    for i in array:
        result = search(minimum, i)
        if result == None:
            minimum.append(i)
            stacks.append([i])
            continue
        minimum[result] = i
        stacks[result].append(i)

    array = []
    min_len = len(minimum)
    while min_len > 0:
        mini_mini = 0
        for i in range(1, min_len):
            if minimum[i] < minimum[mini_mini]:
                mini_mini = i
        array.append(minimum[mini_mini])
        if len(stacks[mini_mini]) <= 1:
            minimum.pop(mini_mini)
            stacks.pop(mini_mini)
            min_len -= 1
            continue
        stacks_len = len(stacks[mini_mini])
        stacks[mini_mini].pop(stacks_len-1)
        minimum[mini_mini] = stacks[mini_mini][stacks_len-2]

    return array
        
    

random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
gort = gort_sort(random_nums)
print(gort)