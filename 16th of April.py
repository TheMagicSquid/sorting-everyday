import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def add_to_tree(tree, value):
    if value < tree['d']:
        if tree['l'] != None:
            tree['l'] = add_to_tree(tree['l'], value)
        else:
            tree['l'] = {'d':value, 'l':None, 'r':None}
    else:
        if tree['r'] != None:
            tree['r'] = add_to_tree(tree['r'], value)
        else:
            tree['r'] = {'d':value, 'l':None, 'r':None}
    return tree

def untree(tree):
    array = []
    if tree['l'] != None:
        array.extend(untree(tree['l']))
    array.append(tree['d'])
    if tree['r'] != None:
        array.extend(untree(tree['r']))
    return array

def create_tree(array):
    tree = {'d':array[0], 'l':None, 'r':None}
    for value in array[1:]:
        tree = add_to_tree(tree, value)
    return tree

def gort_sort(array):
    tree = create_tree(array)
    array = untree(tree)
    return array


random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))