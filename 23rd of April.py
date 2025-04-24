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

def find_spot(array, index):
	for i in range(len(array)-1):
		if array[i] <= array[index] and array[index] < array[i+1]:
			return i+1
	if array[index] < array[0]:
		return 0
	return len(array)

def gort_sort(array):
	notsorted = True
	while notsorted:
		for i in range(len(array)):
			index = find_spot(array, i)
			if not i == index-1:
				notsorted = True
			array.insert(index, array[i])
			if i > index:
				array.pop(i+1)
			else:
				array.pop(i)
		notsorted = not is_sorted(array)
	return array

random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))