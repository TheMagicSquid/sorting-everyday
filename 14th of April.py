import random

def random_numbers(amount, maxs):
    # Helper
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(0,maxs))
    return number_list

def gort_sort(array):
    bracket = []
    bra_round = []
    for i in range(round(len(array)/2+0.5)*2):
        if i >= len(array):
            bra_round.append(None)
            continue
        bra_round.append(i)
    bracket.append(bra_round)
    while len(bra_round) > 2:
        bra_round = []
        previous_bracket = bracket[len(bracket)-1]
        for i in range(0, round(len(previous_bracket)/2+0.5)*2, 2):
            if i >= len(previous_bracket):
                bra_round.append(None)
                continue
            if previous_bracket[i] == None:
                bra_round.append(previous_bracket[i+1])
                continue
            if previous_bracket[i+1] == None:
                bra_round.append(previous_bracket[i])
                continue
            if array[previous_bracket[i]] <= array[previous_bracket[i+1]]:
                bra_round.append(previous_bracket[i])
            else:
                bra_round.append(previous_bracket[i+1])
        bracket.append(bra_round)
    previous_bracket = bracket[-1]
    if array[previous_bracket[0]] <= array[previous_bracket[1]]:
        bracket.append([previous_bracket[0]])
    else:
        bracket.append([previous_bracket[1]])
    
    new_array = []
    win_index = bracket[-1][0]
    while win_index != None:
        new_array.append(array[win_index])
        bracket_index = bracket[0].index(win_index)
        bracket[0][bracket_index] = None
        for i in range(len(bracket)-1):
            new_index = round(bracket_index/2-0.4)
            brac_type = bracket_index ^ 1
            previous_bracket = bracket[i]
            if previous_bracket[bracket_index] == None:
                bracket[i+1][new_index] = previous_bracket[brac_type]
                bracket_index = new_index
                continue
            if previous_bracket[brac_type] == None:
                bracket[i+1][new_index] = previous_bracket[bracket_index]
                bracket_index = new_index
                continue
            if array[previous_bracket[bracket_index]] <= array[previous_bracket[brac_type]]:
                bracket[i+1][new_index] = previous_bracket[bracket_index]
            else:
                bracket[i+1][new_index] = previous_bracket[brac_type]
            bracket_index = new_index

        win_index = bracket[-1][0]
    return new_array



random_nums = random_numbers(200, 200)
print("Unsorted Array")
print(random_nums)
print("\nSorted Array")
print(gort_sort(random_nums))