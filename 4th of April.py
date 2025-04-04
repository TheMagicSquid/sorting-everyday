import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort(array):
    array_data = {}
    digit = 0
    for item in array:
        digit = max(digit, len(str(item)))
    if digit <= 1:
        return sort_single_digits(array)
    for i in range(len(array)):
        string_thing = str(array[i])
        if len(string_thing) != digit:
            if not "0" in array_data:
                array_data["0"] = []
            array_data["0"].append(string_thing)
            continue
        if not string_thing[0] in array_data:
            array_data[string_thing[0]] = []
        array_data[string_thing[0]].append(string_thing[1:])
    for i in array_data.keys():
        array_data[i] = gort_sort(array_data[i])

    return array_data

def ungort(dictonarty, previous):
    sorted_array = []
    if isinstance(dictonarty, list):
        for i in dictonarty:
            sorted_array.append(previous+i)
        return sorted_array
    for i in range(10):
        if str(i) in dictonarty:
            sorted_array.extend(ungort(dictonarty[str(i)], previous+str(i)))
    return sorted_array

def string_to_int(array):
    for i in range(len(array)):
        array[i] = int(array[i])
    return array

def sort_single_digits(array):
    new_array = []
    for i in range(10):
        for j in range(array.count(str(i))):
            new_array.append(str(i))
    return new_array

random_nums = random_numbers(100, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
gort = gort_sort(random_nums)
print(string_to_int(ungort(gort, "")))