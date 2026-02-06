def two_sums(target, target_list):
    # create hashmap storing each num as key and index as value
    num_to_index = {}
    # loop through the list and get both the value(key ) and index(value) of each element
    for i, num in enumerate(target_list):
        # calculate the compliment on each element
        compliment = target - num
        # check if compliment already exists in our map
        if compliment in num_to_index:
            return num_to_index[compliment], i
        # else store the num at index i
        num_to_index[num] = i


print(two_sums(3, [1, 4, 2]))
