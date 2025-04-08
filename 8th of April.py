import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list


def gort_sort(array):
    size = round(pow(len(array),1/2))
    while size >= 1:
        size = int(size)
        averages = []
        group_num = 0
        sum = 0
        for i in range(len(array)):
            if i > (group_num+1)*size-1:
                averages.append(sum/size)
                sum = 0
                group_num += 1
            sum += array[i]
        group_num = (len(array)%size)
        if group_num == 0:
            averages.append(sum/size)
        else:
            averages.append(sum/group_num)

        averages_len = len(averages)
        for i in range(averages_len):
            minimum = i
            for j in range(i+1, averages_len):
                if averages[j] < averages[minimum]:
                    minimum = j
            for j in range(size):
                array[i*size+j], array[minimum*size+j] = array[minimum*size+j], array[i*size+j]
            averages[i], averages[minimum] = averages[minimum], averages[i]
        size = size/2

    return array
        
    

random_nums = random_numbers(20, 20)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
gort = gort_sort(random_nums)
print(gort)