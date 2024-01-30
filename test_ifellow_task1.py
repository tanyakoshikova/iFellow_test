import random


def get_min_max_average(len_arr=10):
    arr = []
    for i in range(len_arr):
        arr.append(random.uniform(0, 1))
    return min(arr), max(arr), sum(arr) / len_arr


minimum, maximum, average = get_min_max_average()
print(f'minimum: {minimum}, maximum: {maximum}, average: {average}')