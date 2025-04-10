import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def find_zero(array, digit, start):
    for i in range(start, len(array)):
        if len(array[i]) < digit:
            return i
        if array[i][len(array[i])-digit] == "0":
            return i


def gort_sort(array):
    max_length = 0
    array_len = len(array)
    for i in range(array_len):
        binary = bin(array[i])[2:]
        max_length = max(max_length, len(binary))
        array[i] = binary
    
    for i in range(max_length):
        for j in range(array_len):
            j_len = len(array[j])
            if j_len < i or array[j][j_len-i-1] == "0":
                continue
            result = find_zero(array, i+1, j+1)
            if result == None:
                break
            value = array.pop(result)
            array.insert(j, value)

    for i in range(array_len):
        array[i] = int(array[i], 2)
    return array
        
    
random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
gort = gort_sort(random_nums)
print(gort)