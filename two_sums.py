
def two_sums(target, target_list):
    # create hashmap storing each num as key and index as value
    num_to_index = {}

    for i, num in enumerate(target_list):
        compliment = target - num
        if compliment in num_to_index:
            return num_to_index[compliment], i
        num_to_index[num] = i


print(two_sums(3, [1, 4, 2])
      )
